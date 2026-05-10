from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ✅ HOME PAGE ROUTE (IMPORTANT)
@app.route('/')
def home():
    return render_template('index.html')

# Booking API
@app.route('/book', methods=['POST'])
def book():
    data = request.json
    return jsonify({"message": "Appointment booked successfully"})

if __name__ == '__main__':
    app.run(debug=True)