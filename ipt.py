import requests

# Function to get IP information
def get_ip_info(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to display IP information
def display_ip_info(ip_info):
    if ip_info and ip_info['status'] == 'success':
        print(f"IP Address: {ip_info.get('query')}")
        print(f"City: {ip_info.get('city')}")
        print(f"Region: {ip_info.get('regionName')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Location: {ip_info.get('lat')}, {ip_info.get('lon')}")
        print(f"ISP: {ip_info.get('isp')}")
        print(f"Organization: {ip_info.get('org')}")
        print(f"Timezone: {ip_info.get('timezone')}")
    else:
        print("Could not retrieve information for the given IP address.")

# Main function
def main():
    ip_address = input("Enter the IP address: ")
    ip_info = get_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
