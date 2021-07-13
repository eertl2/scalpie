from selenium import webdriver as wd
from worker import worker
import glv
import multiprocessing
from concurrent.futures import ProcessPoolExecutor as pool
import chromedriver_binary

# activeP = 0 #the number of threads that are currently in the payment info
# purchased = 0 #number of items purchased

if __name__ == "__main__":
    m = multiprocessing.Manager()
    lock = m.Lock()

    activeP = m.Value(0)
    purchased = m.Value(0)

    with pool as executor:
        results = [executor.submit(target=worker, args = ("bestbuy", glv.ITEM, lock, activeP, purchased)) for _ in range(3)]

        for f in pool:
            print(f.result)

        
# def acquirePurchasePerm(activePurchasers, purchased, lock):
#     with lock:
#         if(activePurchasers + purchased) < glv.QUANITY:
#             activePurchasers += 1
#             return 1
#         if(purchased == glv.QUANITY):
#             return -1
#         return 0

    
   
