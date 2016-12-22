import unittest
import gettext

class TestTranslation(unittest.TestCase):
    def SetUp(self):
        gettext.install('solid')
    def test_english(self):
        gettext.install('solid')
        print(_('Hello World!'))
    def test_german(self):
        de = gettext.translation('solid', localedir='locale', languages=['de'])
        de.install()
        self.assertEqual(_('Hello World!'),'Hallo Welt!')
