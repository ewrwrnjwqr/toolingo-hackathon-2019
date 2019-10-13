from flask import Flask, request, redirect
from flask import render_template
from ast import literal_eval
app = Flask(__name__)


# Input("Kyan", ["Hebrew, English"],["Spanish"])
# print(database)





@app.route('/')
def hello_world():
    return 'This website is working, are you?'



@app.route('/inputs', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        return render_template('response.html', name=request.form["name"], known_language=request.form["known_language"], desired_language=request.form["desired_language"])

    return render_template('inputtts.html')

if __name__ == '__main__':
    app.run()

