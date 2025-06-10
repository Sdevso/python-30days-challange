import json
with open('G:\\project\\python-30days\\week1\\Inventory.json', 'r') as file:
    data = json.load(file)

servers = data['servers']

print("""--- Server Inventory --- \n
This script will display the details of each server in the inventory.\n""")
for server in servers:
    print("server_name:", server['name'])
    print("ip_address:", server['ip'])
    print("is_running:", server['is_running'] if 'is_running' in server else "Down")

    if 'metadata' in server:
        metadata = server['metadata']
        print("uptime:",metadata.get('uptime') if 'uptime' in metadata else "N/A")
        print("location:", metadata.get('location') if 'location' in metadata else "N/A")
        print("os:", metadata.get('OS') if 'OS' in metadata else "N/A")
        print("----------------------")
    else:
        print("metadata: N/A")
        print("----------------------")