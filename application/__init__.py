from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] ="4545d85c580ef37a12303d35686927852187c3ea8138fe121cd382333dd3"
app.config["MONGO_URI"] = "mongodb+srv://harshitd891:LHw8hTmYbljcf9Bc@cluster0.2edjw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


mongodb_client = PyMongo(app)
db = mongodb_client.cx['Cluster0']

from application import routes
