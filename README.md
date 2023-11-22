# To-Do Web Application

Welcome to the To-Do Web Application, a simple yet powerful task management system built using Flask, SQLAlchemy, and Flask-Login.

## Preview : 
![To-do-new](https://github.com/abhishekmuhuri/To-do-webapp/assets/66702834/42b73e67-56a1-445d-a147-ae17ac5692e1)


## Features

- **User Authentication:** Register, login, and logout securely. Passwords are hashed for enhanced security.
- **Task Management:** Create, view, and manage your tasks. Mark tasks as done or undone, and delete tasks as needed.
- **Task Prioritization:** Assign priorities to tasks for better organization. (Low, Medium, High)
- **Responsive Design:** Enjoy a seamless experience, thanks to the responsive web design and Bootstrap.

## Tech Stack
- **Backend:** Flask, SQLAlchemy
- **Authentication:** Flask-Login
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (can be easily configured for other databases)
- **ORM:** SQLAlchemy

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/abhishekmuhuri/To-do-webapp
   cd your-repo

2. Install dependencies:
```bash
  Copy code
  pip install -r requirements.txt

```
3. Set up the database:
```bash
Copy code

flask db init
flask db migrate
flask db upgrade
```
4. Run the application:
 ```bash
  Copy code
  flask run
```

5. Visit http://127.0.0.1:5000 in your web browser.

