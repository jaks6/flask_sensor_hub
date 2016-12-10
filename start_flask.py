import os
import json
from flask import Flask, render_template, g
import sqlite3
from sensor_reader import hat_sensors

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, './sensor_reader/sqlite.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route("/")
def main():
    sensor_values = hat_sensors.get_values()
    db = get_db()
    cur = db.execute('select value, timestamp from "values" order by id asc')
    rows = cur.fetchall()
    history = json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    avg = rows[len(rows)-1][0] #take last row-s first property  
    return render_template('sensors.html', history = history, sensor_values = sensor_values, avg = avg, format = format)

if __name__ == "__main__":
    app.run(host='0.0.0.0')





