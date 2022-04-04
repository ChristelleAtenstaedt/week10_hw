# We have created a dynamic request

from flask import Flask, Response, request, url_for

app = Flask(__name__)

# 3 routes all part of the same application
@app.route('/')
def welcome_to_flask():
    return "Welcome to Flask!"

@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"

@app.route('/bye')
def bye_from_flask():
    return "Bye from Flask!"

#@app.route('/get/text')
#def get_text():
    #return Response("Hello from a RESPONSE object", mimetype='text/plain')

@app.route('/post/text', methods=['POST']) # can only respond if it's a HTTP POST request
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data: " + data_sent, mimetype='text/plain')

# Homework - week 10

@app.route('/dynamic/<word>')
def home(word):
    return word


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is" + " " + str(squared)
    return line

# Activity 1


@app.route('/user/<name>')
def hello(name):
    greeting = "Hello" + " " + name
    # above - the curly braces {} hold a variable; when this runs,
    # the value will replace the braces and the variable name
    return greeting

# Activity 2 - the title isn't working for some reason?

# triple quotes are use to enclose strings containing single or double quotes, or (as in this case) to represent a multi-line string # the .format() method formats the specified value(s), in this case 'name', and inserts them inside the string's placeholder, which is defined using {}...

@app.route('/hello/<name>')
def say_hello_page(name):
    return """" 
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name page</h1>
    <p>Hello {}!</p>
</body>
</html>
""".format(name)

# Activity 3


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name page</h1>
    <p>Hello {}!</p>
    <p>You are {} year(s) old.</p>
    <hr>
    <a href="{}">Welcome</a>
</body>
</html>
""".format(name, age, url)

#Activity 4


#@app.route('/photo/page')
@app.route('/photo/page')
def photo_page():
    return Response ("Photo of me - aren't I cute?!", mimetype='text/plain')


@app.route("/about_page/<name>/<int:age>/<hobby>/<location>")
def about_page(name, age, hobby, location):
    url = url_for('static', filename='LittleG.jpg') # I now can't get photo_page in there anymore without an error
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>About page</h1>
    <p>This is a page about {}!</p>
    <p>I am {} year(s) old.</p>
    <p>My favourite hobby is {}</p> 
    <p>I live in {}</p>
    <hr>
    <a href="{}">Photo of me!</a>
    
</body>
</html>
""".format(name, age, hobby, location, url)




if __name__ == "__main__":
    app.run(debug=True, port=4000)# named parameter debug = True



