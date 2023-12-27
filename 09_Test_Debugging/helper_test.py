from unittest import TestCase, main

def sum_squares(values):
    cumulative = 0
    for value in values:
        cumulative += value ** 2
        yield cumulative
        
class HelperTestCase(TestCase):
    def verify_complex_case(self, values, excepted):
        except_it = iter(excepted)
        found_it = iter(sum_squares(values))
        test_it = zip(except_it, found_it)
        
        for i, (expect, found) in enumerate(test_it):
            self.assertEqual(
                expect,
                found,
                f'잘못된 인덱스: {i}'
            )
        
        # 두 제너레이터를 모두 소진했는지 검증
        
        try:
            next(except_it)
        except StopIteration:
            pass
        else:
            self.fail('실제보다 예상한 제너레이터가 더 깁니다')
            
            
        try:
            next(found_it)
        except StopIteration:
            pass
        else:
            self.fail('예상한 제너레이터보다 실제가 더 깁니다')
            
    def test_wrong_lengths(self):
        values = [1.1, 2.2, 3.3]
        excepted = [
            1.1 ** 2,
        ]
        self.verify_complex_case(values, excepted)
        
    def test_wrong_results(self):
        values = [1.1, 2.2, 3.3]
        excepted = [
            1.1 ** 2,
            1.1 ** 2 + 2.2 ** 2,
            1.1 ** 2 + 2.2 ** 2, 3.3**2 + 4.4 ** 2,
        ]
        self.verify_complex_case(values, excepted)
        
        
if __name__ == "__main__":
    main()