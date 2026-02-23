from django.utils.translation import gettext_lazy as _

MODULE_ID = 'esign'
MODULE_NAME = _('E-Signatures')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'create-outline'
MODULE_DESCRIPTION = _('Electronic signature workflows and document signing')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'documents'

MENU = {
    'label': _('E-Signatures'),
    'icon': 'create-outline',
    'order': 70,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Documents'), 'icon': 'create-outline', 'id': 'documents'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'esign.view_signaturerequest',
'esign.add_signaturerequest',
'esign.change_signaturerequest',
'esign.manage_settings',
]
