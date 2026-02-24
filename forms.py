from django import forms
from django.utils.translation import gettext_lazy as _

from .models import SignatureRequest

class SignatureRequestForm(forms.ModelForm):
    class Meta:
        model = SignatureRequest
        fields = ['title', 'document_name', 'status', 'signer_name', 'signer_email', 'sent_at', 'signed_at', 'expires_at', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'document_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'signer_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'signer_email': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'email'}),
            'sent_at': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'datetime-local'}),
            'signed_at': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'datetime-local'}),
            'expires_at': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

