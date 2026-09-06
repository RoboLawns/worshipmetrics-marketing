import type { APIRoute } from 'astro';

const NOTIFY_RECIPIENT = 'paul@worshipmetrics.com';
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export const POST: APIRoute = async ({ request, locals }) => {
  let email = '';
  let name = '';
  let source = '';
  let honeypot = '';

  const contentType = request.headers.get('content-type') || '';
  if (contentType.includes('application/json')) {
    const body = await request.json().catch(() => ({}));
    email = String(body.email || '').trim();
    name = String(body.name || '').trim();
    source = String(body.source || '').trim();
    honeypot = String(body.website || '').trim();
  } else {
    const formData = await request.formData();
    email = String(formData.get('email') || '').trim();
    name = String(formData.get('name') || '').trim();
    source = String(formData.get('source') || '').trim();
    honeypot = String(formData.get('website') || '').trim();
  }

  // Honeypot filled in means a bot — pretend success, store nothing.
  if (honeypot) {
    return new Response(JSON.stringify({ ok: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  }

  if (!email || !EMAIL_PATTERN.test(email)) {
    return new Response(JSON.stringify({ ok: false, error: 'Please enter a valid email address.' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const runtimeEnv = (locals as { runtime?: { env?: Record<string, string> } }).runtime?.env;
  const resendApiKey = runtimeEnv?.RESEND_API_KEY;
  const resendFromEmail = runtimeEnv?.RESEND_FROM_EMAIL || 'WorshipMetrics <no-reply@worshipmetrics.com>';
  const resendAudienceId = runtimeEnv?.RESEND_AUDIENCE_ID;

  if (!resendApiKey) {
    return new Response(JSON.stringify({ ok: false, error: 'Signup is temporarily unavailable.' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  // Add to the Resend audience when one is configured — the durable list.
  if (resendAudienceId) {
    const contactResponse = await fetch(`https://api.resend.com/audiences/${resendAudienceId}/contacts`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${resendApiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        first_name: name || undefined,
        unsubscribed: false,
      }),
    });

    // 409 means the contact already exists — that is a success from the subscriber's side.
    if (!contactResponse.ok && contactResponse.status !== 409) {
      return new Response(JSON.stringify({ ok: false, error: 'Signup failed. Please try again.' }), {
        status: 502,
        headers: { 'Content-Type': 'application/json' },
      });
    }
  }

  // Notify Paul so signups are visible even before sequences exist.
  await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${resendApiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: resendFromEmail,
      to: [NOTIFY_RECIPIENT],
      subject: 'New newsletter signup - WorshipMetrics',
      text: [
        'New newsletter signup',
        '',
        `Email: ${email}`,
        `Name: ${name || 'Not provided'}`,
        `Source: ${source || 'Not provided'}`,
      ].join('\n'),
    }),
  }).catch(() => {});

  return new Response(JSON.stringify({ ok: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
};
