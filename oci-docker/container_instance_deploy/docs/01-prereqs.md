# 1) Prerequisites

This project deploys a minimal Flask app to an OCI Container Instance. You will need:

- An OCI account with rights to create network resources, OCIR repositories, and Container Instances in your target compartment.
- Windows 10/11 with PowerShell.
- Docker Desktop installed and running (`docker version` works).
- OCI CLI installed and configured.

## Install and configure OCI CLI (Windows)

1) Open PowerShell as your user (not necessarily Administrator).

2) Allow scripts for your user:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3) Download and run the installer:

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1 -OutFile install.ps1
.\install.ps1 -InstallDir $HOME\bin\oci-cli
```

Restart your terminal and verify:

```powershell
oci --version
```

## Create API keys and configure profile

Generate keys (OpenSSL is bundled with Git for Windows or use any OpenSSL installation):

```powershell
mkdir $HOME\.oci -ErrorAction Ignore
openssl genrsa -out $HOME\.oci\oci_api_key.pem 2048
openssl rsa -pubout -in $HOME\.oci\oci_api_key.pem -out $HOME\.oci\oci_api_key_public.pem
```

Upload the public key to your OCI user:

- Console → Profile menu (top-right) → User Settings → API Keys → Add API Key → Paste the content of `oci_api_key_public.pem`.
- Note the fingerprint that OCI returns.

Create the CLI config:

```powershell
oci setup config
```

When prompted, provide:

- Tenancy OCID
- User OCID
- Region (e.g., `eu-frankfurt-1`, `us-ashburn-1`)
- Fingerprint from the API key upload
- Private key path: `C:\Users\<you>\.oci\oci_api_key.pem`

Test:

```powershell
oci iam region list
```

If this returns JSON, your CLI auth is working.

## Collect required identifiers

Have these values ready (you can find them in the Console):

- Tenancy OCID
- Compartment OCID (target compartment for container instance and repo)
- Region (full name and short code, e.g., `us-ashburn-1` → `iad`)
- Object Storage Namespace (used for OCIR username prefix)

Find the Object Storage Namespace:

- Console → Tenancy Details → Object Storage Namespace (this is also your OCIR namespace).


