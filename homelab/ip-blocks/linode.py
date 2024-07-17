linode_file = open("homelab/ip-blocks/cloud-ip-ranges/linode.txt", "r").read()
linode_output_file = open("homelab/ip-blocks/linode.txt", "w")

for line in linode_file.split("\n"):
    #print(line.split(",")[0])
    linode_output_file.write(f'{line.split(",")[0]}\n')
linode_output_file.close()