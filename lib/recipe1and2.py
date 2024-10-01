class Todo:
    def __init__(self):
        self.task_list = []

    def add(self,task):
        if type(task) != str:
            raise Exception("Only strings are allowed!")
        self.task_list.append(task)

    def show(self):
        return self.task_list
    
    def mark_complete(self, task):
        if type(task) != str:
            raise Exception("Only strings are allowed!")
        if task not in self.task_list:
            raise Exception("No such task!")
        self.task_list.remove(task)
