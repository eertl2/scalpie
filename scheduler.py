from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor as pool
from concurrent.futures import as_completed
from worker import Worker

import dbg
import glv
import chromedriver_binary # type: ignore

dbg = dbg.Dbg()

class Scheduler:

    def run():
        m = Manager()
        lock = m.Lock()

        activeP = m.Value('i', 0)
        purchased = m.Value('i', 0)

        with pool() as executor:
            futures = [executor.submit(Worker, "BestBuy", glv.ITEM, lock, activeP, purchased) for _ in range(2)]

            for f in as_completed(futures):
                dbg.debug(str(f))

        dbg.debug("Purchased:" + str(purchased.value))