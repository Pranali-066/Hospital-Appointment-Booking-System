from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allow frontend requests from other ports

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourNewPassword123!",  # Use your new root password
    database="hospital_db"
)

cursor = db.cursor(dictionary=True)

# API route for registration
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    password = data.get("password")

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    existing = cursor.fetchone()
    if existing:
        return jsonify({"message": "Email already registered!"})

    # Insert user
    cursor.execute(
        "INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)",
        (name, email, phone, password)
    )
    db.commit()

    return jsonify({"message": f"Your registration is successful, {name}!"})

# API route for login
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()
    if user:
        return jsonify({"message": f"Welcome back, {user['name']}!"})
    else:
        return jsonify({"message": "Invalid email or password!"})

if __name__ == "__main__":
    app.run(debug=True)