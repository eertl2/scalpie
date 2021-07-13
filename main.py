from selenium import webdriver as wd
from worker import worker
import glv
#from multiprocessing import pool
import multiprocessing
import chromedriver_binary

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args = ("bestbuy", glv.ITEM))
    p2 = multiprocessing.Process(target=worker, args = ("bestbuy", glv.ITEM))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    
   
