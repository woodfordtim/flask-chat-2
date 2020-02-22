import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME /MESSAGE"

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)