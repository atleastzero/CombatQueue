from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

host = os.environ.get('mongodb://localhost:27017/TTRPI')

client = MongoClient()
db = client.TTRPI
pcs = db.pcs

@app.route('/')
@app.route('/PCs')
@app.route('/pcs')
def pc_index():
    return render_template("PC_index.html", pcs=pcs.find())

@app.route('/PCs/new')
@app.route('/pcs/new')
def pc_new():
    return render_template("PC_new.html", pc={})

@app.route('/PCs', methods=["POST"])
def pc_submit():
    pc = {
        'name': request.form.get('name'),
        'age': request.form.get('age')
    }
    print(pc)
    pc_id = pcs.insert_one(pc).inserted_id
    print(pc_id)
    return redirect(url_for("pc_index"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))