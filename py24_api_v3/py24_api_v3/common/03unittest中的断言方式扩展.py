"""
============================
Author:柠檬班-木森
Time:2019/12/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest


class TestLogin(unittest.TestCase):

    def test_login_pass(self):
        # expected = {"code": 1, "msg": "python"}
        #
        # res = {"code": 0, "msg": "dfghjkl;'fghjklpython--342343232423sfghuiop["}
        # 断言两个数据是否相等   xx == xxx
        # self.assertEqual(expected["code"],res["code"])
        # 断言两个数据不相等    xx != xxx
        # self.assertNotEqual(expected["code"],res["code"])

        # 成员断言---》  x in XXX
        # self.assertIn(expected["msg"],res["msg"])
        # 非成员断言 - --》  x not in XXX
        # self.assertNotIn(expected["msg"], res["msg"])

        # 布尔值断言
        # self.assertTrue("123")
        # self.assertFalse("")

        # 身份断言（判断是否是同一个对象）
        # li = [1, 2, 3]
        # li2 = li
        # li3 = [1, 2, 3]
        # print(id(li),id(li2),id(li3))

        # self.assertIs(li, li3)
        # self.assertIsNot(li,li3)

        # 断言是否为None
        self.assertIsNone(None)
