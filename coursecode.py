coursecode='DEMO111'
if __name__=="__main__":
    testname = open("coursecode.py","r")
    testname.readline()
    name = input("Enter the name of the quiz instance : ")
    content= "coursecode='"+name+"'\n"
    content=content+testname.read()
    testname.close()
    testname=open("coursecode.py","w")
    testname.write(content)