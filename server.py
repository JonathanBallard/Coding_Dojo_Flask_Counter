from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():

    if 'count' in session:
        session['count']+=1
    else:
        session['count'] = 0
    return render_template("index.html")







if __name__ == "__main__":
    app.run(debug=True)