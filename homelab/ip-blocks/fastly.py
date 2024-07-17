import json

fastly_file = open("homelab/ip-blocks/cloud-ip-ranges/fastly-ip-ranges.json", "r").read()
fastly_output_file = open("homelab/ip-blocks/fastly.txt", "w")


fastly_json = json.loads(fastly_file)

for ipv4 in fastly_json["addresses"]:
    #print(ipv4)
    fastly_output_file.write(f'{ipv4}\n')
for ipv6 in fastly_json["ipv6_addresses"]:
    #print(ipv6)
    fastly_output_file.write(f'{ipv6}\n')
fastly_output_file.close()