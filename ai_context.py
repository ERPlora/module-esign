"""
AI context for the eSign module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: eSign

### Models

**SignatureRequest** — a document sent to one person for electronic signature.
- `title` (str): name of the signature request (e.g. "Service Agreement - John Doe")
- `document_name` (str): original document filename or label
- `status` (choice): draft, pending, signed, declined, expired (default: pending)
- `signer_name` (str): full name of the expected signer
- `signer_email` (email): where the signing invitation is sent
- `sent_at` (datetime, nullable): when the request was dispatched
- `signed_at` (datetime, nullable): when the document was signed
- `expires_at` (date, nullable): deadline for signing; after this date, status should become expired
- `notes` (text): internal notes or context

### Key flows

1. **Create a request**: provide title, document_name, signer_name, signer_email. Status starts as "draft" or "pending".
2. **Send for signing**: set status="pending", sent_at=now.
3. **Record signature**: set status="signed", signed_at=now.
4. **Decline**: set status="declined".
5. **Expire**: set status="expired" when today > expires_at and status is still "pending".
6. **Filter pending**: query by status="pending" to see outstanding requests.

### Notes
- SignatureRequest is per-signer — one document requiring multiple signers needs one request per signer.
- No FK to documents or customers — all references are name/email strings to keep the module self-contained.
"""
