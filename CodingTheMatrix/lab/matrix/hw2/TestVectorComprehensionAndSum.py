import sys
sys.path.append('E:\\personal\\programming\\learning\\CodingTheMatrix\\lab\\matrix')

from hw2 import vec_select, vec_sum, vec_select_sum, scale_vecs
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

    def test_vec_select_sum_for_empty_list_of_vectors(self):
        __domain = {'a', 'b', 'c', 'd'}
        veclist = list()
        self.assertTrue(vec_sum(veclist, __domain) == Vec(__domain,{}))

    def test_vec_select_sum_of_zero_vectors(self):
        __domain = {'a', 'b', 'c', 'd'}
        veclist = [Vec(__domain,{}), Vec(__domain, {})]
        self.assertTrue(vec_sum(veclist, __domain) == Vec(__domain,{}))

    def test_vec_select_sum_of_zero_vectors(self):
    	# veclist = [Vec({'a', 'b', 'c', 'd'}, {'a': 2, 'b': 3, 'c':1}), Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': 1}), Vec({'a', 'b', 'c', 'd'}, {'c': 5})]
        __domain = {'a', 'b', 'c', 'd'}
        v1 = Vec(__domain, {'a': 1})
        v2 = Vec(__domain, {'a': 0, 'b': 1})
        v3 = Vec(__domain, {        'b': 2})
        v4 = Vec(__domain, {'a': 10, 'b': 10})

        veclist = [v1, v2, v3, v4]
        self.assertTrue(vec_sum(veclist, __domain) == Vec(__domain, {'b': 13, 'a': 11}))


    def test_vec_select_sum_of_zero_vectors(self):
    	# veclist = [, Vec({'a', 'b', 'c', 'd'}, {'a': 3, 'c': 1}), Vec({'a', 'b', 'c', 'd'}, {'c': 5})]
        __domain = {'a', 'b', 'c', 'd'}
        v1 = Vec(__domain, {'a': 2, 'b': 3, 'c': 1})
        v2 = Vec(__domain, {'a': 3,         'c': 1})
        v3 = Vec(__domain, {                'c': 5})

        veclist = [v1, v2, v3]
        selected1 = vec_select(veclist, 'c')
        selected2 = vec_select(veclist, 'b')
        selected3 = vec_select(veclist, 'd')

        self.assertTrue(vec_sum(selected1, __domain) == Vec(__domain, {}))
        self.assertTrue(vec_sum(selected2, __domain) == Vec(__domain, {'a':3, 'c':6}))
        self.assertTrue(vec_sum(selected1, __domain) == Vec(__domain, {'a':5,'b':3,'c':7}))


    def test_vec_select_sum(self):
    	__domain = {'a', 'b', 'c'}
    	v1 = Vec(__domain, {'a': 1})
    	v2 = Vec(__domain, {'a': 0, 'b': 1})
    	v3 = Vec(__domain, {        'b': 2})
    	v4 = Vec(__domain, {'a': 10, 'b': 10})

    	veclist = [v1, v2, v3, v4]

    	self.assertTrue(vec_select_sum(veclist, 'a', __domain) == Vec(__domain, {'b': 3}))

    def test_scale_vector(self):
    	v1 = Vec({1,2,3}, {2: 9})
    	v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})

    	self.assertTrue(scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})])


if __name__ == '__main__':
	unittest.main()