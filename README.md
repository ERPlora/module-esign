# E-Signatures Module

Electronic signature workflows and document signing.

## Features

- Create and manage signature requests for documents
- Track signature status through a complete lifecycle (draft, pending, signed, declined, expired)
- Record signer details including name and email
- Set expiration dates on signature requests
- Dashboard with overview of all signature activity

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > E-Signatures > Settings**

## Usage

Access via: **Menu > E-Signatures**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/esign/dashboard/` | Overview of signature request activity and status |
| Documents | `/m/esign/documents/` | List and manage all signature requests |
| Settings | `/m/esign/settings/` | Configure e-signature module settings |

## Models

| Model | Description |
|-------|-------------|
| `SignatureRequest` | A document signing request with title, signer details, status tracking, and expiration |

## Permissions

| Permission | Description |
|------------|-------------|
| `esign.view_signaturerequest` | View signature requests |
| `esign.add_signaturerequest` | Create new signature requests |
| `esign.change_signaturerequest` | Edit existing signature requests |
| `esign.manage_settings` | Manage e-signature module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
