def test_init(accum):
    assert accum.getCount==0

def test_default_Add(accum):
    accum.add()
    assert accum.getCount==1

def test_adding_Three(accum):
    accum.add(3)
    assert accum.getCount==3

def test_adding_twice(accum):
    accum.add()
    accum.add()
    assert accum.getCount==2        
