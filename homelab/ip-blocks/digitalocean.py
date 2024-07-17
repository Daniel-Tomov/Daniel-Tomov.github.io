digitalocean_file = open("homelab/ip-blocks/cloud-ip-ranges/digitalocean.csv", "r").read()
digitalocean_output_file = open("homelab/ip-blocks/digitalocean.txt", "w")

for line in digitalocean_file.split("\n"):
    #print(line.split(",")[0])
    digitalocean_output_file.write(f'{line.split(",")[0]}\n')
digitalocean_output_file.close()