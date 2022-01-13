from bowling import Bowling
import pytest

@pytest.mark.plenos_sueltos
def test_plenos_sueltos():
    assert Bowling("X9-9-9-9-9-9-9-9-9-").calculate_score(), 100
    assert Bowling("X9-X9-9-9-9-9-9-9-").calculate_score(), 110

@pytest.mark.plenos_last_frame
def test_plenos_last_frame():    

    assert Bowling("9-9-9-9-9-9-9-9-9-X9-").calculate_score(), 100

@pytest.mark.plenos_seguidos
def test_plenos_seguidos():
    assert Bowling("XX9-9-9-9-9-9-9-9-").calculate_score(), 120
    assert Bowling("XXX9-9-9-9-9-9-9-").calculate_score(), 141

@pytest.mark.plenos_seguidos_last_frame
def test_plenos_seguidos_last_frame():
    assert Bowling("9-9-9-9-9-9-9-9-9-XXX").calculate_score(), 111
    assert Bowling("XXXXXXXXXXXX").calculate_score(), 300

@pytest.mark.plenos_y_spares
def test_plenos_y_spares():
    assert Bowling("8/549-XX5/53639/9/X").calculate_score(), 149
    assert Bowling("X5/X5/XX5/--5/X5/").calculate_score(), 175