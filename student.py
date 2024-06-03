# class Student:
#     name = "Agnes"
#     code ="021"
#     school = "AkiraChix"
#     age = 20
class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code

    def greet_student(self):
        greeting=f"Hello {self.first_name},welcome to {self.school}.your code is {self.code}"
        return greeting
    def Student_birth_year(self):
        year=f"Hello {self.first_name},you were born in {2024-self.age}"
        return year
    def Student_initials(self):
        initials=f"Hey your initials are {self.first_name[0]}.{self.last_name[0]}"
        return initials

    def Student_full_name(self):
        fullname=f"my name is {self.first_name} {self.last_name}"
        return fullname

    def enrol_student(self):
        enrol=f"Hey {self.first_name} {self.last_name} you are code {self.code} from {self.country} and you are enrolled to {self.school} ."
        return enrol
