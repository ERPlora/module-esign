"""Tests for esign views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('esign:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('esign:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('esign:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSignatureRequestViews:
    """SignatureRequest view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('esign:signature_requests_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('esign:signature_requests_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('esign:signature_requests_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('esign:signature_requests_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('esign:signature_requests_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('esign:signature_requests_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('esign:signature_request_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('esign:signature_request_add')
        data = {
            'title': 'New Title',
            'document_name': 'New Document Name',
            'status': 'New Status',
            'signer_name': 'New Signer Name',
            'signer_email': 'test@example.com',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, signature_request):
        """Test edit form loads."""
        url = reverse('esign:signature_request_edit', args=[signature_request.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, signature_request):
        """Test editing via POST."""
        url = reverse('esign:signature_request_edit', args=[signature_request.pk])
        data = {
            'title': 'Updated Title',
            'document_name': 'Updated Document Name',
            'status': 'Updated Status',
            'signer_name': 'Updated Signer Name',
            'signer_email': 'test@example.com',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, signature_request):
        """Test soft delete via POST."""
        url = reverse('esign:signature_request_delete', args=[signature_request.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        signature_request.refresh_from_db()
        assert signature_request.is_deleted is True

    def test_bulk_delete(self, auth_client, signature_request):
        """Test bulk delete."""
        url = reverse('esign:signature_requests_bulk_action')
        response = auth_client.post(url, {'ids': str(signature_request.pk), 'action': 'delete'})
        assert response.status_code == 200
        signature_request.refresh_from_db()
        assert signature_request.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('esign:signature_requests_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('esign:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('esign:settings')
        response = client.get(url)
        assert response.status_code == 302

