# 2) IAM and Networking

This section covers minimal IAM policies and how to create a simple VCN and subnet for a publicly accessible Container Instance.

> Note: In many orgs, networking and policy may be centrally managed. If you already have a public subnet, skip to the OCIR and deployment steps later.

## Minimal IAM policies

If you are an administrator in the tenancy, you may already have the permissions. If not, create policies in the root compartment (or ask an admin) to allow your group to manage necessary resources in your target compartment.

Example policy statements (replace names and OCIDs accordingly):

- In the root compartment (or a common policies compartment), create a policy targeting your user group, e.g., `DevOpsGroup`:

```
Allow group DevOpsGroup to use repos in compartment <YourCompartmentName>
Allow group DevOpsGroup to manage repos in compartment <YourCompartmentName>
Allow group DevOpsGroup to manage container-instances in compartment <YourCompartmentName>
Allow group DevOpsGroup to manage virtual-network-family in compartment <YourCompartmentName>
```

Explanation:
- `virtual-network-family` permits VCN/subnet/security list creation.
- `container-instances` permits CI creation and management.
- `repos` covers OCIR repositories.

If you want stricter policies, scope them to `use` or `read` vs `manage` and to specific resources, but the above is simplest for a demo.

## Create a VCN with a public subnet

You can use the Console VCN Wizard or CLI. The wizard is easiest.

### Console (recommended for first-time)

1) Console → Networking → Virtual Cloud Networks → Start VCN Wizard → VCN with Internet Connectivity.
2) Choose compartment, name, CIDR (e.g., 10.0.0.0/16), create.
3) The wizard creates:
   - VCN
   - Internet Gateway
   - Route Table with default route to IGW
   - Security List
   - Public subnet

Note the following outputs:
- VCN OCID
- Subnet OCID (public subnet)

### Security list rule for port 8080

For simplicity, allow inbound TCP 8080 from anywhere:

1) Networking → Virtual Cloud Networks → your VCN → Security Lists → select the list tied to your public subnet.
2) Add Ingress Rule:
   - Source CIDR: `0.0.0.0/0`
   - IP Protocol: TCP
   - Destination Port Range: `8080`

> For production, restrict the source CIDR or use an NSG with tighter rules.

### Availability Domain

Container Instances run in an availability domain (AD). Find your AD name from the Console:

- Console → Governance & Administration → Tenancy Details → Regions → select active region → note AD names (e.g., `kIdk:US-ASHBURN-AD-1`).

You will need one AD name when creating the container instance.


