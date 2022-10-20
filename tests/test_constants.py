import numpy as np

from simple_functions import pi


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi = pi(2)
        assert np.isclose(my_pi, np.pi, atol=1e-12)

    def test_python_version():
        from platform import python_version
        assert python_version() == '3.9.15'
