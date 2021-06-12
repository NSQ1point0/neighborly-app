import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        # DONE: Update with appropriate MongoDB connection information
        url = "mongodb://neighborly-db-account:t2r7hpz8NXdu5ekhd7MruazEG8D5GAtbcOmMTKRlzxm9S9E3CBtOY8ZroTIszz6SRMNKUDLp7oo20ABnpNjnGA==@neighborly-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-db-account@"
        client = pymongo.MongoClient(url)
        database = client['azure']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

