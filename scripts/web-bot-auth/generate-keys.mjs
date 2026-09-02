// Generates the Web Bot Auth Ed25519 keypair for worshipmetrics.com.
//
// Writes:
//   keys/web-bot-auth-ed25519.private.jwk.json   (gitignored — never commit)
//   public/.well-known/http-message-signatures-directory   (public JWKS)
//
// Re-running rotates the key: it overwrites both files, so the published
// directory always matches the private key on disk. Existing signed
// requests keep verifying until their `expires` window passes only if the
// old public key stays in the directory — for a clean rotation, append the
// new key to `keys` instead of replacing (edit below), deploy, then drop
// the old one after a day.
//
// Usage: node scripts/web-bot-auth/generate-keys.mjs

import { generateKeyPairSync, createHash } from "node:crypto";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "..", "..");

const { publicKey, privateKey } = generateKeyPairSync("ed25519");
const publicJwk = publicKey.export({ format: "jwk" }); // { kty: "OKP", crv: "Ed25519", x }
const privateJwk = privateKey.export({ format: "jwk" }); // adds d

// RFC 7638 thumbprint: SHA-256 over the required members in lexicographic
// order, base64url — used as the `keyid` in Signature-Input.
const thumbprintInput = JSON.stringify({
  crv: publicJwk.crv,
  kty: publicJwk.kty,
  x: publicJwk.x,
});
const kid = createHash("sha256").update(thumbprintInput).digest("base64url");

const directory = {
  keys: [
    {
      kty: publicJwk.kty,
      crv: publicJwk.crv,
      x: publicJwk.x,
      kid,
      use: "sig",
    },
  ],
};

const privatePath = join(repoRoot, "keys", "web-bot-auth-ed25519.private.jwk.json");
mkdirSync(dirname(privatePath), { recursive: true });
writeFileSync(privatePath, JSON.stringify({ ...privateJwk, kid, use: "sig" }, null, 2) + "\n");

const directoryPath = join(
  repoRoot,
  "public",
  ".well-known",
  "http-message-signatures-directory",
);
mkdirSync(dirname(directoryPath), { recursive: true });
writeFileSync(directoryPath, JSON.stringify(directory, null, 2) + "\n");

console.log(`kid: ${kid}`);
console.log(`private key: ${privatePath}`);
console.log(`directory:   ${directoryPath}`);
