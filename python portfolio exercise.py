# Scholarship eligibility criteria through math and physics scores.
print("==============SCHOLARSHIP CRITERIA AND ITS ELIGIBILITY ==============")
name = ("What is your name :")
physics_grade=int(input("What is you physics grade:"))
math_grade=int(input("What is your math grade:"))
# if get either 80 or greater in physics or math then you are eligible. 
if physics_grade >=80 or math_grade >=80:
    print(f"YOU ARE ELIGIBLE FOR THIS SCHOLARSHIP {name}")
else:
    print("YOU ARE NOT ELIGIBLE ")