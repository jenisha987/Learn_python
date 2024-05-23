#--Function caching in Python--
import functools
import time
from functools import lru_cache
@lru_cache(maxsize=None)


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(20))



#--AsyncIO in Python--

import asyncio 
import requests
import time

async def function1():
    await asyncio.sleep(1)
    print("Func 1")
    return "Jenisha"
async def function2():
    await asyncio.sleep(1)
    print("Func 2")
async def function3():
    await asyncio.sleep(4)
    print("Func 3")
async def main():
    L = await asyncio.gather( 
        function1(),
        function2(),
        function3(),
    )
    print(L)
asyncio.run(main())

#example next
async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico", "wb").write(response.content)
    print("Func 1")
async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico", "wb").write(response.content)
    print("Func 2")
async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    print("Func 3")
async def main():
    L = await asyncio.gather( 
        function1(),
        function2(),
        function3(),
    )
    print(L)
asyncio.run(main())

