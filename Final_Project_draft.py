import datetime
import calendar

class Event:
    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date

class Eventplanner:
    def __init__(self, month):
        
        month.capitalize()

        self.month = month

        self.your_calendar = Calendar(month)
        
        self.events = []

    def add_event(self, event):
        if isinstance(event, Event): 
            self.events.append(event)
        
        else: 
            print("Invalid Object")

    def view_events(self):
        if not self.events:
            print("event not found")
        else:
            print("upcoming events")
        for event in self.events:
            print(f"Title: {event.title}")
            print (f" Location: {event.location}")
            print(f" Date: {event.date}")

    def display_current_calendar (self):

        return print(self.your_calendar.display_calendar())
    




class Calendar:
    def __init__(self, month): 

        self.month = month

        months = ["January","Febuary","March","April","May","June"
                      ,"July","August","September","October","November","December"]

        index = 0
        for index, mon in months:
            if mon == month:
                currentmonth = months[index]
            
            index += 1
        
        
        
        
        
        def display_calendar(self):
            
            planner = calendar.monthcalendar(datetime.datetime.now().year,currentmonth)

            return print(planner)
        
def main(month):
    yourplanner = Eventplanner(month)

    yourplanner.display_current_calendar()




      










if __name__ == "__main__":
        
        print("Welcome to your Event Planner! \n")
        print ("1: Open Event Planner (View Events)") 
        print("2: Close Program")  
        
        selection = input("Enter your selection: (1/2)")

        if selection == "1":
            print("What Month are you planning in? \n")
            print("0: January")
            print("1: Febuary")
            print("2: March")
            print("3: April")
            print("4: May")
            print("5: June")
            print("6: July")
            print("7: August")
            print("8: September")
            print("9: October")
            print("10: November")
            print("11: December")

            selection2 = input("Enter your selection: (1/2/3/4/5/6/7/8/9/10/11)")
            
        
        
        else:
            print("Goodbye!")
            
            quit()
        
        main(selection2)
        



