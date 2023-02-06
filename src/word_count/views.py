from flask import Blueprint, render_template, request
from src.word_count.core import WordCountCore
from src.utils.exceptions import NoTextException


home = Blueprint('home', __name__, url_prefix='/')
word_count = Blueprint('word_count', __name__, url_prefix='/count')

@home.route("/", methods=["GET"])
def index():
    headers = {'Content-Type': 'text/html'}
    return render_template('form.html', word_count=None), 200, headers


@word_count.route("/", methods=["POST"])
def count_words():
    try:
        word_count = WordCountCore(payload=dict(request.form)).count_words()
        headers = {'Content-Type': 'text/html'}

        return render_template('form.html', word_count=word_count), 200, headers
        
    except NoTextException as error:
        headers = {'Content-Type': 'text/html'}

        return render_template('form.html', word_count=None, error={"message": error.message}), 200, headers
