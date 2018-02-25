from member import Member, MemberClub


class ProcessMember(object):
    """
        This class manages all the required operation to manage the club.
    """
    EXIT_PROGRAM = "7"

    def __init__(self, club_member):
        self.club_member = club_member
        self.method_dict = {"1": self._add, "2": self._view_member_info, "3": self._search_member,
                            "4": self._display_member, "5": self._update_member_info,
                            "6": self._remove_member}

    def process_club_members(self):
        while True:
            print("Choose one the options to process member:")
            print("1 Add new member")
            print("2 View member Info")
            print("3 Search for a member")
            print("4 Browse All Members")
            print("5 Edit members")
            print("6 Delete a member")
            print("7 Quit application\n")
            number = input("Enter a number: ")
            if number == ProcessMember.EXIT_PROGRAM:
                print("have a nice day")
                break
            method = self.method_dict.get(number)
            if method is None:
                print("Enter valid number: ")
            else:
                method()

    def _add(self):
        member_name = input("Enter member name: ")
        member_id = input("Enter member id: ")
        gender = input("Enter gender: ")
        phone = input("Enter phone: ")
        weight = input("Enter weight: ")
        member = Member(member_name, member_id, gender, phone, weight)
        self.club_member.add(member)

    def _view_member_info(self):
        member_id = input("Enter member id: ")
        print(self.club_member.view_member_info(member_id))

    def _search_member(self):
        member_id = input("Enter member id: ")
        print(self.club_member.search_member(member_id))

    def _display_member(self):
        print(self.club_member.display_member())

    def _update_member_info(self):
        member_id = input("Enter member id: ")
        self.club_member.update_member_info(member_id)

    def _remove_member(self):
        member_id = input("Enter member id: ")
        self.club_member.remove_member(member_id)

if __name__ == "__main__":
    club = MemberClub("member.dat")
    process_member = ProcessMember(club)
    process_member.process_club_members()
