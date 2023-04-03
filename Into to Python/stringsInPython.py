"""
here it's multi lines comment

:))
"""


name="mahmoud hassan"

bio="""This is {}
I'm a software engineer
i'm 29 years old
"""

bio2="""This is {name}
I'm a software engineer
i'm 29 years old
"""

age=34

ageString=str(age)

print(f"my age is {age}")

print(bio.format(name))
print(bio2.format(name="Ahmed"))