# Teacher类
import os
import pickle


class Teacher(object):
    def __init__(self, name=''):
        self.tname = name
        self.grouplist = []  # 放的是group对象，在school建立班级的时候关联上去的
        return

    def store(self):
        fddir = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\\teacher\%s' % (fddir, self.tname), 'wb') as fd:
            pickle.dump(self, fd)
        return

    def checkgroupinfo(self):
        for g in self.grouplist:
            print("%s 班级有以下学生：" % g.gname)
            for key in g.gstudentdict.keys():
                print(key)
        return self

    def changescore(self):
        gname = input("请输入要登记成绩的班级名字：")
        for g in self.grouplist:
            if gname == g.gname:
                flag = True
                while flag:
                    sname = input("请输入学生姓名：")
                    sscore = input("请输入学生成绩：")
                    if sname in g.gstudentdict.keys():
                        g.gstudentdict[sname] = sscore
                    else:
                        print("没有这个学生。")
                    cont = input("继续登记吗？y/n")
                    if cont == 'n':
                        flag = False
        return self
