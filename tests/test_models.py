"""Tests for esign models."""
import pytest
from django.utils import timezone

from esign.models import SignatureRequest


@pytest.mark.django_db
class TestSignatureRequest:
    """SignatureRequest model tests."""

    def test_create(self, signature_request):
        """Test SignatureRequest creation."""
        assert signature_request.pk is not None
        assert signature_request.is_deleted is False

    def test_str(self, signature_request):
        """Test string representation."""
        assert str(signature_request) is not None
        assert len(str(signature_request)) > 0

    def test_soft_delete(self, signature_request):
        """Test soft delete."""
        pk = signature_request.pk
        signature_request.is_deleted = True
        signature_request.deleted_at = timezone.now()
        signature_request.save()
        assert not SignatureRequest.objects.filter(pk=pk).exists()
        assert SignatureRequest.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, signature_request):
        """Test default queryset excludes deleted."""
        signature_request.is_deleted = True
        signature_request.deleted_at = timezone.now()
        signature_request.save()
        assert SignatureRequest.objects.filter(hub_id=hub_id).count() == 0


