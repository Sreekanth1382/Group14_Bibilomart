Flask Web Application
This Flask web application provides a simple user authentication system and a book catalog. Users can register, log in, and view a list of available books. The application also includes some additional pages for health, science, and contact information.

Main Features:
User Authentication:
Users can register and log in to the application.
The login() and register() functions handle user authentication.
Passwords are stored securely in the SQLite database.
Book Catalog:
The application includes a list of books, which are stored in the books table of the SQLite database.
The books() function renders the page that displays the list of books.
Users can search for books based on the title or author.
Database Management:
The application uses a SQLite database to store user and book data.
The get_db() function establishes a connection to the database, and the init_db() function creates the necessary tables if they don't already exist.
The populate_books_table() function adds some sample book data to the books table.
Flask Routing:
The application uses various Flask routes to handle different pages and functionality, such as the index, login, registration, admin, and book-related pages.
Each route function renders the corresponding HTML template.
Flash Messages:
The application uses Flask's flash messaging system to display success and error messages to the user.
The get_flashed_messages() function is used to retrieve the flash messages for display in the templates.
Session Management:
The application uses Flask's session management to keep track of the logged-in user.
The session object is used to store the username of the logged-in user.
HTML Templates:
The application uses Jinja2 templates to render the HTML pages.
The templates are located in the templates directory and are named after the corresponding routes (e.g., index.html, login.html, books.html, etc.).
Running the Application
Install the required dependencies (Flask, SQLite3):
pip install flask
Create the SQLite database file:
The application assumes the database file is named users.db and is located in the same directory as the app.py file.
Run the Flask application:
python app.py
The application will start running in debug mode at http://localhost:5000/.
Access the application in your web browser:
The main page is available at http://localhost:5000/.
Users can register, log in, and navigate to the book catalog and other pages.
File Structure
app.py: The main Flask application file.
bibilomart.sql: SQL script to create the users table.
create_books_table.sql: SQL script to create the books table.
templates/: Directory containing the HTML templates.
index.html: The homepage.
login.html: The login page.
register.html: The registration page.
logout.html: The logout page.
books.html: The book catalog page.
search.html: The search results page.
health.html: The health page.
science.html: The science page.
contact.html: The contact page.
book_pages/: Directory containing individual book pages.
Customization
To customize the application, you can modify the following:

Database: Update the SQLite database schema and corresponding SQL scripts to add more tables or change the existing ones.
Book Catalog: Modify the books table and the populate_books_table() function to add, update, or remove books.
HTML Templates: Customize the HTML templates to change the layout, styling, and content of the pages.
Flask Routes: Add or modify the Flask routes to introduce new functionality or pages.
