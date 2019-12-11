from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

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



@app.route('/bracelets/<bracelet_id>')
def bracelets_detail(bracelet_id):
    """Show a single playlist."""
    bracelet = bracelets.find_one({'_id': ObjectId(bracelet_id)})
    return render_template('bracelets_detail.html', bracelet = bracelet)

@app.route('/bracelets/<bracelet_id>', methods=['POST'])
def bracelets_update(bracelet_id):
    """Submit an edited bracelet."""
    
    # create our updated playlist
    updated_bracelet = {
        'brand': request.form.get('brand'),
        'size': request.form.get('size'),
        'image': request.form.get("image"),
        'price': request.form.get("price")    
    }
    # set the former playlist to the new one we just updated/edited
    bracelets.update_one(
        {'_id': ObjectId(bracelet_id)},
        {'$set': updated_bracelet})
    # take us back to the playlist's show page
    return redirect(url_for('bracelets_detail', bracelet_id=bracelet_id))


@app.route('/bracelets/<bracelet_id>/edit')
def bracelets_edit(bracelet_id):
    """Show the edit form for a playlist."""
    bracelet = bracelets.find_one({'_id': ObjectId(bracelet_id)})
    # Add the title parameter here
    return render_template('bracelets_edit.html', bracelet=bracelet, title='Edit bracelet')




