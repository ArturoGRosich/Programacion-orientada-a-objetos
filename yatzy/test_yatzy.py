import pytest
from Yatzy import Yatzy

def test_chance():
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 1, 2)

def test_single_numbers():
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 2 == Yatzy.ones(1, 1, 3, 4, 5)
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
    assert 0 == Yatzy.threes(1, 1, 1, 4, 5)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)
    assert 0 == Yatzy.fours(1, 2, 1, 1, 3)
    assert 4 == Yatzy.fours(1, 2, 3, 4, 5)
    assert 0 == Yatzy.fives(1, 2, 1, 1, 3)
    assert 20 == Yatzy.fives(5, 5, 5, 5, 3)
    assert 0 == Yatzy.sixes(1, 2, 1, 1, 3)
    assert 12 == Yatzy.sixes(6, 2, 1, 1, 6)

def test_pairs():
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(3, 2, 5, 4, 1)

def test_two_pairs():
    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)

def test_three():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 2, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)

def test_poker():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)    
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)    

def test_straights():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)

def test_full_house():
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 7 == Yatzy.fullHouse(1, 1, 1, 2, 2)  
    assert 0 == Yatzy.fullHouse(1, 1, 2, 2, 3)  
    assert 0 == Yatzy.fullHouse(1, 2, 2, 2, 2)