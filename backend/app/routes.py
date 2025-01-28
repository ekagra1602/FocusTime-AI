from flask import Blueprint, jsonify
from .models import User, db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return {'message': 'FocusTime AI backend is running!'}

@main.route("/create-user", methods=["GET"])
def create_user():
    new_user = User(username="testuser", email="testuser@example.com")
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"})