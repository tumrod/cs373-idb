from flask import Flask, render_template
from Models import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/characters')
@app.route('/characters/sort_by=<sort_by>')
def characters(sort_by=None):

    if sort_by is not None:
        all_characters = Character.get_all_sorted_characters(sort_by)
    else:
        all_characters = Character.get_all_characters()

    return render_template('characters.html', all_characters=all_characters)

if __name__ == '__main__':
    app.run()
