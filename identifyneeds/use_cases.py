
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
        # conditions_to_fetch = characteristic.get_condition_names()
        # conditions = memrepo.get(filter_names=conditions_to_fetch)
        # for condition in conditions

