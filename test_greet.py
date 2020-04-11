from greet import greet

def test_req1():
    assert(greet("Bob") == "Hello, Bob.")

def test_req2():
    assert(greet(None) == "Hello, my friend.")

def test_req3():
    assert(greet("JERRY") == "HELLO JERRY.")

def test_req4():
    assert(greet(["Jill", "Jane"]) == "Hello, Jill and Jane.")

def test_req5():
    assert(greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte.")

def test_req6():
    assert(greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!")

def test_req7():
    assert(greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne.")

def test_req8():
    assert(greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne.")
