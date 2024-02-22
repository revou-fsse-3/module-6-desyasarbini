import pytest
from app import app
from app.utils.database import db
import os

@pytest.fixture
def test_app():
    """"test application setup"""

    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client