from Task import Task

print('Hello, lets get started!')

taskList = []

def start():
    print('Choose the options')
    print('1. Add a task')
    print('2. Remove a task')
    print('3. Show all tasks')

    try:
        option = int(input())
        if(option == 1):
            name = str(input('What name of the task:'))
            description = str(input('What description of the task:'))
            deadLine = str(input('What deadline of the task:'))
            task = Task(name, description, deadLine)
            taskList.append(task)
        elif(option == 2):
            index = int(input('What index of the task:'))
            taskList.pop(index)
        elif(option == 3):
            index = 0
            for task in taskList:
                print(f'Task number {index}')
                task.getName()
                task.getDescription()
                task.getDeadLine()
                index += 1
    except (IndexError, ValueError):
        print('Invalid input')

while(True):
    start()