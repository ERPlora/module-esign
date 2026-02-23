from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

SIGN_STATUS = [
    ('draft', _('Draft')),
    ('pending', _('Pending')),
    ('signed', _('Signed')),
    ('declined', _('Declined')),
    ('expired', _('Expired')),
]

class SignatureRequest(HubBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    document_name = models.CharField(max_length=255, verbose_name=_('Document Name'))
    status = models.CharField(max_length=20, default='pending', choices=SIGN_STATUS, verbose_name=_('Status'))
    signer_name = models.CharField(max_length=255, verbose_name=_('Signer Name'))
    signer_email = models.EmailField(verbose_name=_('Signer Email'))
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Sent At'))
    signed_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Signed At'))
    expires_at = models.DateField(null=True, blank=True, verbose_name=_('Expires At'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'esign_signaturerequest'

    def __str__(self):
        return self.title

