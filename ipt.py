import requests
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

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
        print(f"{Fore.YELLOW}IP Address: {ip_info.get('query')}")
        print(f"{Fore.YELLOW}City: {ip_info.get('city')}")
        print(f"{Fore.YELLOW}Region: {ip_info.get('regionName')}")
        print(f"{Fore.YELLOW}Country: {ip_info.get('country')}")
        print(f"{Fore.YELLOW}Location: {ip_info.get('lat')}, {ip_info.get('lon')}")
        print(f"{Fore.YELLOW}ISP: {ip_info.get('isp')}")
        print(f"{Fore.YELLOW}Organization: {ip_info.get('org')}")
        print(f"{Fore.YELLOW}Timezone: {ip_info.get('timezone')}")
    else:
        print(f"{Fore.RED}Could not retrieve information for the given IP address.")

# Main function
def main():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display banner
    banner = """
    ██╗██████╗ ████████╗
    ██║██╔══██╗╚══██╔══╝
    ██║██████╔╝   ██║   
    ██║██╔═══╝    ██║   
    ██║██║        ██║   
    ╚═╝╚═╝        ╚═╝   
                        """
    print(Fore.GREEN + banner)
    
    # Display additional information
    print(f"{Fore.GREEN}Coded by: Ahraf Uzzaman")
    print(f"{Fore.GREEN}Author: Cyber Pirates")
    print(f"{Fore.GREEN}Github: https://github.com/CyberPirates24")
    print("\n")

    ip_address = input("Enter the IP address: ")
    ip_info = get_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
