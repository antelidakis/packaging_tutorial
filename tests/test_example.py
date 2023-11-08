from example_package_annteli import example

def test_add_one():
    x=2
    out = example.add_one(x)
    assert out==3