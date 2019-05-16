# -*- encoding: utf-8 -*-
'''
@File    :   run.py    
@Contact :   mdengx@126.com
@function:   TODO
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/16 11:05   loudDD      1.0         None
'''

# import lib
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    discovery = unittest.defaultTestLoader.discover("./",pattern="test*.py")
    with open("./result.html","wb") as f:
        runner = HTMLTestRunner(stream=f,title="test report",description="test case result")
        runner.run(discovery)