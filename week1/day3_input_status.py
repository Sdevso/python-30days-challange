import json

# Define the file path (using a raw string for Windows paths)
file_path = r'G:\project\python-30days\week1\Inventory.json'

try:
    # Open and load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)
    servers = data['servers'] # Get the list of server dictionaries


    # --- KEY CHANGE: Handling multiple inputs ---
    # Get user input, split by comma, and strip whitespace from each name
    raw_input_names = input("Enter server name(s) to look up (comma separated): ").split(',')
    # Create a clean list of names, removing any empty strings that might result from extra commas
    search_names = [name.strip() for name in raw_input_names if name.strip()]
    # --- END KEY CHANGE ---

    print("\n--- Server Inventory Lookup Results ---")
    print("=======================================\n")

    # Loop through each server name the user requested
    for requested_name in search_names:
        found_server_details = None # Variable to hold server details if found for the current requested_name

        # Loop through your entire server inventory to find a match for the current requested_name
        for server_info in servers:
            if server_info.get('name') == requested_name:
                found_server_details = server_info # Store the found server's dictionary
                break # Stop searching, we found it!

        # Now, check if the server was found and print results
        if found_server_details:
            print(f"--- Details for: {found_server_details['name']} ---")

            # Basic details
            print(f"Name:    {found_server_details.get('name', 'N/A')}")
            print(f"IP:      {found_server_details.get('ip', 'N/A')}")

            # More descriptive status for is_running
            status = "Running" if found_server_details.get('is_running', False) else "Stopped"
            print(f"Status:  {status}")

            # Optionally add services if present (simplified)
            if 'services' in found_server_details and found_server_details['services']:
                print(f"Services: {', '.join(found_server_details['services'])}")

            print("----------------------")
        else:
            print(f"Server '{requested_name}' not found in inventory.")
            print("----------------------") # Add a separator for not-found messages too

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error: Could not read JSON from '{file_path}': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")