import pytest
from common import user
import json

@pytest.mark.usefixtures("setup_db")
def test_init_user(setup_db):
    conn = setup_db
    usr = user.User.from_email(conn,'notreal@yahoo.com')
    assert usr is None

    #Now test a real user in the test data system
    test_email = 'user1@example.com'
    usr = user.User.from_email(conn,test_email)
    assert usr is not None
    assert usr.first_name =='John'
    assert usr.user_id ==1
    dusr = usr.to_dict()
    assert dusr['email']==test_email
    assert dusr['firstName']=='John'
    assert dusr["userId"] ==1
    jdusr = usr.to_json()
    assert json.loads(jdusr)==dusr