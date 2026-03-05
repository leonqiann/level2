from flask import Flask, g
import sqlite3 


DATABASE = 'top50songfeb11.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv   





@app.route("/")
def home():
   #home page

   sql = """SELECT track, artist_name, featured_name, album_name, publication_year, genre_name, duration, streams
                FROM songfeb11
                LEFT JOIN album on songfeb11.album_id = album.id
                LEFT JOIN artist ON songfeb11.artist_id = artist.id
                LEFT JOIN featured ON songfeb11.featured_id = featured.id
                LEFT JOIN year ON songfeb11.year_id = year.id
                LEFT JOIN genre ON songfeb11.genre_id = genre.id;"""
   results = query_db(sql)
   return str(results)
   
@app.route("/song/<int:id>")
def song (id):
    #js one bike based on id 
    sql ="""SELECT track, artist_name, featured_name, album_name, publication_year, genre_name, duration, streams
                FROM songfeb11
                LEFT JOIN album on songfeb11.album_id = album.id
                LEFT JOIN artist ON songfeb11.artist_id = artist.id
                LEFT JOIN featured ON songfeb11.featured_id = featured.id
                LEFT JOIN year ON songfeb11.year_id = year.id
                LEFT JOIN genre ON songfeb11.genre_id = genre.id
                WHERE songfeb11.id = ?""" 
    result = query_db(sql,(id,),True)
    return str(result)

if __name__ == "__main__":
   app.run(debug=True)