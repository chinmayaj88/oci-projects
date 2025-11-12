# 3) OCIR Registry and Docker Image

This section covers creating an OCIR repository, logging in with Docker, building the image, and pushing it to OCIR.

## Create OCIR repository

You can use Console or CLI. For a simple public repo (good for demos):

```powershell
$compartmentId = "<compartment_ocid>"
oci artifacts container repository create `
  --compartment-id $compartmentId `
  --display-name "hello-flask" `
  --is-public true
```

Notes:
- If the repository already exists, this will error; you can ignore and continue.
- Public makes testing easier. For private, set `--is-public false` and ensure your Container Instance has permissions to pull.

## Docker login to OCIR

You need your Object Storage Namespace (`<ns>`) and region short code (e.g., `iad`, `fra`, `bom`). Your Docker username is `<ns>/<your-oci-username>`. Password is an OCI Auth Token (User Settings → Auth Tokens → Generate Token).

```powershell
docker login <region>.ocir.io
# Username: <ns>/<your-oci-username>
# Password: <an OCI Auth Token value>
```

## Build and tag the image

From your project root (contains `Dockerfile`):

```powershell
docker build -t hello-flask:1 .
```

Test locally (optional):

```powershell
docker run --rm -p 8080:8080 hello-flask:1
# Open http://localhost:8080
# Press Ctrl+C to stop
```

Tag for OCIR:

```powershell
$region = "<region>"   # e.g. iad
$ns = "<namespace>"    # Object Storage Namespace
docker tag hello-flask:1 "$region.ocir.io/$ns/hello-flask:1"
```

## Push to OCIR

```powershell
docker push "$region.ocir.io/$ns/hello-flask:1"
```

After pushing, note your image URL:

```
<region>.ocir.io/<namespace>/hello-flask:1
```


