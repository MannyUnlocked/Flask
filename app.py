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
import uuid  # Import uuid for generating unique transaction IDs

app = Flask(__name__)
CORS(app)

@app.route('/transaction-mode', methods=['POST', 'GET'])
def transaction_notification():
    if request.method == 'POST':
        data = request.json
        success = data.get('success')
        print('POST method received')
        if success:
            transaction_id = str(uuid.uuid4())  # Generate a unique transaction ID
            print('Successful transaction received.')
            return jsonify({'message': 'Transaction recorded successfully', 'success': True, 'transaction_id': transaction_id}), 200
        else:
            return jsonify({'message': 'Invalid request'}), 400
    elif request.method == 'GET':
        print('GET method received')
        # For demonstration, return a static response with a unique transaction ID
        return jsonify({'message': 'GET request received', 'success': True, 'transaction_id': str(uuid.uuid4())}), 200



