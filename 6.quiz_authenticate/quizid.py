quizid='DEMO111.TX'
if __name__=="__main__":
    testname = open("quizid.py","r")
    testname.readline()
    name = input("Enter the name of the quiz instance : ")
    content= "quizid='"+name+"'\n"
    content=content+testname.read()
    testname.close()
    testname=open("quizid.py","w")
    testname.write(content)