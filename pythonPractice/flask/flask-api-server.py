from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Simulating a database with an in-memory dictionary
data_store = {
    1: {"name": "Item 1", "description": "This is item 1"},
    2: {"name": "Item 2", "description": "This is item 2"}
}

# Helper function to find an item by ID
def find_item(item_id):
    return data_store.get(item_id)


# Route to get all items (GET)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": data_store})


# Route to get a specific item by ID (GET)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify(item)
    else:
        abort(404, description=f"Item with ID {item_id} not found.")


# Route to create a new item (POST)
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400, description="Bad Request: Missing 'name' field.")
    
    new_id = max(data_store.keys()) + 1
    item = {
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    data_store[new_id] = item
    return jsonify(item), 201  # 201 means "Created"


# Route to update an existing item (PUT)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        abort(404, description=f"Item with ID {item_id} not found.")
    
    if not request.json:
        abort(400, description="Bad Request: Request body must be JSON.")
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    
    data_store[item_id] = item
    return jsonify(item)


# Route to delete an item (DELETE)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        abort(404, description=f"Item with ID {item_id} not found.")
    
    del data_store[item_id]
    return jsonify({"result": f"Item with ID {item_id} deleted."}), 200


# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": error.description}), 404


# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400


# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
