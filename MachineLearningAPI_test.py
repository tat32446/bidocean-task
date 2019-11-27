import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'make': "alfa-romero",   
                            'body-style': "convertible",   
                            'wheel-base': "88.6",   
                            'engine-size': "130",   
                            'horsepower': "111",   
                            'peak-rpm': "5000",   
                            'highway-mpg': "27",   
                            'price': "13495",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/d84ea6d5be6046e982533287f5953cef/services/aeb307cce2d742f3b3a0a5bfce4118cb/execute?api-version=2.0&format=swagger'
api_key = 'F0AyRRVSxtIPj8PvwO+Bd756+C6MFmBNzyj1a0o0/K6rYWkCAi9TJ9tVNV8k6leeacNKDiUsO0k/HpLGhDWZ6Q==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))