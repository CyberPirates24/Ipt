# IPT - IP TRACING TOOL ![Screenshot 2024-08-06 222458](https://github.com/user-attachments/assets/963fc3e0-e9b7-47cc-a51b-354588993a34)

This is a simple Python script to trace the geographical location and other details of an IP address using the `ip-api.com` service. The tool fetches and displays information such as city, region, country, latitude, longitude, ISP, and organization associated with the provided IP address.

## Features

- Fetches IP address information including:
  - City
  - Region
  - Country
  - Latitude and Longitude
  - ISP
  - Organization
  - Timezone
- Uses the free `ip-api.com` service without the need for an API key.

## Requirements

- Python 3.x
- `requests` library
- `colorama` pkg

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/CyberPirates24/Ipt.git
    cd Ipt
    ```

2. **Install the Requirements**

    ```sh
    pip install requests
    pip install colorama
    ```

## Usage

1. **Run the script:**

    ```sh
    python ipt.py
    ```

2. **Enter the IP address:**

    When prompted, enter the IP address you want to trace.

## Example

```sh
$ python ip_tracing_tool.py
Enter the IP address: 8.8.8.8
IP Address: 8.8.8.8
City: Mountain View
Region: California
Country: United States
Location: 37.386, -122.084
ISP: Google LLC
Organization: Google LLC
Timezone: America/Los_Angeles
