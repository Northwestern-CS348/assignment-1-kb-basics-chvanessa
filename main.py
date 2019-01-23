import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)
        

    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : pyramid3")
        self.assertEqual(str(answer[2]), "?X : pyramid4")
        

    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")

    # def test_assert(self):
    #     file2 = 'statements_kb2.txt'
    #     data = read.read_tokenize(file2)
    #     self.KB2 = KnowledgeBase([], [])
    #     # Checking to make sure fact #1 from kb2.txt was correctly added into the KB
    #     self.KB2.kb_assert(data[0])
    #     self.KB2.kb_assert(data[0]) #try inserting same fact? does it duplicate
    #     print("list of facts:" + str(self.KB2.facts))
    #     # Checking to make sure a rule would not be added to the KB
    #     print("rule" + str(data[8]))
    #     self.KB2.kb_assert(data[8])
    #     print("list of facts (appended)" + str(self.KB2.facts))
    #     #self.assertEqual()
        # for item in data:
        #     if isinstance(item, Fact):
        #         self.KB.kb_assert(item)


if __name__ == '__main__':
    unittest.main()
