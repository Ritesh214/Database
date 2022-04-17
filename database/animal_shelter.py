from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:52920/?authSource=AAC'%(user,password))
        self.database = self.client['AAC']

	# Method to implement the C in CRUD.
    def create(self, data):
		#Verify that add criteria was provided, else raise an exception
        if data is not None:          
			#Store the results of the insert to variable
            print("--------------------- Inserting New Animal --------------------")
            insert_result = self.database.animals.insert(data)  # data should be dictionary
            print("---------------------------- Done -----------------------------")
            #If insert was successful, return True, else, return False
            if insert_result is not None:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

	# Method to implement the R in CRUD. 
    def read(self, search):
		#Verify that search criteria was provided, else raise an exception
        if search is not None:
            searchResult = self.database.animals.find(search) # data should be dictionary
            return searchResult
        else:
            exception = "Nothing to search, search parameter is empty"
            return exception
            
	# Method to implement the U in CRUD
    def update(self, query, record):
        #Verify that update record exists, else raise an exception
        if record is not None:
            # update the documents matching the query criteria and print no. of documents updated in json format
            update_result = self.database.animals.update_one(query, record)
            result= "Documents updated: " + json.dumps(update_result.modified_count)
            return result
        else:
            raise Exception("Record not found")

	# Method to implement the D in CRUD
    def delete(self, data):
        #Verify that record to be deleted has been supplied, else raise an exception
        if data is not None:
            # delete the documents matching data criteria and print no. of documents deleted in json format
            delete_result = self.database.animals.delete_one(data)
            result = "Documents deleted: "+ json.dumps(delete_result.deleted_count)
            return result
        else:
            raise Exception("No record provided.")
