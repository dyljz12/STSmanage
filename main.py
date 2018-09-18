#main.py
from interface import *
from lib import *

programexitflag = False
optdic = {'1': schoolmanage.schoolcontrol, '2': teachermanage.teachercontrol, '3': studentmanage.studentcontrol,
          '4': exit}

while not programexitflag:
    idcheck = input("Who areeee you?\n1:Administrator\n2:Teacher\n3:Student\n4:exit\n")
    if idcheck in optdic.keys():
        optdic[idcheck]()
###报名后信息不在数据库里++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++