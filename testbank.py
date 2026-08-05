from bank import value


def test_capital():
    assert value("HELLO")==0
    assert value("H")==20
def test_lower():
    assert value("hello")==0
    assert value("h")==20
def test_num():
    assert value("77hjh")==100
def test_sign():
    assert value("+u*&un")==100
def test_phrase():
    assert value("I am ok ")==100
    assert value("i am ok")==100
def test_hello_phrase():
    assert value("hello, Newman") == 0
def test_phrase():
    assert value("What's happening?") == 100
    assert value("Good morning") == 100



