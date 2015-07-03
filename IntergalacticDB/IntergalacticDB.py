from flask import Flask, render_template
from IntergalacticDB.models import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/characters')
def characters():
    all_chartacters = Character.get_all_characters()
    return render_template('characters.html', all_chartacters=all_chartacters)

if __name__ == '__main__':
    app.run()
