# import Flask and request
from flask import Flask, app, request

# develop the app
app = Flask(__name__)

# both GET and POST requests
@app.route("/form-example", methods=['GET', 'POST'])
def form_example():
    # the POST request
    if request.method == 'POST':
        username = request.form.get('username')
        interest = request.form.get('interest')
        return '''
            <h1>The student's name is: {}</h1>
            <h1>The field of interest is: {}</h1>'''.format(username, interest)
    
    # the GET request
    return '''
              <form method="POST">
                  <div><label>Username: <input type="text" name="username"></label></div>
                  <div><label>Interest: <input type="text" name="interest"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

if __name__ == '__main__':
    # we'll run the app in debug mode on port 3000
    app.run(debug=True, port=3000, host="0.0.0.0")