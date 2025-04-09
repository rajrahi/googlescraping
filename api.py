import requests
import json




def get_keywords(limit , skip):

    keywords = []

    limit = limit
    skip = skip

    # Replace with the actual URL of your API endpoint              
    api_url = f"https://4884-106-51-128-51.ngrok-free.app/get_keywords?limit={limit}&skip={skip}"

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


def post_feed(feed_data):
    # Replace with the actual URL of your API endpoint
    api_url = "https://4884-106-51-128-51.ngrok-free.app/feed/"
    
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_url, data=feed_data, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error making request: {e}"
