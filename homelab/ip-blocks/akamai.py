akamai_v4_input = open("homelab/ip-blocks/cloud-ip-ranges/akamai-v4-ip-ranges.txt").read()
akamai_v6_input = open("homelab/ip-blocks/cloud-ip-ranges/akamai-v6-ip-ranges.txt").read()
akamai_output = open("homelab/ip-blocks/akamai.txt", "w")

akamai_output.write(akamai_v4_input.replace("\t", "").replace(" ", ""))
akamai_output.write("\n")
akamai_output.write(akamai_v6_input.replace("\t", "").replace(" ", ""))
akamai_output.write("\n")
akamai_output.close()