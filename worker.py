import bestbuy

class worker:
    def __init__(self, place, item):
        if place == "bestbuy":
            bb = bestbuy.bestbuy()
            bb.purchase(item)
        return