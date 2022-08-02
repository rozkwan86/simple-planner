from datetime import date, datetime, time, timedelta
import calendar

def cale(f):
    todo = 1

    f.write("\n")
    f.write("\n")
    
    try:    
        s1=input('Enter day start hour and min as HH:MM: ')  
        t1 = datetime.strptime(s1, "%H:%M")
    except ValueError as e_cale:
        cale(f)
    try:
        s2=input("Enter day end hour and min separated by HH:MM: ")
        t2 = datetime.strptime(s2, "%H:%M")
    except ValueError as e_cale2:
        s2=input("Enter day end hour and min separated by HH:MM: ")
        t2 = datetime.strptime(s2, "%H:%M")
        
    inter = int(input("Enter intervals in minutes: "))
    timeskip = timedelta(minutes = inter)     

    start = t1
    end  = t2
    
    f.write("\n")
    f.write("Appointments:")
    f.write("\n")
    f.write("\n")
    
    while (start <= end):
        f.write(str(start).strip("1900-01-01").replace(" ",""))
        start += timeskip
        f.write("\n")

     
    f.write("\n")
    f.write("\n")
    f.write("Top 10 To-do: ")
    f.write("\n")
    f.write("\n")
    for x in range(1,11):
        f.write(str(todo) + ': \n')
        todo = todo + 1
    f.write("\n")
    f.write("\n")
    f.write("Notes:\n" )

def grab_ymd():
    grab = input("What is the date (in MM-DD-YYYY)? ")  
    grabdate = datetime.strptime(grab,"%m-%d-%Y").date()


    extension = ".txt"  
    file_name = str(grabdate) + extension
    file = open(file_name, 'w')

    yy = grabdate.year
    mm = grabdate.month
    dd = grabdate.day

    file.write(calendar.month(yy, mm))   
    file.write("\n")
    file.write("Week #: "+ str(date(yy, mm, dd).isocalendar()[1]))
    file.write("\n")

    file.write("Date: " + str(grabdate))
    file.write("\n")

    cale(file)

    file.close()
    
try:
    grab_ymd()
    
except ValueError as e:
    grab_ymd()
