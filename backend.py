from flask import request, jsonify
from pymongo import MangoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_decription:
        return jsonify({"error": "Both fields are required"}), 400

    result = collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "Item saved",
        "id": str(result.inserted_id)
    }), 201
