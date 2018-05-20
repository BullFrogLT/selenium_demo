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
suite.addTest(Search("test_createuser_search")) 
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

# 测试报告截图





# Jenkins





# 附件

​		

## :white_check_mark:  浏览器属性，调用说明：

driver.属性值

| **属性**                                   | 变量说明                                     |
| ---------------------------------------- | ---------------------------------------- |
| driver.current_url                       | 获得当前页面的URL                               |
| driver.page_source                       | 获取页面html源代码                              |
| driver.title                             | 获取当前页面的标题                                |
| driver.current_window_handle             | 获取当前窗口句柄                                 |
| driver.window_handles                    | 获取所有窗口句柄                                 |
|                                          | **函数说明**                                 |
| driver.find_element*()                   | 定位元素                                     |
| driver.get(url)                          | 浏览器加载url                                 |
| driver.forward()                         | 浏览器向前                                    |
| driver.back()                            | 浏览器向前                                    |
| driver.refresh()                         | 浏览器刷新                                    |
| driver.close()                           | 关闭当前窗口 ，或最后打开的窗口                         |
| driver.quit()                            | 关闭所有关联窗口，并且安全关闭session                   |
| driver.maximize_window()                 | 最大化浏览器窗口                                 |
| driver.set_window_size(宽，高)              | 设置浏览器窗口大小                                |
| driver.get_window_size()                 | 获取当前窗口的长和宽                               |
| driver.get_window_position()             | 获取当前窗口坐标                                 |
| driver.get_screenshot_as_file(filename)  | 截取当前窗口                                   |
| driver.implicitly_wait(秒)                | 隐式等待，通过一定的时长等待页面上某一元素加载完成。若提前定位到元素，则继续执行。若超过时间未加载出，则抛出NoSuchElementException异常 |
| driver.switch_to_frame(id或name属性值)       | 切换到新表单(同一窗口)。若无id或属性值，可先通过xpath定位到iframe，再将值传给switch_to_frame() |
| driver.switch_to.parent_content()        | 跳出当前一级表单。该方法默认对应于离它最近的switch_to.frame()方法 |
| driver.switch_to.default_content()       | 跳回最外层的页面                                 |
| driver.switch_to_window(窗口句柄)            | 切换到新窗口                                   |
| driver.switch_to.window(窗口句柄)            | 切换到新窗口                                   |
| driver.switch_to_alert()                 | 警告框处理。处理JavaScript所生成的alert,confirm,prompt |
| driver.switch_to.alert()                 | 警告框处理                                    |
| driver.execute_script(js)                | 调用js                                     |
| driver.get_cookies()                     | 获取当前会话所有cookie信息                         |
| driver.get_cookie(cookie_name)           | 返回字典的key为“cookie_name”的cookie信息 。 实例：driver.get_cookie("NET_SessionId") |
| driver.add_cookie(cookie_dict)           | 添加cookie。“cookie_dict”指字典对象，必须有name和value值 |
| driver.delete_cookie(name,optionsString) | 删除cookie信息                               |
| driver.delete_all_cookies()              | 删除所有cookie信息                             |
|                                          |                                          |

> 1. 显示等待
>
>    显示等待是一种条件出发式的等待方式，指定某一条件直到整个条件成立时才会继续执行，可以设置超时时间，如果超过这个时间元素依然没被加载，就会抛出异常
>
>    ```
>    from selenium.webdriver.support.ui import WebDriverWait
>    from selenium.webdriver.support import expected_conditions as EC
>    try:
>    	# 默认 500ms 检测一次元素是否存在
>        element = WebDriverWait(driver, 10).until(
>        	EC.presence_of_element_located((BY.ID, "元素"))
>        )
>    finally:
>    	driver.quit()
>    ```
>
>    | 内置方法                                   | 说明                                       |
>    | -------------------------------------- | ---------------------------------------- |
>    | title_is                               | 判断当前页面的 title 是否等于预期内容                   |
>    | title_contains                         | 判断当前页面的 title 是否包含预期字符串                  |
>    | presence_of_element_located            | 判断某个元素是否被加到了 dom 树里，并不代表元素一定可见           |
>    | visibility_of_element_located          | 判断某个元素是否可见                               |
>    | presence_of_all_elements_located       | 判断是否至少有1个元素存在于 dom 树种                    |
>    | text_tobe_present_in_element           | 判断某个元素中的 text 是否包含了预期的字符串                |
>    | text_tobe_present_in_element_value     | 判断某个元素中的 value 属性是否包含了预期的字符串             |
>    | frame_to_be_available_and_switch_to_it | 判断该 frmae 是否可以切换进去，如果可以的话，返回 True 并且切换进去，否则返回 False |
>    | invisibility_of_element_located        | 判断某个元素中是否不存在于 dom 树或不可见                  |
>    | element_to_be_clickable                | 判断某个元素中是否可见并且是 enable 的                  |
>    | staleness_of                           | 等待某个元素从 dom 树种移除                         |
>    | element_to_be_selected                 | 判断某个元素是否被选中了，一般用于下拉列表                    |
>    | element_located_to_be_selected         | 判断某个元素是否被选中了，一般用于下拉列表                    |
>    | element_selection_state_to_be          | 判断某个元素的选中状态是否符合预期                        |
>    | element_located_selection_state_to_be  | 判断某个元素的选中状态是否符合预期                        |
>    | alert_is_present                       | 判断页面上是否存在 alert 框                        |
>
>    ​
>
>
> 2. 隐式等待
>
>    隐式等待是在尝试发现某个元素的时候，如果没能立刻发现，就等待固定长度的时间，类似于 socket 超时，默认设置是0秒，一旦设置了隐式等待时间，它的作用范围是 Webdriver 对象实例的整个生命周期。



## :white_check_mark:  页面元素属性，调用说明：

driver.find_element*.属性值

或

element=driver.find_element*

element.属性值

| 属性                          | 变量说明                      |
| --------------------------- | ------------------------- |
| element.size                | 获取元素的尺寸                   |
| element.text                | 获取元素的文本                   |
| element.tag_name            | 获取标签名称                    |
|                             | **函数说明**                  |
| element.clear()             | 清除文本                      |
| element.send_keys(value)    | 输入文字或键盘按键（需导入Keys模块）      |
| element.click()             | 单击元素                      |
| element.get_attribute(name) | 获得属性值                     |
| element.is_displayed()      | 返回元素结果是否可见（True 或 False）  |
| element.is_selected()       | 返回元素结果是否被选中（True 或 False） |
| element.find_element*()     | 定位元素，用于二次定位               |
|                             |                           |


## :white_check_mark: 鼠标事件  

|                    | 说明                                       |
| ------------------ | ---------------------------------------- |
| context_click()    | 右击，需要用到ActionChains类，例如:ActionChains(driver).double_click(double).perform() |
| double_click()     | 双击                                       |
| drag_and_drop() 拖动 | 拖动，例如:ActionChains(driver).drag_and_drop(原始位置,   目标位置).perform() |
| move_to_element()  | 鼠标悬停在一个元素上                               |
| lick_and_hold()    | 按下鼠标左键在一个元素上                             |
|                    |                                          |
|                    |                                          |
|                    |                                          |
|                    |                                          |
|                    |                                          |


## :white_check_mark:  键盘事件

|                             | 说明                        |
| --------------------------- | ------------------------- |
| send_keys(Keys.BACK_SPACE)  | 删除键(BackSpace)，需要导入Keys 包 |
| send_keys(Keys.SPACE)       | 空格键(Space)                |
| send_keys(Keys.TAB)         | 制表键(Tab)                  |
| send_keys(Keys.ESCAPE)      | 回退键(Esc)                  |
| send_keys(Keys.ENTER)       | 回车键(Enter)                |
| send_keys(Keys.CONTROL,'a') | 全选(Ctrl+A)                |
| send_keys(Keys.CONTROL,'c') | 复制(Ctrl+C)                |
| send_keys(Keys.CONTROL,'x') | 剪切(Ctrl+X)                |
| send_keys(Keys.CONTROL,'v') | 粘贴(Ctrl+V)                |

