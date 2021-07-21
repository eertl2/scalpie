from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor as pool
from concurrent.futures import as_completed
from worker import Worker

import tasks
import dbg
import glv
import chromedriver_binary # type: ignore

dbg = dbg.Dbg()


class Scheduler:
    taskList = tasks.Tasklist()

    def run(self):
        m = Manager()
        lock = m.Lock()

        activeP = m.Value('i', 0)
        purchased = m.Value('i', 0)

        for task in self.taskList.tasks:
            with pool() as executor:
                futures = [executor.submit(Worker, "BestBuy", task.links[i], lock, activeP, purchased) for i in range(len(task.links))]

                for f in as_completed(futures):
                    dbg.debug(str(f))

        dbg.debug("Purchased:" + str(purchased.value))