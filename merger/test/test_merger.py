from heapq import merge
import json
from io import StringIO
import pathlib
import pytest

from merger.main import Merger

LOCATION = str(pathlib.Path(__file__).parent.resolve())


@pytest.fixture
def expected_out_data():
    with open(LOCATION + '/expected_out_data.json') as fd:
        yield json.load(fd)


def test_answer(expected_out_data):

    merge = Merger(input=LOCATION + '/in_data.json', datapath=LOCATION + '/out_data.json')
    merge.run()

    assert merge.data == expected_out_data
