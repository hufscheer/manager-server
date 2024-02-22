import pytest
from django.db import connection
import os

@pytest.fixture
def load_sql_fixture():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'resources/fixture.sql')

    with open(file_path) as f:
        queries = f.read().split(';')
        with connection.cursor() as cursor:
            for query in queries:
                if query:
                    cursor.execute(query)
