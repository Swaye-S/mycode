#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials 
# it is easily recyled from our previous script 

def returncreds():
    ## first i want to grab my credentials 
    with open('/home/student/nasa.creds', 'r') as mycreds:
        nasacreds = mycreds.read()
    ## remove any new lines from api key
    nasacreds = 'api_key=' + nasacreds.strip('\n')
    return nasacreds

# this is our main function
def main():
    ## first grab credentials 
    nasacreds = returncreds()

    ##update the dare below, if you like
    startdate = 'start_date=2023-07-11'

    ## the value below is not being used in this 
    ## version of the script 
    #enddate = 'end_date=END_DATE'

    #make a request with the request library 
    neowrequest = requests.get(NEOURL + startdate + '&' + nasacreds)

    # strip off json attachment from our response 
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata) 
if __name__ == '__main__':
    main() 
