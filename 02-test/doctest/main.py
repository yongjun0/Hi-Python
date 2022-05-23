#https://stackoverflow.com/questions/67379623/doctest-multiple-files-from-one-file
import doctest
import importlib.util

# from link

def import_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

'''
'''

if __name__ == "__main__":
    test_modules = [

        #("module_name", "path+file_name")
        ("this_is_my_module_name", "/Users/yongjunchoi/Research/coding/Python/doctest/vowels.py")
        ("main.B", "./coulomb.py")
    ]
    
    for name, path in test_modules:
        doctest.testmod(import_module(name, path)) # from document


