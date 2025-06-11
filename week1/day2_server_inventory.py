import json # Imports the 'json' module, which provides tools for working with JSON data.

# Defines the path to your inventory file.
# The 'r' before the string makes it a "raw string" to correctly handle backslashes in Windows file paths.
file_path = r'G:\project\python-30days\week1\Inventory.json'

# Opens the file specified by 'file_path' in 'r' (read) mode.
# The 'with' statement ensures the file is automatically closed when done, even if errors happen.
with open(file_path, 'r') as file:
    # Reads the JSON data from the opened file and converts it into Python objects (like dictionaries and lists).
    data = json.load(file)

# Accesses the value associated with the 'servers' key from the 'data' dictionary.
# This value is a list of server dictionaries, which is assigned to the 'servers' variable.
servers = data['servers']

# Prints a descriptive header for the inventory list.
print("server inventory list\n")
print("------------------------------------")

# Loops through each individual server dictionary in the 'servers' list.
# In each iteration, 'server' will hold one server's data (e.g., {"name": "web-prod-01", ...}).
for server in servers:
    # Prints the server's name. .get('name') is used for safe access; it returns None if 'name' key is missing.
    print("Server name: ", server.get('name'))
    # Prints the server's IP address using .get() for safe access.
    print("IP: ", server.get('ip'))

    # Checks if the 'is_running' key exists in the current 'server' dictionary.
    # This is a conditional expression (often called a ternary operator):
    # If 'is_running' is present, it prints its value. Otherwise, it prints "Down".
    print("is_running", server.get('is_running') if 'is_running' in server else "Down")

    # Checks if the 'metadata' key exists in the current 'server' dictionary.
    # THIS IS THE CORRECTED COMMENT: Previously, it incorrectly said 'metedata'.
    if 'metadata' in server:
        # If 'metadata' exists, it retrieves its value (which is another dictionary).
        metadata = server['metadata']
        # Prints the 'uptime' from the 'metadata' dictionary. .get() is used for safe access, defaulting to "N/A".
        print("uptime: ", metadata.get('uptime', "N/A"))
        # Prints the 'location' from the 'metadata' dictionary.
        print("location: ", metadata.get('location', "N/A"))
        # Prints the 'OS' from the 'metadata' dictionary. (Note: 'OS' is typically capitalized in your JSON).
        print("OS: ", metadata.get('OS', "N/A"))
        # Prints the 'environment' from the 'metadata' dictionary, if available in your random inventory.
        print("environment: ", metadata.get('environment', "N/A"))
        # Prints a separator line to distinguish between server entries.
        print("------------------------------------")
    else:
        # If the 'metadata' key is not present for the current server.
        print("No metadata present for server")
        # Prints a separator line even if no metadata was found, for consistent output formatting.
        print("------------------------------------")