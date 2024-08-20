# stonks: 2 - Week Flask Roadmap

This roadmap is designed to guide the development of `stonks` a Flask-based web application that allows users to manage a personalized stock watchlist. Over the course of two weeks, the intern will learn the basics of Flask, how to structure a web application, manage user authentication, integrate third-party APIs for real-time stock data, and visualize data. The project will also involve setting up a development environment using Poetry for dependency management and deploying the application. By the end of this roadmap, the intern will have built a fully functioning stock watchlist application with features such as user sign-up, login, personalized watchlists, and detailed stock information.

### **Week 1: Flask Basics and Application Development**

**Day 1: Introduction to Flask and Project Setup**

- Install Flask and create a basic "Hello, World!" application.
- Understand Flask's core concepts: the application object, routes, HTTP methods (GET, POST).
- Set up the foundation for stonks: create a homepage.

**Day 2: Setting Up Poetry for Dependency Management**

- Install and configure [Poetry](https://python-poetry.org/) for managing project dependencies.
- Use Poetry to create a `pyproject.toml` file.
- Learn how to add, update, and manage dependencies using Poetry.
- Integrate Poetry with stonks for streamlined dependency management and environment setup.

**Day 3: Application Structure and Dynamic Content**

- Dive into Flask’s application structure: `app`, `route`, `templates`, `static`.
- Manage dynamic content using the Jinja2 template engine.
- Create a basic watchlist page where users can add and view their selected stocks.

**Day 4: Form Handling with Flask**

- Use Flask-WTF for form validation.
- Create forms for users to sign up and log in.
- Capture user input through forms and handle session management for logged-in users.

**Day 5: Introduction to Database Handling**

- Set up a database connection using Flask-SQLAlchemy.
- Create simple database models (e.g., User, Stock models).
- Enable users to save their watchlist to the database and persist this data.

**Day 6: Enhancing stonks**

- Improve and refine stonks.
- Dynamically list the stocks in the user’s watchlist.
- Create a stock details page where users can view detailed information about each stock.

**Day 7: Weekly Review and Project Enhancement**

- Recap the topics covered during the week.
- Address any issues or bugs in the application.
- Prepare for the more advanced topics in the upcoming week.

### **Week 2: Advanced Topics and Final Project**

**Day 8: Modular Application Development with Flask Blueprints**

- Introduce the concept of Flask Blueprints.
- Organize the application into modules using Blueprints (`auth`, `watchlist`, `main`).
- Refactor stonks into a modular structure.

**Day 9: User Authentication and Session Management**

- Implement user authentication and session management using Flask-Login.
- Set up user registration and login systems.
- Ensure that users can only access and manage their own watchlist.

**Day 10: Real-Time Data Fetching with API Integration**

- Integrate third-party APIs (e.g., Alpha Vantage, Finnhub) to fetch real-time data for stocks.
- Retrieve real-time pricing for each stock in the user’s watchlist.
- Display stock details and real-time data on the stock details page.

**Day 11: Data Visualization**

- Use Matplotlib or Chart.js to create visual representations of stock performance.
- Add charts to show price trends and other key metrics for stocks in the watchlist.
- Enhance the application with data visualizations on the stock details page.

**Day 12: Notifications and Reporting with Flask-Mail**

- Send email notifications using Flask-Mail.
- Notify users of significant changes in the stocks on their watchlist.
- Create and send reports of stock performance via email.

**Day 13: Deploying the Application**

- Deploy the application to a server (using Heroku, PythonAnywhere, or Docker).
- Discuss deployment best practices.
- Manage environment variables and implement security measures.

**Day 14: Project Presentation and Wrap-Up**

- Finalize stonks by making improvements and fixing any remaining bugs.
- Present the project: The intern will demonstrate what they have learned by showcasing the application.
- Provide feedback on the project, suggest improvements, and discuss the next steps.
