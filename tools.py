import database


class Task:

    def __init__(self, title):
        self.title = title
        self.is_completed = False

    # self.date = self.date

    def change_completion(self):
        self.is_completed = not self.is_completed
