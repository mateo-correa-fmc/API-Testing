from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data structure (replace this with a database in production)
data_store = [
    {'id': 1, 'name': 'Mateo','Team':'devopsQA'},
    {'id': 2, 'name': 'Conan','team':'Surface'},
    {'id': 3, 'name': 'Lyann','team':'Surface'}
]

# GET method to retrieve all testers
@app.route('/testers', methods=['GET'])
def get_all_items():
    return jsonify({'items': data_store})

# GET method to retrieve a specific tester by ID
@app.route('/testers/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        return jsonify({'item':     item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# POST method to add a new tester
@app.route('/testers', methods=['POST'])
def create_item():
    new_item = {'id': len(data_store) + 1, 'name': request.json['name']}
    data_store.append(new_item)
    return jsonify({'message': 'Item created successfully', 'item': new_item}), 201

# PUT method to update a specific tester by ID
@app.route('/testers/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        item['name'] = request.json['name']
        item['team'] = request.json['team']
        return jsonify({'message': 'Item updated successfully', 'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# DELETE method to delete a specific tester by ID
@app.route('/testers/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data_store
    data_store = [item for item in data_store if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'})

@app.route('/testers/uppercase/<int:item_id>', methods=['PUT'])
def uppercase_item_name(item_id):
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        item['name'] = item['name'].upper()
        return jsonify({'message': 'Item name changed to uppercase', 'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/testers/update_team/<int:item_id>', methods=['PUT'])
def update_item_team(item_id):
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        team_name = request.json.get('team', '')  # Extract team name from JSON request
        item['team'] = team_name
        return jsonify({'message': f'Team updated to {team_name} for item with ID {item_id}', 'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
