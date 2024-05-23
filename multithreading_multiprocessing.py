#--Multithreading in Python--

import threading
import time

#indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds.")
    time.sleep(seconds)

# #Normal Code
time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()
print(time2 - time1)
    
# #Same code using thread(100-102)
time1 = time.perf_counter()
t1 = threading.Thread(target = func, args = [4])
t2 = threading.Thread(target = func, args = [2])
t3 = threading.Thread(target = func, args = [1])

t1.start() #0 bata nai start huna thalxa
t2.start()
t3.start()

t1.join() #wait until t1 is over
t2.join() #wait until t2 is over
t3.join() #wait until t3 is over
time2 = time.perf_counter()
print(time2 - time1)



#--Multiprocessing in Python--

import multiprocessing
import concurrent.futures
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")
url = "https://picsum.photos/200/300"
pros = []
for i in range(5):
    downloadFile(url, i)
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)
for p in pros:
    p.join()

# with concurrent.futures.ProcessPoolExecutor() as executor:
    # l1 = [url for i in range(6)]
    # l2 = [i for i in range(6)]
    # results = executor.map(downloadFile, l1, l2)
    # for r in results:
    #     print(r)