# --** coding=utf-8 **--
"""
test
"""
import pysnooper


@pysnooper.snoop()
def hello(arg1, arg2):
    """
    test hello
    """
    print('a:{}'.format(arg1))
    plus_arg = arg1 + arg2
    multiple_arg = arg2 * 3
    print(plus_arg)
    print(multiple_arg)


if __name__ == '__main__':
    print('hello stock test')
    hello(1, 2)
    hello('foo', 'bar')
