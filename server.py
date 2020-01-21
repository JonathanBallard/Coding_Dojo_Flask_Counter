from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'amount' in session:
        pass
    else:
        if request.form.get('amount'):
            session['amount'] = request.form['amount']
        else:
            session['amount'] = 1
    
    if 'count' in session:
        session['count']+=1
    else:
        session['count'] = 0
    return render_template("index.html")


@app.route('/destroy_session')
def destroy():

    session.clear()
    return redirect("/")

@app.route('/2x')
def double():

    if 'count' in session:
        session['count']+=1
    else:
        session['count'] = 0
    return redirect("/")


@app.route('/x', methods=['POST'])
def amountRoute():
    amt = int(request.form['amount'])
    session['count'] += amt - 1
    
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)