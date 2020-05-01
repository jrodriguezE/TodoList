# To do List
#  Date created: 4/29/2020
# 
class Task:
    def __init__(self,  name, dueDate)
    self.name = name
    self.dueDate = dueDate
    self.done = False

    # funtion in
    def printData(self, index)
        print("{0}. Task: {1}, Date: {2}, Complited: {3}".format(index, self.name
        self.dueDate, self.done))


# Display menu function
def printMenu():
    print("**************************")
    print("*****   My todo List  ****")
    print("**************************")
    print("* 1. Add task")
    print("* 2. Edit task")
    print("* 3. Mark as done task")
    print("* 4. Delete task")
    print("* 5. List of task")
    print("* 6. Exit")

def printTitleList():
    print()
    print("*******************************")
    print("List of Taks")
    print("*******************************")
    print()


# validate function
# 
def getOptions():
    try:
        value = input("type a number: ")
        option = int(value)
    except ValueError:
        print("Wrong value, only numbers between 1-6.")

    return option

printMenu()
getOptions()