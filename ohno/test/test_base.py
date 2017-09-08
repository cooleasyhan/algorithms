from ohno.base import *

def test_to_list():
    node = get_node(5)
    tmp = to_list(node)
    assert tmp == [0,1,2,3,4]

    node = get_cycle_node(5)
    tmp = to_list(node)
    assert tmp == [0,1,2,3,4,'C']



    