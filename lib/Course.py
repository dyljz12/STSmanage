# Course类
import os
import pickle


class Course(object):
    def __init__(self, name, price):
        self.cname = name
        self.cprice = price
        self.cgroup = []
        return

    def store(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\course\%s' % (fddir, self.cname), 'wb') as fd:
            pickle.dump(self, fd)
        return
