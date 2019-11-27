import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'age': "1",   
                            'workclass': "",   
                            'fnlwgt': "1",   
                            'education': "",   
                            'education-num': "1",   
                            'marital-status': "",   
                            'occupation': "",   
                            'relationship': "",   
                            'race': "",   
                            'sex': "",   
                            'capital-gain': "1",   
                            'capital-loss': "1",   
                            'hours-per-week': "1",   
                            'native-country': "",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/d84ea6d5be6046e982533287f5953cef/services/0c1326e4f7d84cc2908a08424deead14/execute?api-version=2.0&format=swagger'
api_key = 'Wxk4/E3HVU/XT2Kl3kdgJ+2DLCUA0OtQ1JP5wJuAd7PYBmHGHBFVV/lra2WrKyi2oxe+DpmG8HUiVWqVA6/CtA==' # Replace this with the API key for the web service
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
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'age': "1",   
                            'workclass': "",   
                            'fnlwgt': "1",   
                            'education': "",   
                            'education-num': "1",   
                            'marital-status': "",   
                            'occupation': "",   
                            'relationship': "",   
                            'race': "",   
                            'sex': "",   
                            'capital-gain': "1",   
                            'capital-loss': "1",   
                            'hours-per-week': "1",   
                            'native-country': "",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://studio.azureml.net/apihelp/workspaces/d84ea6d5be6046e982533287f5953cef/webservices/3f27f38e0c5447fb9607d28b46cb11e9/endpoints/0c1326e4f7d84cc2908a08424deead14/score'
api_key = 'abc123' # Replace this with the API key for the web service
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
