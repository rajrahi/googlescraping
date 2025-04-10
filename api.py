import requests
import json


from  pydantic_model import AdData



def open_config():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        return "Error: config.json file not found"
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in config.json"

api = open_config()['api']

def get_keywords(limit , skip):

    keywords = []

    limit = limit
    skip = skip


    # Replace with the actual URL of your API endpoint              
    api_url = f"{api}/get_keywords?limit={limit}&skip={skip}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            for d in data["data"]:
                keywords.append(d)

            skip += limit
            print(skip)
            
            
            # print(json.dumps(data , indent=4))
        else:
            return f"Error: Status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error making request: {e}"

    return keywords

# print(get_keywords(1 , 0))


# def post_feed(feed_data):
#     # Replace with the actual URL of your API endpoint
#     api_url = f"{api}/append/"
    
#     try:
#         headers = {'Content-Type': 'application/json'}
#         response = requests.post(api_url, json=feed_data, headers=headers)
        
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return f"Error: Status code {response.status_code}"
#     except requests.exceptions.RequestException as e:
#         return f"Error making request: {e}"
    
def post_feed(ad: AdData):
    api_url = "https://4e02-2406-7400-56-ab78-6ce0-b010-bd9-1e58.ngrok-free.app/append/"  # Replace with your real URL
    headers = {"Content-Type": "application/json"}
    
    # Convert Pydantic model to dict
    feed_data = ad.dict()  # or ad.model_dump() for Pydantic v2+

    # Send as JSON
    response = requests.post(api_url, json=feed_data, headers=headers)
    
    return response.json() 


