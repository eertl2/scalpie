from selenium import webdriver as wd
from worker import worker
import glv
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor as pool
import chromedriver_binary # type: ignore

if __name__ == "__main__":
    m = Manager()
    lock = m.Lock()

    activeP = m.Value('i', 0)
    purchased = m.Value('i', 0)

    with pool() as executor:
        results = [executor.submit(worker, "bestbuy", glv.ITEM, lock, activeP, purchased) for _ in range(2)]

    for f in results:
        print(f)

    print(activeP.value)




    
   
