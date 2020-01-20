from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/characters')
def show_characters():
    return render_template("show_characters.html")

@app.route('/addCharacter')
def create_character():
    return render_template("create_character.html")