import docker


client = docker.from_env()

images = client.images.list()
print(f'local images: { images }')

client.images.pull('python', tag='3.9.13')

launching_containers = client.containers.list()
print(f'launching_containers: { launching_containers }')

all_containers = client.containers.list(all=True)
print(f'all_containers: { all_containers}')









