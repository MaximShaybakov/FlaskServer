from flask import Flask


app = Flask('app')

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=False, load_dotenv=True)
