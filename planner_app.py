from datetime import date, datetime, time, timedelta
import calendar

def makechoices():
    print("Planner page maker. What are you thinking? \n")
    print("1: Make yearly calendar. \n")
    print("2: Make daily pages. \n")
    choice = int(input("Your choice: "))

    if choice == 1:
        try:    
            year = input("Enter a year:")
            year_cp = int(year)
            getyear = datetime.strptime(year,"%Y").date()      
         
            extension = ".txt"  
            file_name = str(year_cp) + extension
            file = open(file_name, 'w') 
            file.write(calendar.calendar(year_cp))
            file.close()
        except ValueError as e_choice:
            makechoices()        
                
    elif choice == 2:
        import planner_pages
        
    else:
        print("Goodbye!")

makechoices()
