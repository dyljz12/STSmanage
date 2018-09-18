# Student类
import os
import pickle
from . import Group
from . import School
from . import Course
from . import Teacher


class Student(object):
    def __init__(self):
        self.sname = ''
        self.schname = ''
        self.scoursedic = {}
        self.sgrouplist = []
        return

    def store(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\student\%s' % (fddir, self.sname), 'wb') as fd:
            pickle.dump(self, fd)
        return

    def reg(self):
        name = input("请输入您的名字：")
        schoolname = input("请输入学校名字：")
        self.sname = name
        self.schname = schoolname

        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\school\%s' % (fddir, schoolname), 'rb') as fd:
            schoolobj = pickle.load(fd)
            schoolobj.studentlist.append(self)
            schoolobj.store()     ###有问题
        self.store()
        print('注册成功')
        return self

    def addgroup(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\school\%s' % (fddir, self.schname), 'rb') as fd:
            schoolobj = pickle.load(fd)
            schoolobj.getcourse()
            schoolobj.getgroup()
        choosecourse = input("输入你要上的课程名字：")
        choosegroup = input("输入你要上的班级名字：")

        with open('%s\dumpfile\group\%s' % (fddir, choosegroup), 'rb') as fd1:
            groupobj = pickle.load(fd1)
            if len(groupobj.gstudentdict) < int(groupobj.gmaxstudent):
                self.scoursedic[choosecourse] = '未缴费'
                groupobj.addstudent(self.sname)
                groupobj.store()
                print("报名成功，未缴费。")
            else:
                print("该班满员，不能报名。")
        self.store()
        return self

    def scorecheck(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        for i in self.sgrouplist:
            with open('%s\dumpfile\group\%s' % (fddir, i), 'rb') as fd:
                groupobj = pickle.load(fd)
                print("%s 课程的成绩是 %d" % (i, groupobj.gstudentdict[self.sname]))
        return self

    def pay(self):
        for key, ifpay in self.scoursedic.items():
            if ifpay == '未缴费':
                fddir = os.path.dirname(os.path.dirname(__file__))
                with open('%s\dumpfile\course\%s' % (fddir, key), 'rb') as fd:
                    courseobj = pickle.load(fd)
                    price = courseobj.cprice
                print("课程 %s 需要缴费 %s 元" % (key, price))
                yorno = input("是否缴费？y/n")
                if yorno == 'y':
                    self.scoursedic[key] = '已缴费'
                    print("已缴费")
                    self.store()

        return self