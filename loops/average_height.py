logo = """

        .__                         .___ 
__  _  _|__|____________ _______  __| _/ 
\ \/ \/ /  \___   /\__  \\_  __ \/ __ |  
 \     /|  |/    /  / __ \|  | \/ /_/ |  
  \/\_/ |__/_____ \(____  /__|  \____ |  
                 \/     \/           \/  

"""

print(logo)
student_heights = input("Input a list of student height: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
txt = "Calculando"
print(txt.center(40, "="))

total_height = 0
for height in student_heights:
    total_height += height
number_of_student = len(student_heights)

average_height = round(total_height / number_of_student)

print("average total is: ", average_height)
