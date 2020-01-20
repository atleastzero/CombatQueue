from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/characters')
def show_characters():
    return render_template("PC_index.html")

@app.route('/addCharacter')
def create_character():
    return render_template("PC_new.html")