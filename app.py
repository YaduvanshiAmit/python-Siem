from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route and a function to handle it

@app.route('/')
def first_page():
    return 'First page!'

@app.route('/home')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
