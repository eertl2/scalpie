class Task:
    amt = None
    links = []
    running = False
    completed = False

    #for scheduler
    lock = None
    activeP = 0
    purchased = 0

    def acquirePurchasePerm(task):
        with task.lock:
            if(task.activeP + task.purchased) < task.amt:
                task.activeP += 1 
                return 1 #green-light to try purchasing
            if(task.purchased == task.amt):
                return -1 #Quit worker
            return 0 #wait


    def completePurchase(task):
        with task.lock:
            task.activeP -= 1 #buyer completed, decrement active buyers
            task.purchased += 1