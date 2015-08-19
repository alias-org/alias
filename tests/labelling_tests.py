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

    def test_admissible_labelling(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','c'),('c','d'),('d','c')])
        admissible = al.labelling_admissible(af)
        l = af.generate_all_undec()
        n = af.generate_all_undec()
        o = af.generate_all_out()
        p = af.generate_all_undec()
        q = af.generate_all_undec()
        r = af.generate_all_undec()
        s = af.generate_all_undec()
        n.label_in('d')
        n.label_out('c')
        o.label_in('a')
        p.label_in('a')
        p.label_in('d')
        p.label_out('c')
        q.label_in('a')
        q.label_out('b')
        r.label_in('a')
        r.label_in('c')
        r.label_out('b')
        r.label_out('d')
        s.label_in('a')
        s.label_in('d')
        s.label_out('b')
        s.label_out('c')
        lexists = False
        nexists = False
        oexists = False
        pexists = False
        qexists = False
        rexists = False
        sexists = False
        for m in admissible:
            if l == m:
                lexists = True
            if n == m:
                nexists = True
            if o == m:
                oexists = True
            if p == m:
                pexists = True
            if q == m:
                qexists = True
            if r == m:
                rexists = True
            if s == m:
                sexists = True

        assert (lexists & nexists & oexists & pexists & qexists & rexists & sexists)

    def test_complete_labelling(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        l = af.generate_all_undec()
        n = af.generate_all_undec()
        o = af.generate_all_out()
        n.label_in('a')
        n.label_out('b')
        o.label_in('b')
        o.label_in('d')
        completes = al.labelling_complete(af)
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
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        l = af.generate_all_undec()
        grounded = al.labelling_grounded(af)
        assert grounded == l

    def test_preferred_labelling(self):
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        preferred = al.labelling_preferred(af)
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
        af = al.ArgumentationFramework()
        af.add_attack(atts=[('a','b'), ('b','a'), ('b','c'),('c','d'),('d','e'),('e','c')])
        preferred = al.labelling_stable(af)
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