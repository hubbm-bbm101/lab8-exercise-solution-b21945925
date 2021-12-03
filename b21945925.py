import sys
file = open(sys.argv[1],"r",encoding="utf-8")
content = file.read().split("\n")
maindict = {}
for i in content:
    person, school = i.split(":")
    maindict[person] = str(school)
for student in sys.argv[2].split(","):
    try:
        print("Name: {}, University: {} ".format(student,maindict[student]))
    except:
        print("No record of {} was found!".format(student))
