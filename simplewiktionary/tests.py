try:
    from .code import SimpleWiktionary
except ImportError:
    from code import SimpleWiktionary

import unittest


class FullTest(unittest.TestCase):

    def test_1(self):
        SCRAP_ITEMS = 100

        s = SimpleWiktionary()
        result = []
        for item in  s.get_list_of_defined_words(SCRAP_ITEMS):
            result.append(item)

        self.assertEqual(len(result), SCRAP_ITEMS)
        self.assertEqual(len(s.get_current_list_of_words()), SCRAP_ITEMS)

        for item in  s.get_list_of_defined_words(SCRAP_ITEMS + 4):
            result.append(item)

        self.assertEqual(len(result), SCRAP_ITEMS + 4)
        self.assertEqual(len(s.get_current_list_of_words()), SCRAP_ITEMS + 4)

        result = s.define('black')
        self.assertGreater(len(result), 0)

        result = s.define('lol')
        self.assertGreater(len(result), 0)

        result = s.define('KOLLK:LSMSALMS')
        self.assertEquals(len(result), 0)


if __name__ == '__main__':
    unittest.main()

