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
import uuid

app = Flask(__name__)
CORS(app)

# Variable to store the last transaction ID
last_transaction_id = None

@app.route('/transaction-mode', methods=['POST'])
def transaction_notification():
    global last_transaction_id
    data = request.json
    success = data.get('success')
    print('POST method received')
    if success:
        # Generate a new transaction ID for a successful transaction
        last_transaction_id = str(uuid.uuid4())
        print('Successful transaction received.')
        return jsonify({'message': 'Transaction recorded successfully', 'success': True, 'transaction_id': last_transaction_id}), 200
    else:
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/transaction-mode', methods=['GET'])
def check_transaction_status():
    global last_transaction_id
    print('GET method received')
    if last_transaction_id:
        return jsonify({'message': 'GET request received', 'success': True, 'transaction_id': last_transaction_id}), 200
    else:
        return jsonify({'message': 'No transaction found', 'success': False}), 200




