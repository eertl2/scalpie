from concurrent.futures import ThreadPoolExecutor as pool
from concurrent.futures import as_completed
from worker import Worker

import tasklist
import dbg
import traceback
import glv
import chromedriver_binary # type: ignore

dbg = dbg.Dbg()

class Scheduler:

    def run(self):
        taskList = tasklist.Tasklist()

        with pool(max_workers=glv.MAX_THREADS) as executor:
            for task in taskList.tasks:
                futures = [executor.submit(Worker, task) for _ in task.links]

                for worker in as_completed(futures):
                    try:
                        dbg.debug(str(worker))
                        dbg.debug("Task completed (item bought):" + str(worker.result().link))
                    except:
                        dbg.debug("Program failed: " + traceback.format_exc())
