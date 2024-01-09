'''
1. Place this program in same the folder as your programs.
2. To assess your programs, run this program.
3. Your results will be saved to the results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(4,3),"4-3=1")
        self.assertEqual(p1.f(2,7),"2+7=9")

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(8),19)
        self.assertEqual(p2.f(25),97)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("123ab"),False)
        self.assertEqual(p3.f("123a1c"),False)
        self.assertEqual(p3.f("123abc"),True)

    def test_p4(self):
        import p4
        self.assertEqual(p4.f("abcdefghijk"),"a+b-c+d-e+f-g+h-i+j-k")

    def test_p5(self):
        import p5
        self.assertEqual(p5.f(201,211),"202,204,206,208,210")

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("abbcccddddeeeeeffffff","e",5),True)
        self.assertEqual(p6.f("abbcccddddeeeeeffffff","e",6),False)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)