"""AI tools for the E-Sign module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListSignatureRequests(AssistantTool):
    name = "list_signature_requests"
    description = "List e-signature requests."
    module_id = "esign"
    required_permission = "esign.view_signaturerequest"
    parameters = {
        "type": "object",
        "properties": {"status": {"type": "string", "description": "draft, pending, signed, declined, expired"}, "limit": {"type": "integer"}},
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from esign.models import SignatureRequest
        qs = SignatureRequest.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        limit = args.get('limit', 20)
        return {"requests": [{"id": str(r.id), "title": r.title, "document_name": r.document_name, "signer_name": r.signer_name, "signer_email": r.signer_email, "status": r.status, "sent_at": r.sent_at.isoformat() if r.sent_at else None} for r in qs.order_by('-created_at')[:limit]]}


@register_tool
class CreateSignatureRequest(AssistantTool):
    name = "create_signature_request"
    description = "Create an e-signature request."
    module_id = "esign"
    required_permission = "esign.add_signaturerequest"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "title": {"type": "string"}, "document_name": {"type": "string"},
            "signer_name": {"type": "string"}, "signer_email": {"type": "string"},
            "expires_at": {"type": "string"}, "notes": {"type": "string"},
        },
        "required": ["title", "document_name", "signer_name", "signer_email"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from esign.models import SignatureRequest
        r = SignatureRequest.objects.create(title=args['title'], document_name=args['document_name'], signer_name=args['signer_name'], signer_email=args['signer_email'], expires_at=args.get('expires_at'), notes=args.get('notes', ''))
        return {"id": str(r.id), "title": r.title, "created": True}
