import json

oracle_file = open("homelab/ip-blocks/cloud-ip-ranges/oracle-cloud-ip-ranges.json", "r").read()
oracle_output_file = open("homelab/ip-blocks/oracle.txt", "w")


oracle_json = json.loads(oracle_file)

for region in oracle_json["regions"]:
    for cidr in region["cidrs"]:
        #print(cidr["cidr"])
        oracle_output_file.write(f'{cidr["cidr"]}\n')
oracle_output_file.close()