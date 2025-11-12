# 6) Cleanup

If this was a demo, remember to clean up resources to avoid charges.

## Delete the Container Instance

```powershell
oci container-instances container-instance delete --container-instance-id <ci_ocid> --force
```

Optionally, delete any attached logs or related artifacts.

## Delete the OCIR repository (optional)

If created only for this demo and not used elsewhere:

```powershell
oci artifacts container repository delete --repository-id <repo_ocid> --force
```

Or, via Console: Developer Services → Container Registry → Repositories → select repo → Delete.

## Remove networking (if created just for this demo)

Delete in reverse order of dependencies:

1) Remove security list rules (or delete security lists not in use)
2) Delete public subnet
3) Delete route rules and internet gateway
4) Delete the VCN

Use Console → Networking, or CLI (`oci network ...`). Be careful not to remove shared or production networks.

## Local cleanup

- Remove local Docker image:

```powershell
docker rmi hello-flask:1
```

- Remove config or tokens you created if no longer needed (OCI auth token, API key). Consider rotating or revoking tokens if this was a trial.


