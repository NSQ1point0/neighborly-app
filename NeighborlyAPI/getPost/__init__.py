import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            # DONE: Update with appropriate MongoDB connection information
            url = "mongodb://neighborly-db-account:t2r7hpz8NXdu5ekhd7MruazEG8D5GAtbcOmMTKRlzxm9S9E3CBtOY8ZroTIszz6SRMNKUDLp7oo20ABnpNjnGA==@neighborly-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-db-account@"
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
