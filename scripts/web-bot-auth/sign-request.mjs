// Signs an outbound HTTP request per Web Bot Auth (IETF webbotauth WG:
// RFC 9421 HTTP Message Signatures with tag="web-bot-auth"), so receiving
// sites can verify the request came from WorshipMetrics by fetching our
// key directory at
// https://worshipmetrics.com/.well-known/http-message-signatures-directory.
//
// Usage:
//   node scripts/web-bot-auth/sign-request.mjs <url>          # print headers
//   node scripts/web-bot-auth/sign-request.mjs <url> --send   # GET with headers
//
// Any WorshipMetrics crawler/agent code can import signAgentRequest()
// instead and attach the returned headers to its own fetch.

import { createPrivateKey, createHash, randomBytes, sign as edSign } from "node:crypto";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const SIGNATURE_AGENT = "https://worshipmetrics.com";
const KEY_PATH = join(
  dirname(fileURLToPath(import.meta.url)),
  "..",
  "..",
  "keys",
  "web-bot-auth-ed25519.private.jwk.json",
);

export function signAgentRequest(url, { validitySeconds = 300 } = {}) {
  const jwk = JSON.parse(readFileSync(KEY_PATH, "utf8"));
  const key = createPrivateKey({ key: jwk, format: "jwk" });
  const kid =
    jwk.kid ??
    createHash("sha256")
      .update(JSON.stringify({ crv: jwk.crv, kty: jwk.kty, x: jwk.x }))
      .digest("base64url");

  const authority = new URL(url).host;
  const created = Math.floor(Date.now() / 1000);
  const expires = created + validitySeconds;
  const nonce = randomBytes(32).toString("base64");

  const signatureAgentField = `"${SIGNATURE_AGENT}"`;
  const params =
    `("@authority" "signature-agent")` +
    `;created=${created};expires=${expires}` +
    `;keyid="${kid}";nonce="${nonce}";tag="web-bot-auth"`;

  const signatureBase =
    `"@authority": ${authority}\n` +
    `"signature-agent": ${signatureAgentField}\n` +
    `"@signature-params": ${params}`;

  const signature = edSign(null, Buffer.from(signatureBase, "utf8"), key);

  return {
    "Signature-Agent": signatureAgentField,
    "Signature-Input": `sig1=${params}`,
    Signature: `sig1=:${signature.toString("base64")}:`,
  };
}

const isMain = process.argv[1] === fileURLToPath(import.meta.url);
if (isMain) {
  const url = process.argv[2];
  if (!url) {
    console.error("Usage: node scripts/web-bot-auth/sign-request.mjs <url> [--send]");
    process.exit(1);
  }
  const headers = signAgentRequest(url);
  for (const [name, value] of Object.entries(headers)) {
    console.log(`${name}: ${value}`);
  }
  if (process.argv.includes("--send")) {
    const res = await fetch(url, { headers });
    console.log(`\n${res.status} ${res.statusText} from ${url}`);
  }
}
