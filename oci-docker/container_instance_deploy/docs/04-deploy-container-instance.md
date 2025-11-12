# 4) Deploy Container Instance

This section shows how to launch an OCI Container Instance with your image. You will need:

- Compartment OCID where the instance will live
- Public Subnet OCID (with route to IGW)
- Availability Domain name (e.g., `kIdk:US-ASHBURN-AD-1`)
- Image URL from OCIR, e.g., `<region>.ocir.io/<namespace>/hello-flask:1`

Ensure your subnet's security list (or NSG) allows inbound TCP 8080 from your source IP(s).

## Create the Container Instance (CLI)

```powershell
$compartmentId = "<compartment_ocid>"
$subnetId      = "<subnet_ocid>"
$ad            = "<availability_domain_name>"   # e.g., kIdk:US-ASHBURN-AD-1
$imageUrl      = "<region>.ocir.io/<namespace>/hello-flask:1"

oci container-instances container-instance create `
  --availability-domain $ad `
  --compartment-id $compartmentId `
  --display-name "hello-flask-ci" `
  --shape "CI.Standard.E4.Flex" `
  --shape-config '{
    "ocpus": 1,
    "memoryInGBs": 2
  }' `
  --vnics "[{
    ""subnetId"": ""$subnetId"",
    ""assignPublicIp"": true
  }]" `
  --containers "[{
    ""displayName"": ""hello"",
    ""imageUrl"": ""$imageUrl"",
    ""command"": [],
    ""arguments"": [],
    ""environmentVariables"": { ""PORT"": ""8080"" },
    ""volumeMounts"": [],
    ""workingDirectory"": """",
    ""isResourcePrincipalDisabled"": false,
    ""ports"": [{ ""containerPort"": 8080, ""protocol"": ""TCP"" }]
  }]"
```

The output includes the Container Instance OCID. If you missed it, list instances:

```powershell
oci container-instances container-instance list --compartment-id $compartmentId
```

## Retrieve public IP

```powershell
$ciId = "<container_instance_ocid>"
oci container-instances container-instance get --container-instance-id $ciId
```

In the JSON, look for `vnics[0].publicIp`. That is the external IP.

## Test the application

From your workstation:

```powershell
curl http://<public_ip>:8080/
```

You should receive JSON similar to:

```json
{ "message": "Hello from Flask on OCI Container Instance!", "version": "1.0.0" }
```


