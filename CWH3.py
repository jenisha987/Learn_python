#--Generators in Python--generates the value one by one

def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)

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

#--Regular Expressions in Python--

# import re
# pattern = r"[A-Z]yclone"
# text = '''Mary Jane Richardson Cyclone Jones (1819–1909) was an American abolitionist,
# philanthropist, and suffragist. Born in Tennessee to free black parents, Jones 
# moved with her family to Cyclone Illinois during her teenage years. Along with her husband, 
# John, she was a leading African-American figure in the early history of Chicago. 
# The Jones household was a Dyclone stop on the Underground Railroad and a center of abolitionist
# activity. The Joneses helped hundreds of fugitives fleeing slavery. After her husband's 
# death in 1879, Jones continued to support African-American civil rights and advancement 
# in Chicago, and became a suffragist. She was active in the women's club movement and mentored 
# a new generation of younger black leaders, such as Fannie Barrier Williams, Ida B. Wells, and 
# Daniel Hale Williams. She also made extensive philanthropic contributions.
# '''
# # match = re.search(pattern, text)
# match = re.finditer(pattern, text)
# for matches in match:
#     # print(matches)
#     print(matches.span())
#     print(text[matches.span()[0]:matches.span()[1]])

#--AsyncIO in Python--

# import asyncio 
# import requests
# import time

# async def function1():
#     await asyncio.sleep(1)
#     print("Func 1")
#     return "Jenisha"
# async def function2():
#     await asyncio.sleep(1)
#     print("Func 2")
# async def function3():
#     await asyncio.sleep(4)
#     print("Func 3")
# async def main():
#     L = await asyncio.gather( 
#         function1(),
#         function2(),
#         function3(),
#     )
#     print(L)
# asyncio.run(main())

#example next
# async def function1():
#     URL = "https://instagram.com/favicon.ico"
#     response = requests.get(URL)
#     open("instagram1.ico", "wb").write(response.content)
#     print("Func 1")
# async def function2():
#     URL = "https://instagram.com/favicon.ico"
#     response = requests.get(URL)
#     open("instagram2.ico", "wb").write(response.content)
#     print("Func 2")
# async def function3():
#     URL = "https://instagram.com/favicon.ico"
#     response = requests.get(URL)
#     open("instagram3.ico", "wb").write(response.content)
#     print("Func 3")
# async def main():
#     L = await asyncio.gather( 
#         function1(),
#         function2(),
#         function3(),
#     )
#     print(L)
# asyncio.run(main())

#--Multithreading in Python--

# import threading
# import time

# #indicates some task being done
# def func(seconds):
#     print(f"Sleeping for {seconds} seconds.")
#     time.sleep(seconds)

# #Normal Code
# # time1 = time.perf_counter()
# # func(4)
# # func(2)
# # func(1)
# # time2 = time.perf_counter()
# # print(time2 - time1)
    
# #Same code using thread(100-102)
# time1 = time.perf_counter()
# t1 = threading.Thread(target = func, args = [4])
# t2 = threading.Thread(target = func, args = [2])
# t3 = threading.Thread(target = func, args = [1])

# t1.start() #0 bata nai start huna thalxa
# t2.start()
# t3.start()

# t1.join() #wait until t1 is over
# t2.join() #wait until t2 is over
# t3.join() #wait until t3 is over
# time2 = time.perf_counter()
# print(time2 - time1)

#--Multiprocessing in Python--

# import multiprocessing
# import concurrent.futures
# import requests

# def downloadFile(url, name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")
# url = "https://picsum.photos/200/300"
# # pros = []
# # for i in range(5):
# #     # downloadFile(url, i)
# #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
# #     p.start()
# #     pros.append(p)
# # for p in pros:
# #     p.join()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     l1 = [url for i in range(6)]
#     l2 = [i for i in range(6)]
#     results = executor.map(downloadFile, l1, l2)
#     for r in results:
#         print(r)