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

        with pool() as executor:
            futures = [executor.submit(Worker, task) for task in taskList.tasks]

            for worker in as_completed(futures):
                dbg.debug(str(worker))
                dbg.debug("Task completed:" + str(worker.result().task.completed))
