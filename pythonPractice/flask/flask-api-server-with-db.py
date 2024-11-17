from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database URI (this can also be PostgreSQL, MySQL, etc.)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# Define a model for the Item (this maps to a database table)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Item {self.name}>"

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}


# Create the database and the Item table
with app.app_context():
    db.create_all()


# Route to get all items (GET)
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()  # Query all items from the database
    return jsonify({"items": [item.to_dict() for item in items]})


# Route to get a specific item by ID (GET)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if item:
        return jsonify(item.to_dict())
    else:
        abort(404, description=f"Item with ID {item_id} not found.")


# Route to create a new item (POST)
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400, description="Bad Request: Missing 'name' field.")
    
    item = Item(name=request.json['name'], description=request.json.get('description', ""))
    db.session.add(item)  # Add the new item to the database session
    db.session.commit()    # Commit the session to save the item

    return jsonify(item.to_dict()), 201  # 201 means "Created"


# Route to update an existing item (PUT)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        abort(404, description=f"Item with ID {item_id} not found.")
    
    if not request.json:
        abort(400, description="Bad Request: Request body must be JSON.")
    
    item.name = request.json.get('name', item.name)
    item.description = request.json.get('description', item.description)
    
    db.session.commit()  # Save the changes to the database
    return jsonify(item.to_dict())


# Route to delete an item (DELETE)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        abort(404, description=f"Item with ID {item_id} not found.")
    
    db.session.delete(item)
    db.session.commit()  # Save the deletion to the database
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
