"""
    File: member.py

    This module define the member class
"""
import pickle


class Member(object):
    """This class represents the Member class with its
        require attributes.
    """

    def __init__(self, name, member_id, gender, phone, weight=0):
        self._name = name
        self._id = member_id
        self._gender = gender
        self._phone = phone
        self._weight = weight

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_gender(self):
        return self._gender

    def get_phone(self):
        return self._phone

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def set_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return "Name: {0._name} Id: {0._id} Gender: {0._gender} Phone: {0._phone} Weight: {0._weight}".format(self)


class MemberClub(object):
    """
        This class handles the club management system and manage the member's information
    """
    def __init__(self, filename=None):
        self.filename = filename
        self._member_dict = {}
        if filename is not None:
            file_object = open(filename, 'rb')
            while True:
                try:
                    member_info = pickle.load(file_object)
                    self.add(member_info)
                except EOFError:
                    file_object.close()
                    return

    def add(self, member_info):
        if member_info.get_id() in self._member_dict.keys():
            print("Member already exist in the club")
        else:
            self._member_dict[member_info.get_id()] = member_info
            self.save_member(self.filename)

    def view_member_info(self, member_id):
        return self.search_member(member_id)

    def search_member(self, member_id):
        if member_id not in self._member_dict.keys():
            print("Member does not exist!")
            return None
        else:
            return self._member_dict.get(member_id)

    def display_member(self):
        return '\n'.join(map(str, self._member_dict.values()))

    def update_member_info(self, member_id):
        if member_id not in self._member_dict.keys():
            print("Member can't be updated, Not added in the club yet!")
        else:
            club_member = self._member_dict.get(member_id)
            weight = input("Enter new weight of the member: ")
            club_member.set_weight(weight)
            phone = input("Enter new phone number of the member: ")
            club_member.set_phone(phone)
        self.save_member(self.filename)

    def remove_member(self, member_id):
        if member_id not in self._member_dict.keys():
            print("Member is not added to the club yet!")
        else:
            self._member_dict.pop(member_id)
            self.save_member(self.filename)

    def save_member(self, filename=None):
        file_object = open(filename, 'wb')
        for member in self._member_dict.values():
            pickle.dump(member, file_object)
        file_object.close()



