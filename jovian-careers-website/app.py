from flask import Flask, render_template, jsonify
from db_utils import initialize_database, get_mysql_connection
from default_config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, DATA_FILE_NAME, WAIT_TIME
import os
import time

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', MYSQL_HOST)
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', MYSQL_USER)
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', MYSQL_PASSWORD)
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', MYSQL_DB)
app.config['DATA_FILE_NAME'] = os.environ.get('DATA_FILE_NAME', DATA_FILE_NAME)
app.config['WAIT_TIME'] = int(os.environ.get('WAIT_TIME', WAIT_TIME))

# Wait for MySQL to start
time.sleep(app.config['WAIT_TIME'])

# Initialize the database
initialize_database(app)


@app.route("/")
def hello_jovian():
  with get_mysql_connection(app) as conn:
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM jobs")
    data = cur.fetchall()
  return render_template('home.html', 
                          jobs=data, 
                          company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  with get_mysql_connection(app) as conn:
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM jobs")
    data = cur.fetchall()
  return jsonify(data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5001)