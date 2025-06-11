import json

file_path= r'G:\project\python-30days\week1\Inventory.json'

with open (file_path,'r') as file:
    data=json.load(file)

servers=data['servers']


raw_input_from_user=input("please provide server name (comma sperated) : ").split(',')
search_name= (name.strip() for name in raw_input_from_user if name.strip())

print("\n *************************server inventory lookup************************* \n")
print("-------------------------------\n")


for requested_name in search_name:
    found_server = None
    
    for server in servers:
        if server.get('name') == requested_name:
            found_server=server
            break
    if found_server:
        print("Server detail for: ", found_server.get('name'))

        print("Name : ", found_server.get('name'))
        print("IP : ", found_server.get('ip'))
        print("is_running : ", found_server.get('is_running') if 'is_running' in found_server else "Down" )
        if 'metadata' in server:
            metadata=server['metadata']
            # Prints the 'uptime' from the 'metadata' dictionary. .get() is used for safe access, defaulting to "N/A".
            print("uptime: ", metadata.get('uptime') if 'uptime' in metadata else "N/A")
        # Prints the 'location' from the 'metadata' dictionary.
            print("location: ", metadata.get('location') if 'location' in metadata else "N/A")
        # Prints the 'OS' from the 'metadata' dictionary. (Note: 'OS' is typically capitalized in your JSON).
            print("OS: ", metadata.get('OS') if 'OS' in metadata else "N/A")
        # Prints the 'environment' from the 'metadata' dictionary, if available in your random inventory.
            print("environment: ", metadata.get('environment') if 'environment' in metadata else "N/A")
        # Prints a separator line to distinguish between server entries.
            print("------------------------------------")
        else:
            print("Metadata not found for server: ", found_server.get('name'))
            print("------------------------------------")

    else:
        print(f"Server '{requested_name}' not found in inventory.")
        print("----------------------\n")
