import json

gcp_file = open("homelab/ip-blocks/cloud-ip-ranges/google-cloud-ip-ranges.json", "r").read()
gcp_output_file = open("homelab/ip-blocks/gcp.txt", "w")

gcp_json = json.loads(gcp_file)

for prefix in gcp_json["prefixes"]:
    if "ipv4Prefix" in prefix:
        #print(f'{prefix["ipv4Prefix"]}')
        gcp_output_file.write(f'{prefix["ipv4Prefix"]}\n')
    elif "ipv6Prefix" in prefix:
        #print(f'{prefix["ipv6Prefix"]}')
        gcp_output_file.write(f'{prefix["ipv6Prefix"]}\n')
gcp_output_file.close()