from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'facdddaeea9463450eb4c01615d93c27'

# Function to connect to the database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('users.db')
        g.db.row_factory = sqlite3.Row
    return g.db

# Create the 'users' and 'books' tables if they don't exist
def init_db():
    db = get_db()
    with app.open_resource('bibilomart.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

    # Create 'books' table if it doesn't exist
    with app.open_resource('create_books_table.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

    # Populate 'books' table with sample data
    populate_books_table(db)

def populate_books_table(db):
    cursor = db.cursor()
    books_data = [
        ('Introduction to Physics', 'Jim Breithaupt', 'A comprehensive introduction to the principles of physics.', 39.99),
        ('Engineering Mechanics', 'Knowledge flow', 'Learn the fundamentals of engineering mechanics.', 49.99),
        ('Computer Science Fundamentals', 'Alan Johnson', 'Essential concepts and theories in computer science.', 29.99),
        ('Advanced Mathematics', 'Celia, A T F Nice', 'Explore advanced topics in mathematics.', 59.99),
        ('Electrical Engineering Principles', 'Allan Hambley', 'Fundamental principles of electrical engineering.', 34.99),
        ('Chemical Engineering Basics', 'James Riggs', 'Introduction to the basics of chemical engineering.', 44.99)
    ]

    for book in books_data:
        title, author, description, price = book
        cursor.execute('INSERT INTO books (title, author, description, price) VALUES (?, ?, ?, ?)', (title, author, description, price))
    
    db.commit()

@app.before_request
def before_request():
    init_db()  # Initialize the database before handling each request

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        messages = get_flashed_messages()
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        if user:
            session['username'] = username
            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username or password', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists', 'error')
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            session['username'] = username
            flash('Registration successful', 'success')
            return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/admin')
def admin():
    if 'username' in session:
        username = session['username']
        return f'Welcome, {username}! This is your admin.'
    else:
        return redirect(url_for('register'))

@app.route('/health.html')
def health():
    return render_template('health.html')
    
@app.route('/Introduction to Physics.html')
def Introduction_to_Physics():
    return render_template('Introduction to Physics.html')
    
@app.route('/Engineering Mechanics.html')
def Engineering_Mechanics():
    return render_template('Engineering Mechanics.html')
    
@app.route('/Computer Science Fundamentals.html')
def Computer_Science_Fundamentals():
    return render_template('Computer Science Fundamentals.html')
    
@app.route('/Advanced Mathematics.html')
def Advanced_Mathematics():
    return render_template('Advanced Mathematics.html')
    
@app.route('/Electrical Engineering Principles.html')
def Electrical_Engineering_Principles():
    return render_template('Electrical Engineering Principles.html')
    
@app.route('/Chemical Engineering Basics.html')
def Chemical_Engineering_Basics():
    return render_template('Chemical Engineering Basics.html')
                    
@app.route('/Introduction to Programming.html')
def Introduction_to_Programming():
    return render_template('Introduction to Programming.html')
    
@app.route('/Data Structures and Algorithms.html')
def Data_Structures_and_Algorithms():
    return render_template('Data Structures and Algorithms.html')
    
@app.route('/History of Science.html')
def History_of_Science():
    return render_template('History of Science.html')
    
@app.route('/The Art of Photography.html')
def The_Art_of_Photography():
    return render_template('The Art of Photography.html')

@app.route('/Foundations of Health Science.html')
def Foundations_of_Health_Science():
    return render_template('Foundations of Health Science.html')
    
@app.route('/Advanced Topics in Health Informatics.html')
def Advanced_Topics_in_Health_Informatics():
    return render_template('Advanced Topics in Health Informatics.html')
    
@app.route('/Exploring Medical Research Methods.html')
def Exploring_Medical_Research_Methods():
    return render_template('Exploring Medical Research Methods.html')
    
@app.route('/Practical Applications in Public Health.html')
def Practical_Applications_in_Public_Health():
    return render_template('Practical Applications in Public Health.html')
               
@app.route('/books.html')
def books():
    return render_template('books.html')

@app.route('/science.html')
def science():
    return render_template('science.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    db = get_db()
    cursor = db.cursor()

    if query:
        # Search for books based on title or author containing the query
        cursor.execute('SELECT * FROM books WHERE LOWER(title) LIKE ? OR LOWER(author) LIKE ?', (f'%{query}%', f'%{query}%'))
        books = cursor.fetchall()
    else:
        books = []

    return render_template('search.html', books=books)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the 'username' from the session
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
