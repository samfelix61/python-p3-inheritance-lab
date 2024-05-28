#!/usr/bin/env python

from user import User

import random

# Assuming User class is defined as follows
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)  # Initialize first_name and last_name using User's __init__ method
        self.knowledge = knowledge  # Initialize knowledge attribute

    def teach(self):
        # This method can be implemented as needed, currently left empty
        pass

# Example usage and test
knowledge_strings = ["Math", "Science", "History"]
teacher = Teacher("John", "Doe", knowledge_strings)

print(teacher.first_name)  # Should output: John
print(teacher.last_name)   # Should output: Doe
print(teacher.knowledge)   # Should output: ['Math', 'Science', 'History']
