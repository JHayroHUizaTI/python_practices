list_numbers = input("list of number: ").split(", ")

for n in range(0, len(list_numbers)):
    list_numbers[n] = int(list_numbers[n])
print(list_numbers)

txt = "calculando"
print(txt.center(40, "="))
high_score = max(list_numbers)
print("the high score is: ", high_score)
