import pytest

import process_data 

def test_process_data () :
    assert (0.1 + 0.2) == pytest.Approx(0.3)