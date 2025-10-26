from flask import Flask, request, jsonify
app = Flask(__name__)

# This is a temporary in-memory "database"
# It's just a simple Python list. The data will reset if the server restarts.
complaints = []
complaint_id_counter = 1 # To give each complaint a unique ID

@app.route('/api/complaints', methods=['GET', 'POST'])
def handle_complaints():
    global complaint_id_counter

    if request.method == 'POST':
        # This block is for receiving a new complaint
        data = request.get_json()
        
        # Create a new complaint dictionary
        new_complaint = {
            "id": complaint_id_counter,
            "title": data.get('title'),
            "description": data.get('description'),
            "status": "Pending" # Default status
        }
        
        complaints.append(new_complaint)
        complaint_id_counter += 1
        
        return jsonify({"message": "Complaint successfully submitted!", "complaint": new_complaint}), 201 # 201 means "Created"

    else:
        # This block is for sending the list of all complaints
        # The GET method is the default
        return jsonify(complaints)

if __name__ == '__main__':
    app.run(debug=True)