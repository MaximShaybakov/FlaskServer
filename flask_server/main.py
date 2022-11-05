from flask import Flask
from data_base.models import Base, engine

app = Flask('app')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(host='127.0.0.1', port=5000)
