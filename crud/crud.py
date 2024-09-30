from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.example_database
collection = db.example_collection

# Create
document = {"name": "abolfalz", "age": 18, "city": "tabriz"}
result = collection.insert_one(document)
print(f"Document inserted with _id: {result.inserted_id}")

# Read
query = {"name": "abolfazl"}
retrieved_document = collection.find_one(query)
print(f"Retrieved document: {retrieved_document}")

# Update
update_query = {"name": "abolfazl"}
new_values = {"$set": {"age": 26}}
collection.update_one(update_query, new_values)
updated_document = collection.find_one(query)
print(f"Updated document: {updated_document}")

# Delete
delete_query = {"name": "abolfazl"}
collection.delete_one(delete_query)
deleted_document = collection.find_one(query)
