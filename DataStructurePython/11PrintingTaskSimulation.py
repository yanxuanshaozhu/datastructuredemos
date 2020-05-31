import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, nextTask):
        self.currentTask = nextTask
        self.timeRemaining = nextTask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randint(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = []
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrinterTask():
            task = Task(currentSecond)
            printQueue.insert(0, task)

        if (not labprinter.busy()) and (not len(printQueue) == 0):
            nexttask = printQueue.pop()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, len(printQueue)))


def newPrinterTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 5)
    print("________________")
    for i in range(10):
        simulation(3600, 10)
