#Unit Testing in Python
#assert statement

#Assert Testing
'''
assert 1>0 ->True
assert 1<0 ->AssertionError
'''

#n=0
#assert 1<n,"The condition is false"

'''
x=int(input("Enter a number"))
try:
    assert x>0, "Wrong number"
    print("Yes")
except AssertionError as ae:
    print(ae)

'''

"""
assertEqual(x, y, msg=None)	x == y
assertNotEqual(x,y,msg=None)	x != y
assertTrue(x, msg=None)	bool(x) is True
assertFalse(x, msg=None)	bool(x) is False
assertIs(x, y , msg=None)	x is y
assertIsNot(x, y, msg=None)	x is not y
assertIsNone(x, msg=None)	x is None
assertIsNotNone(x , msg=None)	x is not None
assertIn(x, y, msg=None)	x in y
assertNotIn(x, y, msg=None)	x not in y
assertIsInstance(x, y, msg=None)	isinstance(x, y)
assertNotIsInstance(x, y, msg=None)	not isinstance(x, y)

"""



import unittest
from calc import Calculator

'''
class TestCalc(unittest.TestCase):
    def test_case(self):
        c=Calculator(9,6)
        self.assertEqual(c.get_addition(),15,'The sum is wrong')

'''

'''
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.c=Calculator(9,6)
        self.f=open('Arya.txt','r')
    def tearDown(self):
        self.f.close()

    def test_diff(self):
        c=Calculator(9,6)
        self.assertEqual(c.get_difference(),3,'The difference is wrong')

'''


'''
class TestStrMethods(unittest.TestCase):
    def test_Upper(self):
        self.assertEqual("foo".upper(),"FOO")

    def test_isUpper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s="hello world"
        self.assertEqual(s.split(),["hello","world"])

if __name__=='__main__':
    unittest.main()

'''

#Assignment -1 List Unit Testing

class List:
    def find(self,data):
        index = data.index(4)
        if(index):
            return index
        else:
            return -1

    def insert(self,data):
        data.insert(3,4)
        length=len(data)
        return length

    def extend(self,data):
        a=[7,8,9,10]
        for i in range(len(a)):
            data.append(a[i])
        return data


class Testlistmethods(unittest.TestCase):  
    """
    def test_list_int(self):  
  
       #  Test that it can sum a list of integers  
         
        data = [1, 2, 3,4,5,6]  
        res = List.find(self,data)  
        self.assertEqual(res, 4)  
    
    def test_list_insert(self):
        data=[1,2,3,4,5,6]
        res=List.insert(self,data)
        self.assertEqual(res,6)
    """

    def test_list_extend(self):
        data=[1,2,3,4,5,6]
        res=List.extend(self,data)
        self.assertEqual(res,[1,2,3,4,5,6,7,8,9,10])

    
    """
    def test_bad_type(self):  
        data = "Apple"  
        with self.assertRaises(TypeError):  
            res = sum(data)  
    """
  
if __name__ == '__main__':  
    unittest.main()  

#python3 -m unittest -v mockito.py