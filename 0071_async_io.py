import time
import asyncio

def sleep():
    time.sleep(1)
    
def sum(name, numbers):
    start = time.time()
    total = 0
    
    for n in numbers:
        sleep()
        total += n
        print(f'작업 중={name}, number={n}, total={total}')
        
    end  = time.time()
    print(f'작업명={name}, 걸린시간={end-start}')
    return total

def main():
    start = time.time()
    
    result1 = sum('a', [1,2])
    result2 = sum('b', [1,2,3])
    
    end = time.time()
    print(f'총합={result1+result2}, 총시간={end-start}')

async def async_sleep():
    await asyncio.sleep(1)
    
async def async_sum(name, numbers):
    start = time.time()
    total = 0
    
    for n in numbers:
        await async_sleep()
        total += n
        print(f'작업 중={name}, number={n}, total={total}')
        
    end  = time.time()
    print(f'작업명={name}, 걸린시간={end-start}')
    return total

async def async_main():
    start = time.time()
    
    task1 = asyncio.create_task(async_sum('a', [1,2]))
    task2 = asyncio.create_task(async_sum('b', [1,2,3]))
    
    await task1
    await task2
    
    result1 = task1.result()
    result2 = task2.result()
    
    end = time.time()
    print(f'총합={result1 + result2}, 총시간={end-start}')
    
if __name__ == '__main__':
    main()
    asyncio.run(async_main())
