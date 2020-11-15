from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Gothons of Planet Percal #25", rv.data)
    assert_in(b"I just wanted to say", rv.data)
    assert_in(b"Hello, World!", rv.data)