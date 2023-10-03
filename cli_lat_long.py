import argparse as arg
import json as js
import sys
from urllib import request, error

API_KEY = "b532eab57e0ef806d7ee79deef2355ec"
BASE_URL = f"http://api.ipstack.com/"

##########################################################
#   Function name: get_location
#   Parameters: ip = ip address to lookup
#   Def: This function is being called by the main function,
#           passing as parameter the ip address we want to lookup.
#           The function will check if a positive response is
#           returned from the BASE_URL which use the default
#           API_KEY and the given IP address to make a url string,
#           if the URL is not valid an error will be raised. Otherwise,
#           the response in JSON format will be processed and query to
#           retrieve the latitude and longitude
#   Return: latitude & Longitude
##########################################################
def get_location(ip):
    url = f"{BASE_URL}{ip}?access_key={API_KEY}"

    try:
        response = request.urlopen(url)
        #check for a positive response
        if response.getcode() == 200:
            data = js.load(response)
            return data.get('latitude'), data.get('longitude')
        else:
            return None, None

    except error.URLError as e:
        print(f'UNEXPECTED ERROR: {e}')
        return None, None

def main():
    psr = arg.ArgumentParser(description="Get latitude and longitud of an IP address.")
    psr.add_argument("ip_addr", type=str, help='The IP address to lookup.')

    args = psr.parse_args()

    latitude, longitude = get_location(args.ip_addr)

    if latitude is not None and longitude is not None:
        #Output latitude & longitude as JSON
        sys.stdout.write(f"{latitude} {longitude}")
    else:
        #Print error message to stderr
        print(f"Error: Unable to retrieve location information for IP {args.ip_addr}.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
