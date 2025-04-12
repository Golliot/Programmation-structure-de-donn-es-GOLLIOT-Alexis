import unittest
from seance3 import Tree

class TestTree(unittest.TestCase):
    
    def test_label(self):
        T=Tree('f',Tree('a'),Tree('b'))
        self.assertEqual(T.label(),'f')

    def test_nb_children(self):
        T1=Tree('b',Tree('c'),Tree('d'))
        T=Tree('a',Tree('f'),T1)
        self.assertEqual(T.nb_children(),2)
    
    def test_is_leaf(self):
        T1=Tree('b',Tree('c'),Tree('d'))
        T=Tree('a',Tree('f'),T1)
        self.assertEqual(T.child(1).is_leaf(),False)
        
    def test_child(self):
        tb=Tree('b')
        t=Tree('a',tb)
        self.assertEqual(t.child(0),tb)
    
    def test_str(self):
        T1=Tree('b',Tree('c'),Tree('d'))
        T2=Tree('e',Tree('f'),Tree('g'))
        T=Tree('a',T1,T2)
        self.assertEqual(str(T),'a(b(c,d),e(f,g))')

if __name__ == '__main__':
    unittest.main()