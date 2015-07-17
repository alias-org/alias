from nose.tools import *
from unittest import TestCase
import alias as al
from ast import literal_eval

class LabellingCreationTests(TestCase):

    def test_blank_labelling_creation(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_blank_labelling()
        assert isinstance(l,al.Labelling)
        assert set(['a','b','c','d']).issubset(l.undefargs)

    def test_allin_labelling_creation(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_all_in()
        assert set(['a','b','c','d']).issubset(l.inargs)

    def test_allout_labelling_creation(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_all_out()
        assert set(['a','b','c','d']).issubset(l.outargs)

    def test_allundec_labelling_creation(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_all_undec()
        assert set(['a','b','c','d']).issubset(l.undecargs)

class LabellingSemanticTests(TestCase):

    def test_complete_labelling(self):
        pass

    def test_grounded_labelling(self):
        pass

    def test_preferred_labelling(self):
        pass

    def test_stable_labelling(self):
        pass
        

