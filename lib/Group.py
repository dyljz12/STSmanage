# Group类
import os
import pickle


class Group(object):
    def __init__(self, name, maxnumber, teachername):
        self.gname = name
        self.gmaxstudent = maxnumber
        self.gteacher = teachername
        self.gstudentdict = {}  # 学生姓名：成绩
        return

    def store(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\group\%s' % (fddir, self.gname), 'wb') as fd:
            pickle.dump(self, fd)
        return

    def addstudent(self, sname):
        self.gstudentdict[sname] = 0
        return
