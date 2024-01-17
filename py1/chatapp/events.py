from flask import Flask, request
from flask_socketio import emit

from .extensions import socketio

users = {}

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined!")
    users[username] = request.sid

@socketio.on("new_message")
def handle_new_message(message):
    with open('records.txt', 'a', newline='') as file:
      file.write(message)
    file.close()
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)
    
@socketio.on("typing")
def handle_typing():
    emit("typing", broadcast=True)
    


