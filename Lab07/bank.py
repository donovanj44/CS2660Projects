"""
Catamount Community Bank
Flask Routes

Warning: This app contains deliberate security vulnerabilities
Do not use in a production environment! It is provided for security
training purposes only!

"""


import csv
from config import display
from flask import Flask, render_template, request, url_for, flash, redirect
from db import Db
from lessons import sql_injection
from lessons.password_crack import authenticate
from lessons.password_crack import hash_pw

app = Flask(__name__, static_folder='instance/static')

app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def home():
    """ Bank home page """
    return render_template('home.html',
                           title="Home Page",
                           heading="Home Page",
                           show=display)


@app.route("/transactions", methods=['GET', 'POST'])
def transactions():
    """ Transaction injection attack """
    search_term = ''
    params = ()
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        query, params = sql_injection.create_search_query(1234, search_term)
    else:
        query = 'SELECT * FROM trnsaction WHERE trnsaction.account_id = ? AND trnsaction.memo LIKE ?'
        params = (1234, '%')

    cnx = Db.get_connection()
    c = Db.execute_query(cnx, query, params)
    rows = c.fetchall()
    return render_template('transactions.html',
                           search_term=search_term,
                           rows=rows,
                           query=query,
                           title="My Transactions",
                           heading="My Transactions")


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Login the user."""
    with open(app.config['CREDENTIALS_FILE']) as fh:
        reader = csv.DictReader(fh)
        credentials = {row['username']:
                           {'acct_id': row['id'],
                            'pw_hash': row['password_hash']}
                       for row in reader}

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            stored_hash = credentials[username]['pw_hash']
            if authenticate(stored_hash, password):
                return redirect(url_for('login_success',
                                        id_=credentials[username]['acct_id']))
        except KeyError:
            pass

        flash("Invalid username or password!", 'alert-danger')
    return render_template('login.html',
                           title="Secure Login",
                           heading="Secure Login")


@app.route("/login_success/<int:id_>", methods=['GET', ])
def login_success(id_):
    flash("Welcome! You have logged in!", 'alert-success')
    return render_template('customer_home.html',
                           title="Customer Home",
                           heading="Customer Home")


@app.route('/catcoin_stock')
def cat_coin_stock():
    my_netid = "jreddy1"  # Replace with your UVM NetID here!
    return render_template("catcoin_stock.html", netid=my_netid)


@app.route("/hashit", methods=['GET', ])
def hashit():
    """ Hash a password. DON'T EVER DO THIS LIKE THIS IN THE REAL WORLD!
        To use this route to generate a sha1 hash:
        1. Run the Flask app (werk.py)
        2. Open a browser and follow this format in the URL:
            http://localhost:8097/hashit?pw=testpassword
            where the password "testpassword" is passed into the "hashit" function and
            the sha1 hash of that string is returned in the browser (in this case):
                8bb6118f8fd6935ad0876a3be34a717d32708ffd
        3. Replace "testpassword" in the query string with another string to generate
            the sha1 hash of that string.
    """
    pw = request.args.get('pw')
    return hash_pw(pw)
