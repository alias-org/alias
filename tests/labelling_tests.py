from nose.tools import *
from unittest import TestCase
import alias
from ast import literal_eval

class LabellingCreationTests(TestCase):

    def test_blank_labelling_creation(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_blank_labelling()
        assert isinstance(l,alias.Labelling)
        assert set(['a','b','c','d']).issubset(l.undefargs)

    def test_allin_labelling_creation(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_all_in()
        assert set(['a','b','c','d']).issubset(l.inargs)

    def test_allout_labelling_creation(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_all_out()
        assert set(['a','b','c','d']).issubset(l.outargs)

    def test_allundec_labelling_creation(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'), ('c','d')])
        l = af.generate_all_undec()
        assert set(['a','b','c','d']).issubset(l.undecargs)

class LabellingSemanticTests(TestCase):

    def test_complete_labelling(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        l = af.generate_all_undec()
        n = af.generate_all_undec()
        o = af.generate_all_out()
        n.label_in('a')
        n.label_out('b')
        o.label_in('b')
        o.label_in('d')
        completes = alias.labelling_complete(af)
        lexists = False
        nexists = False
        oexists = False
        for m in completes:
            if l == m:
                lexists = True
            if n == m:
                nexists = True
            if o == m:
                oexists = True
        assert (lexists & nexists & oexists)

    def test_grounded_labelling(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        l = af.generate_all_undec()
        grounded = alias.labelling_grounded(af)
        assert grounded == l

    def test_preferred_labelling(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        preferred = alias.labelling_preferred(af)
        l = af.generate_all_undec()
        n = af.generate_all_undec()
        o = af.generate_all_out()
        n.label_in('a')
        n.label_out('b')
        o.label_in('b')
        o.label_in('d')
        lexists = False
        nexists = False
        oexists = False
        for m in preferred:
            if l == m:
                lexists = True
            if n == m:
                nexists = True
            if o == m:
                oexists = True

        assert ((not lexists) & nexists & oexists)


    def test_stable_labelling(self):
        af = alias.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        preferred = alias.labelling_stable(af)
        l = af.generate_all_undec()
        n = af.generate_all_undec()
        o = af.generate_all_out()
        n.label_in('a')
        n.label_out('b')
        o.label_in('b')
        o.label_in('d')
        lexists = False
        nexists = False
        oexists = False
        for m in preferred:
            if l == m:
                lexists = True
            if n == m:
                nexists = True
            if o == m:
                oexists = True

        assert ((not lexists) & (not nexists) & oexists)
