from flask import Flask, request, redirect, url_for, render_template

from config import Config

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


app.add_url_rule('/', view_func=login)

if __name__ == "__main__":
    config = Config("localhost", "8080", False)
    app.run(config.HOST, config.PORT, config.DEBUG)
