# Selenium2 + Unittest + Jenkins测试



*  :white_check_mark:  Selenium2 
*  :white_check_mark:  Unittest 
*  ✅  Python2
*  :white_check_mark:  HTMLTestRunner
*  ✅  Jenkins
*  ✅  Xpath



# 一、测试架构介绍

```
.
├── READ.md
├── __init__.py	
├── common_lib					公共基础类
│   ├── __init__.py
│   └── common.py
├── pic							截屏文件保存路径
├── report						测试报告路径
├── run_test.py					测试用例执行主文件
└── test_case
    ├── library_suit			测试用例套件 library
    │   ├── __init__.py
    │   └── __init__.pyc
    └── search_suit				测试用例套件 search
        ├── __init__.py
        ├── __init__.pyc
        ├── login.py			测试用例
        ├── login.pyc
        ├── test_isbn.py
        └── test_isbn.pyc
```



## 二、unittest 介绍

setUp() 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用

tearDown() 方法在每个测试方法执行后调用

unitest.main() 函数用来测试类中以 test 开头的测试用例



### 测试套件使用方法

#### 使用方法一：通过测试套件执行测试用例

```
# 构造测试集
suite = unittest.TestSuite() 
suite.addTest(Search("login")) 
suite.addTest(Search("testResize"))
# 执行测试
runner = unittest.TextTestRunner() 
runner.run(suite)
```



#### 方法二：unittest 提供一种简单的方法，可以通过文件的名称来判断是否为测试用例文件，将用例文件自动添加到测试套件中

```
def createsuite():
	# 定义一个函数批量添加测试用例
    testunit = unittest.TestSuite()
    
    # discover 方法定义
    # test_path：要测试的模块名或测试用例目录
    # pattern = "*.py"：表示用例文件名的匹配原则。星号“*”表示任意多个字符
    # top_level_dir=None:测试模块的顶层目录。如果没顶层目录(也就是说测试用例不是放在多级目录 中)，默认为 None
    discover = unittest.defaultTestLoader.discover(test_path, pattern = "*.py", top_level_dir=None)

	# discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit
    
# 调用函数
all_tests_name = createsuite()
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = u'图书管理系统测试报告',
    description = u'用例执行情况：'
)

# 执行测试用例套件
runner.run(all_tests_name)
```

​	


# 测试用例集

​		

# 测试报告截图





# Jenkins





# 附件

​		
​		
​	

