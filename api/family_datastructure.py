"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class Family:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": 1,
            "first_name": "John"
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        agregado = {
            "id": self._generateId(),
            "first_name": member["first_name"],
        }
        self._members.append(agregado)
        return agregado

    def delete_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x.id == id:
                return self._members.remove(x)


    def update_member(self, id, member):
        # fill this method and update the return
        if id == self._members["id"]:
            puesto = {
                "first_name": member["first_name"],
            }
            self._members.insert(self._members[id], puesto)
        return puesto

    def get_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x.id == id:
                return x

    # this method is done, it returns a list with all the family members

    def get_all_members(self):
        return self._members
