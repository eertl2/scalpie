class Tasklist:

    tasks = []

    def __init__(self):
    #Parse itemlist.txt
        lines = []

        with open("itemlist.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            linestr = line.split('==')

            if linestr[0] == "Quanity":
                curTask = Task()
                curTask.amt = int(linestr[1].strip('\n'))
                count = 0
            elif linestr[0] == '\n': 
                self.tasks.append(curTask)
            else:
                curTask.links.append(linestr[0])
                count += 1
        self.tasks.append(curTask) #append the last task

class Task:
    amt = None
    links = []
    completed = False