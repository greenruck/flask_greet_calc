from flask import Flask, request

app = FLASK(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Practice HQ"

@app.route('/welcome')
def welcome():
    return "WELCOME"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome Back"

