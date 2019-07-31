基于 python + unittest + selenium + ddt+ PageObject 的UI自动化测试项目

# 项目目录
* Cases -- 测试用例集
* Config -- 配置文件
* Content -- 公共方法
* Datas -- 测试数据
* Imgs -- 测试截图
* libs -- 第三方库
* Logs -- 测试日志
* Pages -- 测试页面集
* Reports -- 测试报告集

run为文件执行入口

unittest + ddt 进行测试用例，测试数据的加载启动。

使用PageObject页面分层思想将每个页面的元素定位表达式及所属页面行为统一封装成类，便于快速修改被前端工程师修改了位置的元素位置

使用python代码 调用selenium 库的api通过浏览器驱动WebDriver 操作浏览器，进行web端UI层面的操作

# 整体实现思想：

Pages文件夹内的页面均继承Content.base 文件内的 BasePage 类，该类主要封装了页面通用方法，如：查找元素，获取元素的文本内容。。。

Cases文件夹内的测试类均继承Content.myunittest 文件内的 MyUnittest 类， 该类主要封装了每个测试类所需的通用方法，如：初始化浏览器，初始化
logger对象，页面对象等，使每个测试类只需专注于调用即可

# 尚未完成
* 登陆与投资的逆向用例
* 基于pytest测试框架的的项目重构



