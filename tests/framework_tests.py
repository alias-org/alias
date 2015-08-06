from nose.tools import *
from unittest import TestCase
import alias as al

class FrameworkTests(TestCase):

    @classmethod
    def setup_class(klass):
        """CLASS_SETUP"""

    @classmethod
    def teardown_class(klass):
        """CLASS_TEARDOWN"""

    def setup(self):
        """METHOD_SETUP"""

    def teardown(self):
        """METHOD_TEARDOWN"""

    def test_framework_creation(self):
        af = al.ArgumentationFramework()
        assert isinstance(af, al.ArgumentationFramework)

    def test_argument_addition_single(self):
        af = al.ArgumentationFramework()
        af.add_argument('a')
        af.add_argument('b')
        af.add_argument('c')
        assert 'a' in af.framework
        assert 'b' in af.framework
        assert 'c' in af.framework
        assert set(['a','b','c']).issubset(af.get_arguments())

    def test_argument_addition_list(self):
        af = al.ArgumentationFramework()
        af.add_argument(['a','b','c'])
        assert set(['a','b','c']).issubset(af.get_arguments())

    def test_argument_addition_tuple(self):
        af = al.ArgumentationFramework()
        af.add_argument(('a','b','c'))
        assert set(['a','b','c']).issubset(af.get_arguments())

    def test_arg_obj_retrieval(self):
        af = al.ArgumentationFramework()
        af.add_argument('a')
        assert isinstance(af.get_arg_obj('a'), al.Argument)
        assert (af.get_arg_obj('a').name is 'a')

    def test_att_addition_single(self):
        af = al.ArgumentationFramework()
        af.add_attack(att=('a','b'))
        assert set(['a','b']).issubset(af.get_arguments())
        assert set([('a','b')]).issubset(af.get_attacks())

    def test_att_addition_list(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        assert set(['a','b','c','d']).issubset(af.get_arguments())
        assert set([('a','b'), ('b','c'), ('c','d')]).issubset(af.get_attacks())

    def test_attacking_retrieval(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'),('a','c'),('a','d')])
        assert set(['b','c','d']).issubset(af.get_attacking('a'))

    def test_attacker_retrieval(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'),('b','b'),('c','b')])
        assert set(['a','b','c']).issubset(af.get_attackers('b'))

    def test_existence_check(self):
        af = al.ArgumentationFramework()
        af.add_argument('a')
        assert af.argument_exists('a')

    def test_arg_enumeration(self):
        af = al.ArgumentationFramework()
        af.add_argument(('a','b','c'))
        assert af.num_arguments() is 3

    def test_att_enumeration(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'),('b','b'),('c','b')])
        assert af.num_attacks() is 3

    def test_powerset_creation(self):
        af = al.ArgumentationFramework()
        af.add_argument(['a','b','c'])
        assert set([frozenset(['a', 'c', 'b']), frozenset(['b']), frozenset(['a']), frozenset([]), frozenset(['c', 'b']), frozenset(['a', 'c']), frozenset(['c']), frozenset(['a', 'b'])]).issubset(af.generate_powerset())

    def test_arg_set_attacking(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        assert af.argsP(['a','b']) == set(['b','c'])

    def test_arg_set_attackers(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        assert af.argsM(['b','d']) == set(['a','c'])
        
    def test_arg_set_unattacked(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        assert af.argsU(['a','b']) == set(['a','d'])
        
    def test_arg_set_defending(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        assert af.argsD(['a']) == set(['a','c'])
        
    def test_check_conflict_free(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d'), ('d','c')])
        assert af.is_conflict_free(set(['a','c']))
        assert af.is_conflict_free(set(['a','d']))
        assert af.is_conflict_free(set(['b','d']))

    def test_check_not_conflict_free(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d'), ('d','c')])
        assert not af.is_conflict_free(set(['a','b']))


    def test_check_admissible(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d'), ('d','c')])
        assert af.is_admissible(set(['a','c']))
        assert af.is_admissible(set(['a','d']))

    def test_check_not_admissible(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d'), ('d','c')])
        assert not af.is_admissible(set(['b']))
        assert not af.is_admissible(set(['c']))

    def test_check_complete(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d'), ('d','c')])
        assert af.is_complete(set(['a']))
        assert af.is_complete(set(['a','c']))
        assert af.is_complete(set(['a','d']))

    def test_check_preferred(self):
        pass

    def test_extension_grounded(self):
        pass

    def test_extension_complete(self):
        pass

    def test_extension_preferred(self):
        pass

    def test_extension_stable(self):
        pass

    
