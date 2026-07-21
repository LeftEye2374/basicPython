class Task:

    def __init__(self, name, description, deadLine):
        self.name = name
        self.description = description
        self.deadLine = deadLine

    def getName(self):
        print(self.name)

    def getDescription(self):
        print(self.description)

    def getDeadLine(self):
        print(self.deadLine)