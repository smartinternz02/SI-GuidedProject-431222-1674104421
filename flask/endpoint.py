import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "U2H78KYjZy34DePXTfeNyaXAVYotNo-PlHu9KOBSagUo"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}


payload_scoring = {"input_data": [{"field": [['goitre','tumor','hypopituitary','psych','TSH','T3','TT4','T4U','FTI','TBG']], "values": [[0,0,0,0,0.000000,0.0,0.0,1.00,0.0,40.0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a0ea54a0-71de-438d-8e55-9edd0df906c8/predictions?version=2023-02-07', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})

print("Scoring response")
print(response_scoring.json())