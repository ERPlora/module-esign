"""
E-Signatures Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import SignatureRequest

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('esign', 'dashboard')
@htmx_view('esign/pages/index.html', 'esign/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_signature_requests': SignatureRequest.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# SignatureRequest
# ======================================================================

SIGNATURE_REQUEST_SORT_FIELDS = {
    'title': 'title',
    'status': 'status',
    'document_name': 'document_name',
    'signer_name': 'signer_name',
    'signer_email': 'signer_email',
    'sent_at': 'sent_at',
    'created_at': 'created_at',
}

def _build_signature_requests_context(hub_id, per_page=10):
    qs = SignatureRequest.objects.filter(hub_id=hub_id, is_deleted=False).order_by('title')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'signature_requests': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'title',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_signature_requests_list(request, hub_id, per_page=10):
    ctx = _build_signature_requests_context(hub_id, per_page)
    return django_render(request, 'esign/partials/signature_requests_list.html', ctx)

@login_required
@with_module_nav('esign', 'documents')
@htmx_view('esign/pages/signature_requests.html', 'esign/partials/signature_requests_content.html')
def signature_requests_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'title')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = SignatureRequest.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(title__icontains=search_query) | Q(document_name__icontains=search_query) | Q(status__icontains=search_query) | Q(signer_name__icontains=search_query))

    order_by = SIGNATURE_REQUEST_SORT_FIELDS.get(sort_field, 'title')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['title', 'status', 'document_name', 'signer_name', 'signer_email', 'sent_at']
        headers = ['Title', 'Status', 'Document Name', 'Signer Name', 'Signer Email', 'Sent At']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='signature_requests.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='signature_requests.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'esign/partials/signature_requests_list.html', {
            'signature_requests': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'signature_requests': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
@htmx_view('esign/pages/signature_request_add.html', 'esign/partials/signature_request_add_content.html')
def signature_request_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        document_name = request.POST.get('document_name', '').strip()
        status = request.POST.get('status', '').strip()
        signer_name = request.POST.get('signer_name', '').strip()
        signer_email = request.POST.get('signer_email', '').strip()
        sent_at = request.POST.get('sent_at') or None
        signed_at = request.POST.get('signed_at') or None
        expires_at = request.POST.get('expires_at') or None
        notes = request.POST.get('notes', '').strip()
        obj = SignatureRequest(hub_id=hub_id)
        obj.title = title
        obj.document_name = document_name
        obj.status = status
        obj.signer_name = signer_name
        obj.signer_email = signer_email
        obj.sent_at = sent_at
        obj.signed_at = signed_at
        obj.expires_at = expires_at
        obj.notes = notes
        obj.save()
        response = HttpResponse(status=204)
        response['HX-Redirect'] = reverse('esign:signature_requests_list')
        return response
    return {}

@login_required
@htmx_view('esign/pages/signature_request_edit.html', 'esign/partials/signature_request_edit_content.html')
def signature_request_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(SignatureRequest, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '').strip()
        obj.document_name = request.POST.get('document_name', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.signer_name = request.POST.get('signer_name', '').strip()
        obj.signer_email = request.POST.get('signer_email', '').strip()
        obj.sent_at = request.POST.get('sent_at') or None
        obj.signed_at = request.POST.get('signed_at') or None
        obj.expires_at = request.POST.get('expires_at') or None
        obj.notes = request.POST.get('notes', '').strip()
        obj.save()
        return _render_signature_requests_list(request, hub_id)
    return {'obj': obj}

@login_required
@require_POST
def signature_request_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(SignatureRequest, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_signature_requests_list(request, hub_id)

@login_required
@require_POST
def signature_requests_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = SignatureRequest.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_signature_requests_list(request, hub_id)


@login_required
@permission_required('esign.manage_settings')
@with_module_nav('esign', 'settings')
@htmx_view('esign/pages/settings.html', 'esign/partials/settings_content.html')
def settings_view(request):
    return {}

