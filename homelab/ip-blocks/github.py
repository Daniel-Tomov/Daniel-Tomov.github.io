import json

github_file = open("homelab/ip-blocks/cloud-ip-ranges/github-ip-ranges.json", "r").read()
github_output_file = open("homelab/ip-blocks/github.txt", "w")


github_json = json.loads(github_file)

for key in github_json:
    if key not in ['verifiable_password_authentication', 'ssh_key_fingerprints', 'ssh_keys', 'domains']:
        for ip in github_json[key]:
            #print(ip)
            github_output_file.write(f'{ip}\n')
github_output_file.close()