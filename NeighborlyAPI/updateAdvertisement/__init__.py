import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            # DONE: Update with appropriate MongoDB connection information
            url = "mongodb://neighborly-db-account:t2r7hpz8NXdu5ekhd7MruazEG8D5GAtbcOmMTKRlzxm9S9E3CBtOY8ZroTIszz6SRMNKUDLp7oo20ABnpNjnGA==@neighborly-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-db-account@"
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

