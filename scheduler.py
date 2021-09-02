from concurrent.futures import ThreadPoolExecutor as pool
from concurrent.futures import as_completed
from worker import Worker

import tasklist
import dbg
import traceback
import glv
import multiprocessing
import chromedriver_binary # type: ignore

dbg = dbg.Dbg()

class Scheduler:

    def run(self):
        taskList = tasklist.Tasklist()

        m = multiprocessing.Manager()
        for task in taskList.tasks:
            task.lock = m.Lock()

            with pool(max_workers=glv.MAX_THREADS) as executor:
                futures = [executor.submit(Worker, "bestbuy", link, task) for link in task.links]

                for worker in as_completed(futures):
                    try:
                        dbg.debug(str(worker))
                        dbg.debug("Task completed (item bought):" + str(worker.result()))
                    except:
                        dbg.debug("Program failed: " + traceback.format_exc())
    
