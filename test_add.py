# -*- encoding: utf-8 -*-
'''
@File    :   test_add.py    
@Contact :   mdengx@126.com
@function:   TODO
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/16 9:53   loudDD      1.0         None
'''

from add import method_a
import unittest

class test_a(unittest.TestCase):

    def setUp(self) -> None:
        self.meth = method_a()

    def test_add1(self):
        result = self.meth.add(2,3)
        self.assertEqual(5,result)

    def test_minus1(self):
        result = self.meth.minux(5,3)
        self.assertEqual(result,2)