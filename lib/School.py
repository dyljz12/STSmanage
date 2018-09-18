# school类
import pickle
import os
from . import Course
from . import Group
from . import Student
from . import Teacher


class School(object):
    def __init__(self):
        self.sname = ''
        self.saddress = ''
        self.teacherlist = []
        self.courselist = []
        self.grouplist = []
        self.studentlist = []
        return

    def store(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\school\%s' % (fddir, self.sname), 'wb') as fd:
            pickle.dump(self, fd)
        return

    def setschool(self):
        name = input("学校名字：")
        address = input("学校地址：")
        self.sname = name
        self.saddress = address
        self.store()
        return self

    def getteacher(self):
        print("本校有以下老师：")
        for t in self.teacherlist:
            print(t.tname)
        return

    def getcourse(self):
        print("本校开设以下课程：")
        for c in self.courselist:
            print(c.cname)
        return

    def getgroup(self):
        print("本校开设以下班级：")
        for g in self.grouplist:
            print(g.gname)
        return

    def getstudent(self):
        print("本校有以下学员：")
        for s in self.studentlist:
            print(s.sname)
        return

    def addteacher(self):
        print("招募讲师......")
        name = input("老师姓名：")
        newteacher = Teacher.Teacher(name)
        self.teacherlist.append(newteacher)
        print("%s 老师到岗。" % newteacher.tname)
        newteacher.store()
        self.store()
        return

    def addcourse(self):
        print("开设课程......")
        name = input("课程名称：")
        price = input("课程价格：")
        newcourse = Course.Course(name, price)
        self.courselist.append(newcourse)
        print("%s 课程开设完毕。" % newcourse.cname)
        newcourse.store()
        self.store()
        return

    def addgroup(self):
        print("开设班级......")
        csname = input("课程名字：")
        name = input("班级名字：")
        maxnum = input("班级最多人数：")
        teachername = input("带班老师：")

        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\\teacher\%s' % (fddir, teachername), 'rb') as fd:
            teacherobj = pickle.load(fd)

        cnamelist = []
        for c in self.courselist:
            cnamelist.append(c.cname)
        if csname in cnamelist:
            tnamelist = []
            for t in self.teacherlist:
                tnamelist.append(t.tname)
            if teachername in tnamelist:
                newgroup = Group.Group(name, maxnum, teachername)
                self.grouplist.append(newgroup)
                newgroup.store()
                teacherobj.grouplist.append(newgroup)
                teacherobj.store()
            else:
                print("没有你要的带班老师，班级开设失败。")
        else:
            print("本校没有你输入的课程，班级开设失败")
        self.store()
        return
