from main import CanvasAPI
import unittest
import datetime

class TestCanvasAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = CanvasAPI(3)

    # Test AssignmentStored1
    def testAssignmentStored1(self):
        with self.api.get_connection(autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("USE test")
                cur.execute("SELECT * FROM assignments WHERE name = 'CPEN221A Project'")
                self.assertEqual(datetime.datetime(2024, 12, 9, 22, 0), cur.fetchone()[2])
    
    # Test AssignmentStored2
    def testAssignmentStored2(self):
        with self.api.get_connection(autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("USE test")
                cur.execute("SELECT * FROM assignments WHERE name = 'WW Assignment 8'")
                self.assertEqual(datetime.datetime(2024, 12, 11, 23, 59, 59), cur.fetchone()[2])

    # Test AssignmentStored3
    def testAssignmentStored3(self):
        with self.api.get_connection(autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("USE test")
                cur.execute("SELECT * FROM assignments WHERE name = 'Exam Writing Prep \#2'")
                self.assertEqual(datetime.datetime(2024, 11, 28, 23, 59, 59), cur.fetchone()[2])
    
    # Test NoDuplicates
    def testNoDuplicates(self):
        self.api.UserAssignmentView()
        with self.api.get_connection(autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("USE test")
                cur.execute("SELECT * FROM assignments WHERE name = 'Exam Writing Prep \#2' AND user_id = 3")
                self.assertEqual(datetime.datetime(2024, 11, 28, 23, 59, 59), cur.fetchone()[2])
                self.assertEqual(None, cur.fetchone()) 

if __name__ == '__main__':
    unittest.main()