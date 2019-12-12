"""Test for Boba_Bot_Functions"""

from Boba_Bot_Functions import *

def test_check_wallet():
    """Tests check_wallet function in few cases"""
    assert check_wallet(15, 9.17) == 'Great! You have enough money.'
    assert isinstance(check_wallet(15, 9.17), str)
    assert callable(check_wallet)
    
def test_need_straw(): 
    """Tests need_straw function in few cases"""
    assert check_wallet(int) == 'Invalid response.'
    assert isinstance(need_straw(msg), str)
    assert callable(need_straw)