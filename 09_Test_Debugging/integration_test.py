from unittest import TestCase, main

def setUpModule():
    print('* 모듈 설정')
    
def tearDownModule():
    print('* 모듈 정리')
    
class IntegrationTest(TestCase):
    def setUp(self):
        print('* 테스트 설정')
        
    def tearDown(self):
        print('* 테스트 정리')
        
    def test_end_to_end1(self):
        print("* 테스트 1") # 테스트 할때 setUp과 testDown이 불러와진다
    
    def test_end_to_end2(self):
        print("* 테스트 2") # 테스트 할때 setUp과 testDown이 불러와진다
        
if __name__ == '__main__':
    main() # setUpModule과 tearDownModule은 한 번만 호출됨.