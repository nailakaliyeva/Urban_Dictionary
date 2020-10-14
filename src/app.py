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

#saving it as a dict so I can parse some information
data = json.loads(response.text)                         

#looping through the definition string to get rid of unwanted chars
the_definition = "".join([i for i in data["list"][0]["definition"] if i != "[" and i!="]"])
                                                       
#creating the dict cache after assigning value to the_definition, otherwise it'll be undefined
cache = {}                                           #so this is the way to store information in a dict
cache["definitions"] = []                            
cache["definitions"].append({word: the_definition})  #so I can append it later to  a json format bc
                                                     # dict is an equivalent of json object

if word in cache["definitions"][0].keys():  #need to ask Paolo how to test  lines 37 & 38, cuz I think it's skipping them
    print(cache["definitions"][word].capitalize()+ " is "+ cache["definitions"][the_definition])
else:
    print(word.capitalize() + " is "+ the_definition) 



#this is how to store new data in a json file
with open("json_file.json", "w+") as f:                 
    json.dump(cache, f)
