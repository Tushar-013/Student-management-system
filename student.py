import  os
import  pickle
class  student:
    def __init__(self):
        self.rollno=0
        self.name=" "
        self.sub1=0
        self.sub2=0
        self.sub3=0
    def read_data(self):
        self.rollno=int(input("Roll no:"))
        self.name=input("NAME:")
        self.sub1=int(input("Marks in Subject1:"))
        self.sub2=int(input("Marks in Subject2:"))
        self.sub3=int(input("marks in Subject3:"))
    def compute_total(self):
        self.total=self.sub1+self.sub2+self.sub3
    def show_data(self):
        print(" ",self.rollno,"\t\t\t",self.name,"\t\t\t",self.total)
     
     

   
def append():
    outfile=open("data.dat","ab")
    stu=student()
    n=int(input("No Of Student:"))
    for i in range(n):
            stu.read_data()
            stu.compute_total()
            pickle.dump(stu,outfile)
    outfile.close()

def display():
    infile=open("data.dat","rb")
    try:
        stu=student()
        print("  rollno.\t\t\tNAME\t\t\tTotal")
        while True:
            st=pickle.load(infile)
            st.show_data()
    except EOFError:
            infile.close()




def insert():
    st=student()
    nrec=student()
    print("NEW POSITION TO ENTER")
    nrec.read_data()
    nrec.compute_total()
    print("NEW RECORD IS ENTER")
    infile=open("data.dat","rb")
    outfile=open("temp.dat","wb")
    n=int(input("enter position to enter:"))
    try:
            c=0
            while True:
                st=pickle.load(infile)
                c=c+1
                if(c==n):
                    pickle.dump(nrec,outfile)
                    pickle.dump(st,outfile)
                else:
                    pickle.dump(st,outfile)
    except EOFError:
            outfile.close()
            infile.close()
    os.remove("data.dat")
    os.rename("temp.dat","data.dat")


def delete():
    st=student()
    infile=open("data.dat","rb")
    outfile=open("temp.dat","wb")
    n=int(input("enter for delete:"))
    try:
        c=0
        while True:
            st=pickle.load(infile)
            c=c+1
            if c!=n:
                pickle.dump(st,outfile)
    except EOFError:
      outfile.close()
      infile.close()
    os.remove("data.dat")
    os.rename("temp.dat","data.dat")







def update():
    st=student()
    nrec=student()
    print("Updated value to be enter")
    nrec.read_data()
    nrec.compute_total()
    print("NEW RECORD IS ENTER")
    infile=open("data.dat","rb")
    outfile=open("temp.dat","wb")
    n=int(input("enter position to enter:"))
    try:
            c=0
            while True:
                st=pickle.load(infile)
                c=c+1
                if c!=n:
                    pickle.dump(st,outfile)
                else:
                    pickle.dump(nrec,outfile)
    except EOFError:
            outfile.close()
            infile.close()
    os.remove("data.dat")
    os.rename("temp.dat","data.dat")


def search():
    flag=0
    st=student()
    sname=input("enter name to search:")
    infile=open("data.dat","rb")
    try:
         while True:
              st=pickle.load(infile)
              if(st.name==sname):
                st.show_data()
                flag=1
    except EOFError:
        infile.close()
        if(flag==1):
            print("Search is successfull")
        else:
            print("Search is unsuccessfull")
            




ch="y"
print("           ##$$$STUDENT INFORMATION MANAGEMENT SYSTEM $$$##")
while ch=="y"or ch=="y":
    print()
    print()
    print("          MAIN MENU")
    print()
    print("          1.APPEND")
    print("          2.INSERT")
    print("          3.DELETE")
    print("          4.UPDATE")
    print("          5.DISPLAY")
    print("          6.SEARCH")
    print("          7.EXIT")
    chh=int(input("enter your choice:" ))
    if (chh==1):
        append()
    elif (chh==2):
        insert()
    elif (chh==3):
          delete()
    elif (chh==4):
          update()
    elif (chh==5):
        display()
        print
        print
        a=input("press enter key to continue")
    elif (chh==6):
          f=search()
    elif (chh==7):
        ch='n'
        print("Exit selected"          )
    else:
        print("INVALID CHOICE")



    print("              ###::::::PLESE VISIT AGAIN:::::::###")
    print("              >>>>>>:::THANKS FOR VISITING:::<<<<<<<<" )       

