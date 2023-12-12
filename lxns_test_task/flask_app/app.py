from flask import Flask
from flask import render_template
from db_handler import DbHandler

app = Flask(__name__)

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

@app.route('/')
@app.route('/index')
def index():
    db = DbHandler()
    db.connect()
    db_items = db.select_items()
    db.disconnect()
    
    num_items = 0
    estates=[]
    
    if is_iterable(db_items):
        print("Is iterable")
        estates = [{
            "id": item[0],
            "name": item[1],
            "price": item[2],
            "locality": item[3],
            "img_urls": item[4]
        } for item in db_items]
    else:
        print("Not iterable")    
     
    num_items = len(estates)
    return render_template('index.html', estates=estates, num_items=num_items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)