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
        pass