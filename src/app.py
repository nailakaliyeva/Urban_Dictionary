import requests, os, json

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
#print("Hello, {}".format(input("What is your name?")))
word = input("What term do you want to look for?")
querystring = {"term":word}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
the_definition = "".join([i for i in data["list"][0]["definition"] if i != "[" and i!="]"])
print(word.capitalize() + " is "+ the_definition)

new = {}
new["definitions"] = []
new["definitions"].append({word: the_definition})

with open("json_file.json", "w+") as f:
    json.dump(new, f)
