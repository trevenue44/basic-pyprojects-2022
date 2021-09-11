import random

number_of_wrongs = 0
score = 0

while number_of_wrongs < 3:
    operation = random.choice(["+", "-"])
    question = f"{random.randint(-50, 50)} {operation} {random.randint(-50, 50)}"
    answer = eval(question)
    if int(input(f"Question: {question}\nAnswer: ")) == answer:
        print("Right!")
        score += 3
    else:
        print("Wrong...")
        number_of_wrongs += 1
    print()

print("3 answers wrong. Game Over")
print(f"Score: {score}")
