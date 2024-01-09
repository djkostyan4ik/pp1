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
        self.assertEqual(p1.f(1),False)
        self.assertEqual(p1.f(7),True)
        self.assertEqual(p1.f(80),False)
        self.assertEqual(p1.f(79),True)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(1),10)
        self.assertEqual(p2.f(3),24)
        self.assertEqual(p2.f(6),36)
        self.assertEqual(p2.f(10),52)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("AKJT98765432"),"Q")
        self.assertEqual(p3.f("AKQJT9876532"),"4")

    def test_p4(self):
        import p4
        self.assertEqual(p4.f([55,54,55,55,55]),54)

    def test_p5(self):
        import p5
        self.assertEqual(p5.f([[2,3],[1,0],[3,7],[4,4],[3,3]]),4)
        self.assertEqual(p5.f([[2,3],[1,-5],[3,7],[4,-4],[3,3]]),3)
        self.assertEqual(p5.f([[-2,3],[1,-1],[-3,7],[4,-4],[3,3]]),1)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("A4"),True)
        self.assertEqual(p6.f("abc123"),False)
        self.assertEqual(p6.f("ab123"),True)
        self.assertEqual(p6.f("a123"),True)
        self.assertEqual(p6.f("a12345"),False)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f({"def":1,"de":1,"d:":1},"de"),2)
        self.assertEqual(p7.f({"def":1,"de":1,"d:":1},"d"),3)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
