from flask import Flask, jsonify,request

app = Flask(__name__)

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

@app.route('/api/data', methods=['GET'])
def get_json_data():
    return jsonify(data)

@app.route('/api/app', methods=['POST'])
def update_json_data():
    # Retrieve JSON data from the request
    request_data = request.get_json()
    print(request_data)
    # Update the existing data with the new data
    data.update(request_data)

    # Return the updated data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run()
