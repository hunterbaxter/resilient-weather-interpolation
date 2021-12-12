import pytest
import sys

# from .context import src
# from src.retriever.retriever import get_request_weatherbit

sys.path.append("src/retriever/")

from retriever import get_request_weatherbit


def test_get_request_weatherbit():
    # key = "0e8aeccfa150491880a30ffb53a3e4ba"
    # TODO: Need to implement a correct test with a CI secret for key
    invalid_key = "test_key"
    lat = 51
    lon = -80
    assert True
    with pytest.raises(Exception):
        get_request_weatherbit(key=invalid_key,
                               current=True,
                               lat=lat,
                               lon=lon)
