import pytest

from identifyneeds.repository import MemRepo


@pytest.fixture()
def conditions():
    return [
        {
        }
    ]


class TestMemRepo():

    def test_init_memrepo(self):
        repo = MemRepo()
