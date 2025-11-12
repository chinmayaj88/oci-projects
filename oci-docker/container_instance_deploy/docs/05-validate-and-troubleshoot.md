# 5) Validate and Troubleshoot

This section helps you verify the deployment and diagnose common issues.

## Quick validation checklist

- OCIR image exists and is accessible (public or CI has permissions)
- Container Instance status is RUNNING
- Subnet is public with route to Internet Gateway
- Security list/NSG allows inbound TCP 8080
- Public IP is reachable from your network

## Inspect Container Instance and logs

Show instance details:

```powershell
oci container-instances container-instance get --container-instance-id <ci_ocid>
```

List containers in the CI and check their status:

```powershell
oci container-instances container list --container-instance-id <ci_ocid>
```

Fetch container logs (stdout/stderr):

```powershell
oci container-instances container logs get --container-id <container_ocid>
```

Tip: if not sure of the `container_ocid`, list containers as shown above.

## Common issues

1) Image pull errors
   - Private repo and no pull auth: Make repo public for demo, or attach a secret to CI (Auth Token) or allow dynamic group policy + repository access. For demos, public repo is easiest.
   - Wrong image URL format: Must be `<region>.ocir.io/<namespace>/<repo>:<tag>`.

2) Cannot reach app
   - Security list/NSG missing ingress rule for TCP 8080.
   - Subnet is private or missing route to Internet Gateway.
   - Corporate firewall blocks outbound 8080; try 80 or 443 by adjusting app/ports.

3) App crashes immediately
   - Check logs for missing environment variables, binding to wrong port, or Python dependency errors.
   - Our Dockerfile runs `gunicorn` binding to `0.0.0.0:8080`. Ensure any custom changes keep `PORT=8080` or update both Dockerfile and CI port mappings accordingly.

4) Policy denied
   - Ensure your group has permissions: `manage container-instances`, `manage repos`, and relevant VCN privileges in the target compartment.

## Verifying OCIR and auth

List repositories:

```powershell
oci artifacts container repository list --compartment-id <compartment_ocid>
```

Check auth tokens for your user (Console → User Settings → Auth Tokens). If your Docker login fails, regenerate a new token and use that as the password.


