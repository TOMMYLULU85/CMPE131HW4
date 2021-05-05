import unittest

class TestGraph(unittest.TestCase):
    def test_output(self):
        def printGraph(data):
            out=[]
            for i in data:
                t = []
                out.append(t)
                for x in range(i):
                    print('x',end ='')
                    t.extend('x')
                print()
            return out
        data = [1,2,3]
        output = printGraph(data)
        # x
        # xx
        # xxx
        print(output) # [['x'], ['x', 'x'], ['x', 'x', 'x']]
        self.assertEqual(output,[['x'], ['x', 'x'], ['x', 'x', 'x']])
    
    def test_data(self):
        def printGraph(data):
            out=[]
            for i in data:
                t = []
                out.append(t)
                for x in range(i):
                    print('x',end ='')
                    t.extend('x')
                print()
            return out
        data = [1,2,3]
        output = printGraph(data)
        # x
        # xx
        # xxx
        print(output) # [['x'], ['x', 'x'], ['x', 'x', 'x']]
        self.assertNotEqual(data,[['x'], ['x', 'x'], ['x', 'x', 'x']])
    