from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World! My Improve My City backend is running!'

# This part is needed to run the app directly
if __name__ == '__main__':
    app.run(debug=True)