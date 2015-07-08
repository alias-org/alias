from nose.tools import *
from unittest import TestCase
import alias as al
import os

class ApxTests(TestCase):

    @classmethod
    def setup_class(klass):
        """CLASS_SETUP"""

    @classmethod
    def teardown_class(klass):
        """CLASS_TEARDOWN"""
        dirpath = "tests/test_files/out"
        filelist = os.listdir(dirpath)
        for f in filelist:
            os.remove(dirpath + '/' + f)

    def setup(self):
        """METHOD_SETUP"""

    def teardown(self):
        """METHOD_TEARDOWN"""

    def test_apx_read(self):
        af = al.read_apx('tests/test_files/in/test_apx.apx')
        assert set(['a','b','c','d']).issubset(af.get_arguments())
        assert set([('a','b'),('d','c'),('c','b')]).issubset(af.get_attacks())

    def test_apx_write(self):
        afwrite = al.ArgumentationFramework()
        afwrite.add_argument(['a','b','c','d'])
        afwrite.add_attack('a','b')
        afwrite.add_attack('d','c')
        afwrite.add_attack('c','b')
        al.write_apx(afwrite, 'tests/test_files/out/test_apx.apx')
        afread = al.read_apx('tests/test_files/out/test_apx.apx')
        assert set(['a','b','c','d']).issubset(afread.get_arguments())
        assert set([('a','b'),('d','c'),('c','b')]).issubset(afread.get_attacks())


class TgfTests(TestCase):

    @classmethod
    def setup_class(klass):
        """CSETUP"""

    @classmethod
    def teardown_class(klass):
        """CTEARDOWN"""
        dirpath = "tests/test_files/out"
        filelist = os.listdir(dirpath)
        for f in filelist:
            os.remove(dirpath + '/' + f)

    def setup(self):
        """MSETUP"""

    def teardown(self):
        """MTEARDOWN"""

    def test_tgf_read(self):
        af = al.read_tgf('tests/test_files/in/test_tgf.tgf')
        assert set(['a','b','c','d']).issubset(af.get_arguments())
        assert set([('a','b'),('d','c'),('c','b')]).issubset(af.get_attacks())

    def test_tgf_write(self):
        afwrite = al.ArgumentationFramework()
        afwrite.add_argument(['a','b','c','d'])
        afwrite.add_attack('a','b')
        afwrite.add_attack('d','c')
        afwrite.add_attack('c','b')
        al.write_tgf(afwrite, 'tests/test_files/out/test_tgf.tgf')
        afread = al.read_tgf('tests/test_files/out/test_tgf.tgf')
        assert set(['a','b','c','d']).issubset(afread.get_arguments())
        assert set([('a','b'),('d','c'),('c','b')]).issubset(afread.get_attacks())

class DotTests(TestCase):

    @classmethod
    def setup_class(klass):
        """CSETUP"""

    @classmethod
    def teardown_class(klass):
        """CTEARDOWN"""
        dirpath = "tests/test_files/out"
        filelist = os.listdir(dirpath)
        for f in filelist:
            os.remove(dirpath + '/' + f)

    def setup(self):
        """MSETUP"""

    def teardown(self):
        """MTEARDOWN"""

    def test_dot_read(self):
        af = al.read_dot('tests/test_files/in/test_dot.dot')
        assert set(['a','b','c','d']).issubset(af.get_arguments())
        assert set([('a','b'), ('b','c'),('b','d')]).issubset(af.get_attacks())

    def test_dot_write(self):
        afwrite = al.ArgumentationFramework()
        afwrite.add_argument(['a','b','c','d'])
        afwrite.add_attack('a','b')
        afwrite.add_attack('b','c')
        afwrite.add_attack('b','d')
        al.write_tgf(afwrite, 'tests/test_files/out/test_tgf.tgf')
        afread = al.read_tgf('tests/test_files/out/test_tgf.tgf')
        assert set(['a','b','c','d']).issubset(afread.get_arguments())
        assert set([('a','b'), ('b','c'),('b','d')]).issubset(afread.get_attacks())
