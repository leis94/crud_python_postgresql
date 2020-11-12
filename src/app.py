from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://seviajhr:RwfP9-rDCIZZY5QGwU0RHTgQBDdZi3OS@lallah.db.elephantsql.com:5432/seviajhr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/tasks', methods=['POST'])
def create_task():
    print(request.json)
    return 'received'



if __name__== '__main__':
    app.run(debug=True)