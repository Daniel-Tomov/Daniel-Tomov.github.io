import json

azure_file = open("homelab/ip-blocks/cloud-ip-ranges/microsoft-azure-ip-ranges.json", "r").read()
azure_output_file = open("homelab/ip-blocks/azure.txt", "w")


azure_json = json.loads(azure_file)
for prefix in azure_json["values"]:
    for ip in prefix["properties"]["addressPrefixes"]:
        #print(ip)
        azure_output_file.write(f'{ip}\n')
azure_output_file.close()