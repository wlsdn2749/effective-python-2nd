# 코드에 있는 계산을 여러 CPU 코어가 병렬로 실행할 수 있는 독립적인 작업 단위로 나눈다

# concurrent.futures 내장 모듈의 multiprocessing 내장 모듈은 
# 자식 프로세스로 다른 파이썬 인터프리터를 실행시킴으로써 파이썬에서 여러 CPU 코어를 사용할 수 있게 만들어준다

# 자식 프로세스는 주 인터프리터와 별도로 실행되기 때문에 주 인터프리터의 GIL과 분리된다

# mymodule.py

# parallel.. Thread말고 ProcessPool

import my_module
from concurrent.futures import ProcessPoolExecutor
import time

NUMBERS = [
    (1963309, 2265973), (2030677, 3814172),
    (1551645, 2229620), (2039045, 2020802),
    (1823712, 1924928), (2293129, 1020491),
    (1281238, 2273782), (3823812, 4237281),
    (3812741, 4729139), (1292391, 2123811),
]

def main():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=2) # 스레드 풀을 시작하고 통신 비용이 들기 때문에 이전보다 더 느려짐
    results = list(map(my_module.gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'총 {delta:.3f}초 걸림')
    
if __name__ == '__main__':
    main()