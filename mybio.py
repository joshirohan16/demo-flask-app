"""
Flask app for my bio
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    "Bio page"
    return "Hello"

#---START
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)