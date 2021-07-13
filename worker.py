import bestbuy
from purchasing import purchasing

class worker:
    def __init__(self, place, item):
        if place == "bestbuy":
            bb = bestbuy.bestbuy()
            if(bb.purchase(item)):
                purchasing.purchased += 1
                return
