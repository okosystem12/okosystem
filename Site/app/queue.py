from threading import Thread
import time


class Queue:
    def __init__(self):
        self.queue = list()
        self.work = False
        self.step = 5

    def add_element(self, val):
        self.queue.insert(0, val)
        if not self.work:
            self.work = True
            Thread(target=self.exec).start()

    def remove_element(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        self.work = False

    def exec(self):
        while self.work:
            tr = self.remove_element()
            if tr:
                tr.start()
            time.sleep(self.step)

    def size(self):
        return len(self.queue)


que = Queue()
