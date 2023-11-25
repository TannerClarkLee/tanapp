import pytest
from common import db

def create_test_data(conn):
    with open("./tests/test_data/test_data.sql","r") as f:
        insert_stmts = f.read()
        for item in insert_stmts.split(';'):
            conn.execute(item)
            conn.commit()

    

@pytest.fixture
def setup_db():
    conn = db.init(True)
    create_test_data(conn)
    yield conn
    conn.close()