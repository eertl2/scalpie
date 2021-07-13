from threading import Lock
import glv

class purchasing:
    global activePurchasers #the number of threads that are currently in the payment info
    global purchased #number of items purchased
    global lock

    def __init__(self):
        lock = Lock()
    
    def aquirePurchasePerm():
        purchasing.lock.aquire()
        if(purchasing.activePurchasers + purchasing.purchased) < glv.QUANITY:
            purchasing.activePurchasers += 1
            purchasing.lock.release()
            return 1
        if(purchasing.purchased == glv.QUANITY):
            purchasing.lock.release()
            return -1
        purchasing.lock.release()
        return 0
    
    def purchaseSuccess():
        purchasing.lock.aquire()
        purchasing.purchased += 1
        purchasing.lock.release()