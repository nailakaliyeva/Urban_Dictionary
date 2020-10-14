import requests, os, json, sys

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
#words = input("What term do you want to look for?").split(",")
cache = {}                                           #so this is the way to store information in a dict
cache["definitions"] = []
list_sys = sys.argv[1:]
for i in range(0,len(list_sys)):
    word = list_sys[i]
#for i in words: 
    #word = i
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
                                
    cache["definitions"].append({word: the_definition})  
    


    if word in cache["definitions"][0].keys():  #need to ask Paolo how to test  lines 42 & 43, cuz I think it's skipping them
        print(word.capitalize()+ " is "+ cache["definitions"][0][word]) #since the app only asks for words only when you
    else:                                                               #run "pipenv run python src/app.py"
        print(word.capitalize() + " is "+ the_definition) 

    

    #this is how to store new data in a json file
with open("json_file.json", "a") as f:                 
    json.dump(cache, f)
    
