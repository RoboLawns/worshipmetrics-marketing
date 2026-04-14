import type { APIRoute } from 'astro';

const PILOT_RECIPIENT = 'paul@worshipmetrics.com';

function escapeHtml(value: string) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

export const POST: APIRoute = async ({ request, redirect, locals }) => {
  const formData = await request.formData();
  const payload = {
    churchName: String(formData.get('church_name') || '').trim(),
    yourName: String(formData.get('your_name') || '').trim(),
    email: String(formData.get('email') || '').trim(),
    phone: String(formData.get('phone') || '').trim(),
    congregationSize: String(formData.get('congregation_size') || '').trim(),
    servicesPerWeek: String(formData.get('services_per_week') || '').trim(),
    notes: String(formData.get('notes') || '').trim(),
  };

  if (!payload.churchName || !payload.yourName || !payload.email || !payload.congregationSize || !payload.servicesPerWeek) {
    return new Response('Missing required fields', { status: 400 });
  }

  const runtimeEnv = (locals as { runtime?: { env?: Record<string, string> } }).runtime?.env;
  const resendApiKey = runtimeEnv?.RESEND_API_KEY;
  const resendFromEmail = runtimeEnv?.RESEND_FROM_EMAIL || 'WorshipMetrics <no-reply@worshipmetrics.com>';

  if (!resendApiKey) {
    return new Response('Missing RESEND_API_KEY', { status: 500 });
  }

  const text = [
    'New Pilot Program Request',
    '',
    `Church Name: ${payload.churchName}`,
    `Your Name: ${payload.yourName}`,
    `Email: ${payload.email}`,
    `Phone: ${payload.phone || 'Not provided'}`,
    `Congregation Size: ${payload.congregationSize}`,
    `Services per week: ${payload.servicesPerWeek}`,
    '',
    'Questions / Notes:',
    payload.notes || 'None provided',
  ].join('\n');

  const html = `
    <h1>New Pilot Program Request</h1>
    <p><strong>Church Name:</strong> ${escapeHtml(payload.churchName)}</p>
    <p><strong>Your Name:</strong> ${escapeHtml(payload.yourName)}</p>
    <p><strong>Email:</strong> ${escapeHtml(payload.email)}</p>
    <p><strong>Phone:</strong> ${escapeHtml(payload.phone || 'Not provided')}</p>
    <p><strong>Congregation Size:</strong> ${escapeHtml(payload.congregationSize)}</p>
    <p><strong>Services per week:</strong> ${escapeHtml(payload.servicesPerWeek)}</p>
    <p><strong>Questions / Notes:</strong></p>
    <p>${escapeHtml(payload.notes || 'None provided').replaceAll('\n', '<br />')}</p>
  `;

  const resendResponse = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${resendApiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: resendFromEmail,
      to: [PILOT_RECIPIENT],
      reply_to: payload.email,
      subject: 'New Pilot Program Request - WorshipMetrics',
      text,
      html,
    }),
  });

  if (!resendResponse.ok) {
    const errorText = await resendResponse.text();
    return new Response(`Resend error: ${errorText}`, { status: 502 });
  }

  return redirect('/pilot-program/thank-you', 303);
};
