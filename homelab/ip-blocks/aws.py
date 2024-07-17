import json

aws_file = open("homelab/ip-blocks/cloud-ip-ranges/aws-ip-ranges.json", "r").read()
aws_output_file = open("homelab/ip-blocks/aws.txt", "w")


aws_json = json.loads(aws_file)

for prefix in aws_json["prefixes"]:
    #print(prefix["ip_prefix"])
    aws_output_file.write(f'{prefix["ip_prefix"]}\n')
aws_output_file.close()