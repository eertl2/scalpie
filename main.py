from selenium import webdriver as wd
from worker import worker
import glv
import multiprocessing
from concurrent.futures import ProcessPoolExecutor as pool
import chromedriver_binary

if __name__ == "__main__":
    m = multiprocessing.Manager()
    lock = m.Lock()

    activeP = m.Value(int, 0)
    purchased = m.Value(int, 0)

    with pool as executor:
        results = [executor.submit(target=worker, args = ("bestbuy", glv.ITEM, lock, activeP, purchased)) for _ in range(3)]

        for f in pool:
            print(f.result)


    
   
