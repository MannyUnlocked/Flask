# from flask import Flask, request, jsonify
# # from flask_cors import CORS
# from flask import Flask, request, jsonify
# # from flask_cors import CORS


# app = Flask(__name__)
# # CORS(app) 
# @app.route('/')
# def hello():
#     return 'Hello world'
# if __name__ == '__main__':
#    app.run(debug=True)

# @app.route('/transaction-state', methods=['POST'])
# def transaction_notification():
#     data = request.json  # Get JSON data from the request
#     success = data.get('success') # Extract 'success' parameter from JSON data
#     transactionid = data.get('transactionId')
#     if success:
#         # Handle successful transaction notification
#         print(f'Successful transaction received. Transaction ID: {transactionid}')
#         # You can perform additional actions here, such as logging the transaction, triggering events, etc.
#         return jsonify({'message': 'Success'}), 200  # Respond with success status
#         return "success"
#     else:
#         return jsonify({'message': 'Invalid request'}), 400  # Respond with error status

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app) 

@app.route('/transaction-state', methods=['POST'])
def transaction_notification():
    data = request.json  # Get JSON data from the request
    success = data.get('success') # Extract 'success' parameter from JSON data
    transactionid = data.get('transactionId')
    if success:
        # Handle successful transaction notification
        print(f'Successful transaction received. Transaction ID: {transactionid}')
        # You can perform additional actions here, such as logging the transaction, triggering events, etc.
        return jsonify({'message': 'Success'}), 200  # Respond with success status
        # return "success"
    else:
        return jsonify({'message': 'Invalid request'}), 400  # Respond with error status

# if __name__ == '__main__':
#     app.run(debug=True)