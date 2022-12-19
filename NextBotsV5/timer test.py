from ursina import *

app=Ursina()

def test_func(item, x=None, y=None):
    print(item, x, y)

test_func('test')
invoke(test_func, 'test', delay=2)
invoke(test_func, 'test1', 1, 2, delay=3)
invoke(test_func, 'test2', x=1, y=2, delay=5)
app.run()