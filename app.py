# from flask import Flask, request, jsonify
# from flask_cors import CORS



# app = Flask(__name__)
# CORS(app) 

# @app.route('/transaction-stat', methods=['POST','GET'])
# def transaction_notification():
#     data = request.json  # Get JSON data from the request
#     success = data.get('success') # Extract 'success' parameter from JSON data
#     # transactionid = data.get('transactionId')
#     if success:
#         # Handle successful transaction notification
#         print(f'Successful transaction received.')
#         # print(f'Successful transaction received. Transaction ID: {transactionid}')
#         # You can perform additional actions here, such as logging the transaction, triggering events, etc.
#         return jsonify({'message': 'Success'}), 200  # Respond with success status
#     else:
#         return jsonify({'message': 'Invalid request'}), 400  # Respond with error status
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/transaction-mode', methods=['POST', 'GET'])
def transaction_notification():
    if request.method == 'POST':
        # Handle POST request
        data = request.json  # Get JSON data from the request
        success = data.get('success')  # Extract 'success' parameter from JSON data
        print('POST method recieved')
        if success:
            print('Successful transaction received.')
            # Here, you can perform additional actions, such as logging the transaction, updating a database, etc.
            return jsonify({'message': 'Transaction recorded successfully'}), 200
        else:
            # If the 'success' key is missing or False, return an error response
            return jsonify({'message': 'Invalid request'}), 400
    elif request.method == 'GET':
        print('get method received')
        # Handle GET request
        # For demonstration, let's just return a simple message. 
        # You can adjust this part to return the actual data you want to provide.
        return jsonify({'message': 'GET request received, adjust this response according to your needs.'}), 200



