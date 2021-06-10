#-*-coding:utf-8-*-
# 写一个测试类 对自己写的math_method模块里面的类  进行单元测试
# ps：模块名以test开头。类以Test开头。方法以test开头
import unittest
from class_1118_unittest.math_method import MathMethod


class TestMathMethod(unittest.TestCase):  # 继承unittest里面的TestCase 来写用例
    # 编写测试用例
    # 一个用例就是一个函数，不能传参  只有self关键字
    # 所有的用例（函数）都是test开头:test_
    def setUp(self):  # 重写（父类已有的函数，子类又写了一遍）
        print("**********开始执行用例**********")

    def test_add_two_positive(self):  # 两个正数相加的值
        res = MathMethod(1, 2).add()
        print("1+2的值：", res)
        # 加一个断言：判断期望值与实际结果的比对结果，一致就算通过，不一致就算失败
        try:  # 抓取错误  异常处理
            self.assertEqual(3, res)  # 断言
        except AssertionError as e:
            print("出错了，断言错误是{0}".format(e))
            raise e  # 异常处理之后需要抛出去

    def test_add_two_zero(self):  # 两个0相加的值
        res = MathMethod(0, 0).add()
        print("0+0的值：", res)
        try:
            self.assertEqual(1, res, "两个0相加出错了")  # 断言里面msg在用例执行失败的时候才会显示
        except AssertionError as e:
            print("断言错误是{}".format(e))
            raise AssertionError

    def test_add_two_negative(self):  # 两个负数相加的值
        res = MathMethod(int(-1), int(-2)).add()
        print("-1+-2的值：", res)
        try:
            self.assertEqual(-3, res)
        except AssertionError as e:
            print("出错了，断言错误是{0}".format(e))
            raise e  # 异常处理之后需要抛出去,否则不会显示这条用例失败

    def tearDown(self):  # 重写
        print("*********用例执行结束**********")

# setUp、tearDown 函数可写可不写（夹心饼干）
# setUp 执行每一条用例之前先执行setUp # tearDown 每一条用例执行完毕之后执行tearDown
# 如果有操作必须在执行用例之前准备好，那就放到setUp里。
# 如果有操作必须在执行用例之后清除掉，那就放到tearDown里。


class TestMulti(unittest.TestCase):  # 继承unittest里面的TestCase 来写用例
    # 编写测试用例
    # 一个用例就是一个函数，不能传参  只有self关键字
    # 所有的用例（函数）都是test开头:test_
    def test_multi_two_positive(self):  # 两个正数相乘的值
        res = MathMethod(1, 2).multi()
        print("1*2的值：", res)

    def test_multi_two_zero(self):  # 两个0相乘的值
        res = MathMethod(0, 0).multi()
        print("0*0的值：", res)

    def test_multi_two_negative(self):  # 两个负数相乘的值
        res = MathMethod(-1, -2).multi()
        print("-1*-2的值：", res)

if __name__ == '__main__':
    unittest.main()  # 加载所有用例


# positive
# zero
# negative


