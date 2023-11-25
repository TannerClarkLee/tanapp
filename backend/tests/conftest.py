import pytest
from common import db

def create_test_data():
    pass

@pytest.fixture
def setup_db():
    db_conn = db.init(True)
    create_test_data()
    yield db_conn
    db_conn.close()