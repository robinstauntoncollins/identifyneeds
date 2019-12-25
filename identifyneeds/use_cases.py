
class ListConditions():
    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return self.repo.get()


# class UpdateConditions():

#     def __init__(self, repo, characteristic):
#         self.repo = repo
#         self.characteristic = characteristic

#     def execute(self):
#         self.characteristic.add_

