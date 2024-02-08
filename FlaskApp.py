from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data structure (replace this with a database in production)
data_store = [
    {'id': 1, 'Mateo': 'DevopsQA'},
    {'id': 2, 'Conan': 'Surface'},
    {'id': 3, 'Lyann': 'Surface'}
]

# GET method to retrieve all items
@app.route('/', methods=['GET'])
def get_all_items():
    return jsonify({'items': data_store})

# GET method to retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# POST method to add a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = {'id': len(data_store) + 1, 'name': request.json['name']}
    data_store.append(new_item)
    return jsonify({'message': 'Item created successfully', 'item': new_item}), 201

# PUT method to update a specific item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        item['name'] = request.json['name']
        return jsonify({'message': 'Item updated successfully', 'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# DELETE method to delete a specific item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data_store
    data_store = [item for item in data_store if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
