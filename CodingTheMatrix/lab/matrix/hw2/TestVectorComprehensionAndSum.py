import sys
sys.path.append('E:\\personal\\programming\\learning\\CodingTheMatrix\\lab\\matrix')

from hw2 import vec_select
import hw0
import unittest
from vector.vec import Vec

class TestVectorComprehensionAndSum(unittest.TestCase):


    def test_vecselect_is_valid(self):
    	D = {'a','b','c'}
    	v1 = Vec(D, {'a': 1})
    	v2 = Vec(D, {'a': 0, 'b': 1})
    	v3 = Vec(D, {        'b': 2})
    	v4 = Vec(D, {'a': 10, 'b': 10})
    	
    	__got = vec_select([v1, v2, v3, v4], 'a')
    	__expected = [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    	self.assertTrue( __got == __expected, __got)

if __name__ == '__main__':
	unittest.main()