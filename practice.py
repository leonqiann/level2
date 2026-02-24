# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'top50songfeb11.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" songfeb11 "
           "LEFT JOIN album on songfeb11.album_id = album.id "
           "LEFT JOIN artist ON songfeb11.artist_id = artist.id "
           "LEFT JOIN featured ON songfeb11.featured_id = featured.id"
           "LEFT JOIN year ON songfeb11.year_id = year.id"
           "LEFT JOIN genre ON songfeb11.genre_id = genre.id"
           )

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect('top50songfeb11.db')
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

print_query('don toliver')
