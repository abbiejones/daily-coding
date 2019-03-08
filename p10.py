#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import threading
import time

class Scheduler_1:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            time.sleep(n/1000)
            f()
        t = threading.Thread(target=sleep_then_call(n))
        t.start()


class Scheduler_2:
    def __init__(self):
        self.fns = []
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time.time() * 1000
            for fn, dues in self.fns:
                if now > dues:
                    fn()

            self.fns = [(fn, dues) for (fn, dues) in self.fns if dues > now]
            time.sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, (time.time() *1000) + n))