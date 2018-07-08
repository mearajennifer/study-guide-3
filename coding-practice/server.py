from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"


@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Renders the template for form.html"""

    return render_template("form.html")


@app.route('/results')
def show_results():
    """Renders the template for results.html"""

    if request.args.get('cheery'):
        msg_type = "cheery"
        message = """
        Life’s like a movie. Write your own ending.
        """
        auth = "— Kermit the Frog"
    elif request.args.get('dreary'):
        msg_type = "dreary"
        message = """
        Bad days happen to everyone, but when one happens to you, just
        keep doing your best and never let a bad day make you feel bad
        about yourself.
        """
        author = "— Big Bird"
    elif request.args.get('honest'):
        msg_type = "honest"
        message = """
        Who care if me eat carrot or collard greens? Me also like broccoli
        and lettuce and lima beans. Me still Cookie Monster. That not a sham.
        """
        author = "— Cookie Monster"

    return render_template("results.html",
                           message=message,
                           author=author,
                           msg_type=msg_type)


@app.route('/save-name')
def save_name():
    """Saves person's name in a session and returns to homepage"""

    name = request.args.get("person")
    session['name'] = name

    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
