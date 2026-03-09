# E-Signatures

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `esign` |
| **Version** | `1.0.0` |
| **Icon** | `create-outline` |
| **Dependencies** | None |

## Models

### `SignatureRequest`

SignatureRequest(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, title, document_name, status, signer_name, signer_email, sent_at, signed_at, expires_at, notes)

| Field | Type | Details |
|-------|------|---------|
| `title` | CharField | max_length=255 |
| `document_name` | CharField | max_length=255 |
| `status` | CharField | max_length=20, choices: draft, pending, signed, declined, expired |
| `signer_name` | CharField | max_length=255 |
| `signer_email` | EmailField | max_length=254 |
| `sent_at` | DateTimeField | optional |
| `signed_at` | DateTimeField | optional |
| `expires_at` | DateField | optional |
| `notes` | TextField | optional |

## URL Endpoints

Base path: `/m/esign/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `documents/` | `documents` | GET |
| `signature_requests/` | `signature_requests_list` | GET |
| `signature_requests/add/` | `signature_request_add` | GET/POST |
| `signature_requests/<uuid:pk>/edit/` | `signature_request_edit` | GET |
| `signature_requests/<uuid:pk>/delete/` | `signature_request_delete` | GET/POST |
| `signature_requests/bulk/` | `signature_requests_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `esign.view_signaturerequest` | View Signaturerequest |
| `esign.add_signaturerequest` | Add Signaturerequest |
| `esign.change_signaturerequest` | Change Signaturerequest |
| `esign.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_signaturerequest`, `change_signaturerequest`, `view_signaturerequest`
- **employee**: `add_signaturerequest`, `view_signaturerequest`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Documents | `create-outline` | `documents` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_signature_requests`

List e-signature requests.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | draft, pending, signed, declined, expired |
| `limit` | integer | No |  |

### `create_signature_request`

Create an e-signature request.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes |  |
| `document_name` | string | Yes |  |
| `signer_name` | string | Yes |  |
| `signer_email` | string | Yes |  |
| `expires_at` | string | No |  |
| `notes` | string | No |  |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  esign/
    css/
    js/
  icons/
    icon.svg
templates/
  esign/
    pages/
      dashboard.html
      documents.html
      index.html
      settings.html
      signature_request_add.html
      signature_request_edit.html
      signature_requests.html
    partials/
      dashboard_content.html
      documents_content.html
      panel_signature_request_add.html
      panel_signature_request_edit.html
      settings_content.html
      signature_request_add_content.html
      signature_request_edit_content.html
      signature_requests_content.html
      signature_requests_list.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
