from concurrent.futures import ThreadPoolExecutor as pool
from concurrent.futures import as_completed
from worker import Worker

import tasklist
import dbg
import glv
import chromedriver_binary # type: ignore

dbg = dbg.Dbg()


class Scheduler:

    def run(self):
        taskList = tasklist.Tasklist()

        for task in taskList.tasks:
            with pool() as executor:
                futures = [executor.submit(Worker, task)]

                for f in as_completed(futures):
                    dbg.debug(str(f))
