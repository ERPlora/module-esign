from django.contrib import admin

from .models import SignatureRequest

@admin.register(SignatureRequest)
class SignatureRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_name', 'status', 'signer_name', 'signer_email']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

