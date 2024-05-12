from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')