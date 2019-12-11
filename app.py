from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


client = MongoClient()
db = client.bracelet
bracelets = db.bracelets



app = Flask(__name__)

@app.route('/')
def bracelets_index():
    """Return homepage."""
    return render_template('bracelets_index.html', bracelets=bracelets.find())

@app.route('/bracelets/new')
def bracelets_new():
    """Create a new bracelet."""
    return render_template('bracelets_new.html')
    
@app.route('/bracelets', methods=['POST'])
def bracelet_submit():
    """Submit a new bracelet."""
    bracelet = {
        'brand': request.form.get('brand'),
        'size': request.form.get('size'),
        'image': request.form.get('image'),
        'price': request.form.get('price')
    }
    bracelets.insert_one(bracelet)# may need to be bracelets
    #print(request.form.to_dict())
    return redirect(url_for('bracelets_index'))




