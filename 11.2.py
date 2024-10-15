import sys
from pprint import pprint

class MyClass:
    def __init__(self):
        self.attribute = True

    def func(self):
        print('MyFunction')


def introspection_info(obj):
    dic_info = {}
    dic_info['type_'] = type(obj)
    dic_info['attributes_methods'] = dir(obj)
    dic_info['module'] = sys.modules
    return dic_info

obj = MyClass()

pprint(introspection_info(obj))