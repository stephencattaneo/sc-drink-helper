import json
from io import StringIO
import pathlib
import pytest

from processor.main import Processor

LOCATION = str(pathlib.Path(__file__).parent.resolve())

@pytest.fixture
def input_data():
    with open(LOCATION + '/in_data.txt') as fd:
        yield StringIO(fd.read())

@pytest.fixture
def output_data():
    with open(LOCATION + '/out_data.json') as fd:
        yield json.loads(fd.read())


def test_answer(input_data, output_data):
    proc = Processor(input=input_data)
    proc.run()

    assert proc.output == output_data
