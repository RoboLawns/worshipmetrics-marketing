# WorshipMetrics auth.md

This file follows the Auth.md convention: it tells AI agents and other
automated clients how authentication and registration work for
WorshipMetrics, so nothing has to be guessed or scraped.

## Who this is for

AI agents, MCP clients, and automated tools that want to work with
WorshipMetrics, the all-in-one platform for church worship and production
teams at <https://app.worshipmetrics.com>.

## Open without credentials

No registration or credentials are needed for any of these:

- **MCP server** — `https://worshipmetrics.com/mcp/` (Streamable HTTP).
  Server card: <https://worshipmetrics.com/.well-known/mcp/server-card.json>.
  Its tools expose public product information only.
- **A2A endpoint** — `https://app.worshipmetrics.com/a2a/v1` (JSON-RPC 2.0).
  Agent card: <https://worshipmetrics.com/.well-known/agent-card.json>.
  Discovery-first: it answers simple messages but does not yet execute
  tasks on behalf of callers.
- **API catalog** — <https://worshipmetrics.com/.well-known/api-catalog>
  (RFC 9727 linkset).
- **Knowledge base** — <https://worshipmetrics.com/kb/> (human-readable
  documentation for the whole platform).

## Agent registration

There is no self-serve or API-based agent registration today. WorshipMetrics
does not issue API keys, OAuth clients, or bearer tokens, and does not
publish OAuth authorization server metadata. Please do not probe
`app.worshipmetrics.com` for registration endpoints; this document is the
source of truth.

The RFC 9728 protected resource metadata at
<https://worshipmetrics.com/.well-known/oauth-protected-resource> states the
same thing in machine-readable form: its `authorization_servers` and
`bearer_methods_supported` lists are empty because no authorization server
exists and no bearer tokens are accepted.

### Supported method: human-in-the-loop provisioning

The only credential type is a church member account, and accounts are
provisioned person to person by the WorshipMetrics team:

1. Have your human operator book a call at
   <https://worshipmetrics.com/discovery-call/>, or
2. Email <paul@worshipmetrics.com>, or call 910-WORSHIP (910-967-7447).

An agent working for a church that already uses WorshipMetrics should hand
off to a signed-in person in the web app rather than requesting credentials
of its own.

## Verifying requests from WorshipMetrics

When WorshipMetrics itself sends automated requests to other sites, those
requests are signed per Web Bot Auth (IETF HTTP Message Signatures,
RFC 9421, with `tag="web-bot-auth"`). They carry `Signature-Agent`,
`Signature-Input`, and `Signature` headers, and the Ed25519 public key to
verify them is published at
<https://worshipmetrics.com/.well-known/http-message-signatures-directory>.
A request claiming to be from WorshipMetrics that does not verify against
that key directory is not from us.

## Credential use

- Church data lives behind interactive sign-in at
  <https://app.worshipmetrics.com>, scoped to the signed-in member's church.
- Sign-in credentials are for people. Do not collect, store, or replay a
  member's password on their behalf; ask the person to sign in themselves.
- If token-based agent access ships in the future, it will be documented
  here and in the standard OAuth well-known locations.

---

Canonical URL: <https://worshipmetrics.com/auth.md> ·
Questions: <paul@worshipmetrics.com>
