import unittest
import gettext

class TestTranslation(unittest.TestCase):
    def test_english(self):
        gettext.install('solid', localedir='locale')
        self.assertEqual(_('Hello World!'), 'Hello World!')
    def test_german(self):
        de = gettext.translation('solid', localedir='locale', languages=['de'])
        de.install()
        self.assertEqual(_('Hello World!'),'Hallo Welt!')        
