from unittest import TestCase, main
from utils import to_str

class AssertTestCase(TestCase):
    def test_assert_helper(self):
        excepted = 12
        found = 2 * 5
        self.assertEqual(excepted, found)
        
    def test_assert_statement(self):
        excepted = 12
        found = 2*5
        assert excepted == found
        
if __name__ == '__main__':
    main()