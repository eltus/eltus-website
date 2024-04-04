from flask import Flask, request, jsonify
import sqlite3
import bcrypt

app = Flask(__name__)

# Function to hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Function to authenticate user
def authenticate_user(email, password):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('user_authenticate.db')
        cursor = conn.cursor()

        # Query the database to retrieve the hashed password for the given email
        cursor.execute('SELECT password FROM users WHERE email=?', (email,))
        hashed_password = cursor.fetchone()

        if hashed_password:
            # Check if the provided password matches the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password[0].encode('utf-8')):
                return True
        return False

    except sqlite3.Error as error:
        print("Error:", error)
        return False

# Route for handling sign-in requests
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')

    if authenticate_user(email, password):
        return jsonify({'message': 'Sign-in successful'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
