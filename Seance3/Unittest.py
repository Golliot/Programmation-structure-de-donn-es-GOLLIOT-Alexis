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

    def test_eq(self):
        T1=Tree('b',Tree('c'),Tree('d'))
        T2=Tree('b',Tree('c'),Tree('d'))
        self.assertEqual(T1,T2)
    
    def test_substitute(self):
        T = Tree('+', Tree('7'), Tree('+', Tree('*', Tree('5'), Tree('X')), Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X')))))
        t1 = Tree('*', Tree('5'), Tree('X'))
        t2 = Tree('b')
        self.assertEqual(T.substitute(t1, t2), Tree('+', Tree('7'), Tree('+', Tree('b'), Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))))))

    def test_evaluate(self):
        #Pol = 7+5X+3X^2
        Pol = Tree('+', Tree('7'), Tree('+', Tree('*', Tree('5'), Tree('X')), Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X')))))
        self.assertEqual([Pol.evaluate(0), Pol.evaluate(5), Pol.evaluate(-3)], [7, 107, 19])

if __name__ == '__main__':
    unittest.main()