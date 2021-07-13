from threading import Lock
import glv
import dbg

class purchasing:
    activePurchasers = 0 #the number of threads that are currently in the payment info
    purchased = 0 #number of items purchased
    lock = Lock()
    dbgr = dbg.dbgr()
    
    @staticmethod
    def aquirePurchasePerm():
        purchasing.lock.acquire()
        if(purchasing.activePurchasers + purchasing.purchased) < glv.QUANITY:
            purchasing.activePurchasers += 1
            purchasing.lock.release()
            return 1
        if(purchasing.purchased == glv.QUANITY):
            purchasing.lock.release()
            return -1
        purchasing.lock.release()
        return 0
    
    @staticmethod
    def purchaseSuccess():
        purchasing.lock.acquire()
        purchasing.purchased += 1
        purchasing.lock.release()