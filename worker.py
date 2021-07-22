import bestbuy
import glv
import dbg
import time

dbg = dbg.Dbg()

class Worker:

    def __init__(self, place, item, activeP, purchased):
        if place == "BestBuy":
            bb = bestbuy.BestBuy()     
            bb.purchase(item) #brings browser to the 'buy now' button, but program has to get permission first
            pcode = self.acquirePurchasePerm(activeP, purchased)
            while(pcode != 1):
                dbg.debug("Waiting for buying permission")
                time.sleep(5)
                pcode = self.acquirePurchasePerm(activeP, purchased)
                if(pcode == -1):
                    dbg.debug("Max quanity of product has already been bought")
                    return
            if(bb.buyItem()):
                self.purchaseSuccess(activeP, purchased)
                dbg.debug("Purchase successful.")
            else:
                self.purchaseFail(activeP)
                dbg.debug("Purchase Failed.")
            bb.close()

    def acquirePurchasePerm(self, activeP, purchased):
        if(activeP.value + purchased.value) < glv.QUANITY:
            activeP.value += 1
            return 1
        if(purchased.value == glv.QUANITY):
            return -1
        return 0

    def purchaseSuccess(self, activeP, purchased):
            activeP.value -= 1
            purchased.value += 1

    def purchaseFail(self, activeP):
            activeP.value -= 1