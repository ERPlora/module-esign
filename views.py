"""
E-Signatures Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('esign', 'dashboard')
@htmx_view('esign/pages/dashboard.html', 'esign/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('esign', 'documents')
@htmx_view('esign/pages/documents.html', 'esign/partials/documents_content.html')
def documents(request):
    """Documents view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('esign', 'settings')
@htmx_view('esign/pages/settings.html', 'esign/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

