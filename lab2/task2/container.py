import re

'''students = {
    "Vadim": {"1", "2", "3", "4", "5"},
    "Denis": {"6", "7", "8", "9"},
    "Egor": {"10", "11", "12", "13"}
}'''


# students.get("Vadim").add("6")


class Container:
    current_user = "Vadim"
    usernames_keys = []

    def __init__(self, usernames):
        self.usernames = usernames
        self.usernames_keys.append(usernames.keys())

    def add(self, *element):
        for i in element:
            self.usernames.get(self.current_user).add(i)

    def remove(self, element):
        remove_flag = False
        for i in self.usernames.get(self.current_user):
            if i == element:
                remove_flag = True

        if remove_flag:
            self.usernames.get(self.current_user).remove(element)

    def list(self):
        print(self.usernames.get(self.current_user))

    def switch(self, new_user):
        self.current_user = new_user

        if self.current_user not in self.usernames_keys:
            self.usernames[self.current_user] = set()

    def save(self):
        with open("storage.txt", "w") as f:
            for i in self.usernames.keys():
                f.write(i + " " + " ".join([str(x) for x in self.usernames[i]]) + "\n")

    def load(self):
        with open("storage.txt", "r") as f:
            dict_temp = {}
            for line in f:
                values = line.split(' ')
                dict_temp[values[0]] = set(x.replace("\n", "") for x in values[1:len(values)])
            self.usernames = dict_temp
            return dict_temp

    def grep(self, regex):
        found_elements = []
        for i in self.usernames.get(self.current_user):
            check_i = re.search(regex, i)
            if check_i:
                found_elements.append(i)

        if len(found_elements) == 0:
            return "There are no such elements"
        else:
            return found_elements

    def find(self, *element):
        user_data = self.usernames.get(self.current_user)
        found_elements = []

        for i in user_data:
            for j in element:
                if i == j:
                    found_elements.append(i)

        if len(found_elements) == 0:
            return "There are no such elements"
        else:
            return found_elements



