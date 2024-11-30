import dotenv
import os
import canvasapi
import datetime
from datetime import timedelta

import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor


class CanvasAPI:
    BASEURL = 'https://canvas.ubc.ca'

    def __init__(self, user_id):
        """
        Initializes a CanvasAPI object given a user ID.
        
        Args:
            user_id (int): the unique identifier assigned to the user by the database.
        """

        # Load environmental variables
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.user_id = user_id

        self.HOST = os.environ.get('TIDB_HOST')
        self.PORT = os.environ.get('TIDB_PORT')
        self.DB_USER = os.environ.get('TIDB_USER')
        self.DB_PASSWORD = os.environ.get('TIDB_PASSWORD')
        self.DB_NAME = os.environ.get('TIDB_NAME')
        self.PATH = os.environ.get('CA_PATH')

        # Get token from user_id
        with self.get_connection(autocommit=True) as conn:
            with conn.cursor() as cur:
                userID = (user_id, 100)
                cur.execute("USE test")
                cur.execute("SELECT * FROM users WHERE user_id = %s LIMIT %s", userID)
                self.TOKEN = cur.fetchone()[3]
        
        self.canvas_api = canvasapi.Canvas(self.BASEURL, self.TOKEN)
        self.user = self.canvas_api.get_user('self') #user id
        

    def get_connection(self, autocommit: bool = True) -> MySQLConnection:
        """
        Gets mySQL connector to TiDB database.
        
        Args:
            autocommit (bool): if true, commits changes to database when executing any
                               SQL commands.
        Returns:
            (MySQLConnection): a connector to the TiDB database.
        """

        #config = Config()
        db_conf = {
            "host": self.HOST,
            "port": self.PORT,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "database": self.DB_NAME,
            "autocommit": autocommit,
            "use_pure": True,
        }

        if self.PATH:
            db_conf["ssl_verify_cert"] = True
            db_conf["ssl_verify_identity"] = True
            db_conf["ssl_ca"] = self.PATH
        return mysql.connector.connect(**db_conf)


    def AssignmentList(self):
        """
        Communicates with Canvas API to obtain a list containing all assignments 
        for user with user_id = user_id. 
        
        Returns: 
            (array): an array of Assignment objects containing the user's assignments.
        """

        assignmentList = []

        courses = self.user.get_courses()
        for course in courses:
            try:
                assignments = course.get_assignments()
                
                for assignment in assignments:
                    assignmentList.append(assignment)
            except:
                continue
        
        return assignmentList
    
    def parseDate(self, date) -> datetime.datetime:
        """
        Returns a datetime.datetime from a string 'date' given
        as a string in the format return from a canvasapi date

        Args:
            date (str): date to be parsed
        
        Returns:
            a datetime.datetime of the date specified by the argument 'date'
        """
        
        return datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))


    def UserAssignmentView(self):
        """
        Processes assignments for user with user_id = user_id. Stores
        assignments into SQL database. Due dates and submit by dates
        are stored and treated as times in Pacific Standard Time.
        If any of: assignment name, due date, course name, are null assignment is not added.
        """

        assignments = self.AssignmentList()
        
        for assignment in assignments:
            try:
                due_date = assignment.due_at
                dt = self.parseDate(due_date)
                try:
                    lock_date = assignment.lock_at
                    lt = self.parseDate(lock_date)
                except:
                    lt = self.parseDate(due_date) # if no lt found then set it to be the same as dt
                
                if(dt > datetime.datetime.now()):
                    dt += timedelta(hours = -8) #converting to PT
                    lt += timedelta(hours = -8) #converting to PT
                    dtString = "{year}-{month}-{day} {hour}:{minute}:{second}".format(year=dt.year, month = dt.month, day = dt.day, hour = dt.hour, minute = dt.minute, second = dt.second)
                    ltString = "{year}-{month}-{day} {hour}:{minute}:{second}".format(year=lt.year, month = lt.month, day = lt.day, hour = lt.hour, minute = lt.minute, second = lt.second)
                    with self.get_connection(autocommit=True) as conn:
                        with conn.cursor() as cur:
                            assignmentQUERY = (assignment.name, dtString, ltString, self.user_id, self.canvas_api.get_course(assignment.course_id).name)
                            cur.execute("USE test")
                            cur.execute("INSERT INTO assignments (name, due_date, submit_by_date, pinned, completed, source, user_id, course) VALUES (%s, %s, %s, 0, 0, 'Canvas', %s, %s)", 
                                        assignmentQUERY)
            except:
                continue