import pytest
import fonctions as f
def test_1( ) :
	assert f.puissance( 2 , 3 ) == 8
	assert f.puissance( 2 , 2 ) == 4
	
	

def test_2():
	assert f.puissance(-2,3) == -8
	assert f.puissance(-2,2) == 4
	assert f.puissance (0,0) == 1
	assert f.puissance (0,3) == 0


def test_3():

	assert f.puissance(1,2) == 1
	assert f.puissance(1,-2) == 1
	assert f.puissance(2,2) == 4
	assert f.puissance(2,-3) == 0.125
	
	
	
def test_func():
  with pytest.raises(ValueError, match="La puissance de 0 ne peut pas être défini par un nombre négatif"):
    f.puissance(0,-3)
