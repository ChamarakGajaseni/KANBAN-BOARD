# Database Installation and Visualization Guide

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- [XAMPP](https://www.apachefriends.org/index.html) (which includes MySQL)
- A compatible IDE or text editor

## Installing the Database

1. **Start XAMPP:**
   - Open the XAMPP Control Panel.
   - Start the **Apache** and **MySQL** services by clicking on the "Start" buttons next to each.

2. **Create the Database:**
   - Open your web browser and go to `http://localhost/phpmyadmin`.
   - Click on the **Databases** tab at the top.
   - In the "Create database" named `board-service`, `user-service`, `notification-service`.

3. **Run Database Migrations:**
   - Ensure you have set the `DATABASE_URL` in your `.env` file correctly as follows (or any port that you use to run MySQL):
     ```
     BOARD_DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/board-service
     USER_DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/user-service
     NOTIFICATION_DATABASE_URL=mysql+pymysql://root:@127.0.0.1:3306/notification-service
     ```
      **NOTED** : If the non-alembic ```database.db``` exist, then deletes that file before making initial migration.


   - Make migration according to latest model update.

      ```
      cd backend
      alembic revision --autogenerate -m "migration message"
      ```
      **NOTED** : do this step first if the file is not up to date. 

   - migrate the data

      ```
      alembic upgrade head
      ```

      This command will creates all the tables according to your SQLAlchemy models.

## Visualizing the Database

1. **Access phpMyAdmin:**
   - Open your web browser and go to `http://localhost/phpmyadmin`.
   - Log in using your MySQL credentials (default username is `root`, and the password is empty).

2. **Select the Database:**
   - On the left sidebar, you should see the `workflows` database. Click on it to select it.
   - You can now see all the tables created for your project.


## Conclusion

You have now set up your MySQL database using XAMPP and can visualize it via phpMyAdmin. You can manage your database tables and entries easily from the phpMyAdmin interface.
