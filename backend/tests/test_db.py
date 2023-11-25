from common import db
import pytest

def test_setup():
    db_conn = db.init(True)
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(1) FROM users;")
    rows = cursor.fetchall()
    if len(rows)==0:
        raise Exception("Should have one row when getting count from empty table")
    if rows[0][0]!=0:
        raise Exception("users should be empty on init in testing")
    
@pytest.mark.usefixtures("setup_db")
def test_setup_fixtures(setup_db):
    cursor = setup_db.cursor()
    cursor.execute("SELECT COUNT(1) FROM users;")
    rows = cursor.fetchall()    
    if len(rows)==0:
        raise Exception("Should have one row when getting count from empty table")
    if rows[0][0]!=0:
        raise Exception("users should be empty on init in testing")
    