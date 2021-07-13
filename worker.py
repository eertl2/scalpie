import bestbuy
import glv
import time

class worker:
    def __init__(self, place, item, lock, activeP, purchased):
        if place == "bestbuy":
            bb = bestbuy.bestbuy()
            if(bb.purchase(item)):
                pcode = self.acquirePurchasePerm(lock, activeP, purchased)
                while(pcode == 0):
                    #self.dbgr.debug("Waiting for buying permission")
                    time.sleep(5)
                    pcode = self.acquirePurchasePerm(lock, activeP, purchased)

                    if(pcode == -1):
                        #self.dbgr.debug("Max quanity of product has already been bought")
                        return False
                bb.buyItem()
            return False

    def acquirePurchasePerm(self, lock, activeP, purchased):
        with lock:
            if(activeP + purchased) < glv.QUANITY:
                activeP += 1
                return 1
            if(purchased == glv.QUANITY):
                return -1
            return 0
    
    def purchaseSuccess(self, lock, purchased):
        with lock:
            purchased += 1