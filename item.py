class item:

    amt = None
    links = []

    def __init__(self):
    #Parse user-details.txt
        lines = []

        with open("itemlist.txt", "r") as f:
            lines = f.readlines()

        count = 0
        for line in lines:
            linestr = line.split('==')
            if count == 1:
                self.amt = linestr[1]
            else:
                self.links[count] = linestr[0]