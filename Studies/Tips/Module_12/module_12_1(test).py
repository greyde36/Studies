import module_12_1 as calk

def test_add():
    if calk.add(1,2)==3:
        print("Test add(a,b) is OK")
    else:
        print("Test add(a,b) is FAIL")

def test_sub():
    if calk.sub(3,2)==1:
        print("Test sub(a,b) is OK")
    else:
        print("Test sub(a,b) is FAIL")

def test_mul():
    if calk.mul(1,2)==2:
        print("Test mul(a,b) is OK")
    else:
        print("Test mul(a,b) is FAIL")

def test_div():
    if calk.div(4,2)==2:
        print("Test div(a,b) is OK")
    else:
        print("Test div(a,b) is FAIL")

test_add()
test_sub()
test_mul()
test_div()