#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge=None, list=None):
        super().__init__(first_name, last_name)
        self.knowledge = ["Initial knowledge 1", "Initial knowledge 2"]
        self.list = list if list else []

    def teach(self):
        if self.knowledge:
            return list(self.knowledge)[0]
        else:
            return None
        
my_teacher = Teacher("My", "Teacher")
my_teacher.first_name
my_teacher.last_name