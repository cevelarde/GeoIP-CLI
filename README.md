# GeoIP-CLI

The GeoIP-CLI is a Python program that allows you to retrieve the latitude and longitude information for a specific IP address using the IPStack API.

## Prerequisites

Before using this program, you will need the following:

- Python 3 installed on your system.
- An API key from IPStack. You can sign up for a free API key on the [IPStack website](https://ipstack.com/). You can keep the default API key or edit the "cli_lat_long.py" file to replace the default API key by your own key.

## Installation

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/cevelarde/GeoIP-CLI.git

## Usage

1. Open a terminal or command prompt on the root project directory.

2. Run the following cmd to build the container as well as run the container:
   - docker build -t cli_geoip --rm .
   - docker run -it --name cli_geoip_container --rm cli_geoip

3. Run the program with the IP address you want to look up:

   python cli_lat_long.py 134.201.250.155

   You can replace the '134.201.250.155' IP address with the IP address you want to query.

4. The program will make an HTTP request to the IPStack API and display the latitude and longitude information for the provided IP address.

5. You can use the program's output as part of other Unix tools or scripts in your data processing pipeline.

## Security

- **Protect Your API Key**: Keep your IPStack API key confidential. Do not expose it in publicly accessible code repositories or share it with unauthorized individuals.
- **Error Handling**: Handle errors gracefully and avoid leaking sensitive information in error messages that could be exploited by malicious actors.

## Example

python3 cli_lat_long.py 134.201.250.155

Output:

34.0475 -118.2922
