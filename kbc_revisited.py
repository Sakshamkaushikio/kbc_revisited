print("Welcome to KBC\n\nanswer each question to win 10k per question")

ql = [["Question 1. What is the capital of India?","A. Mumbai","B. New Delhi","C. Kolkata","D. Chennai","b"],
        ["Question 2. How many days are there in a leap year?","A. 365","B. 366","C. 367","D. 368","b"],
        ["Question 3. Which planet is known as the Red Planet?","A. Venus","B. Jupiter","C. Mars","D. Saturn","c"],
        ["Question 4. Who is known as the Father of the Nation in India?","A. Jawaharlal Nehru","B. Subhas Chandra Bose","C. Bhagat Singh","D. Mahatma Gandhi","d"],
        ["Question 5. Which is the largest ocean in the world?","A. Atlantic Ocean","B. Indian Ocean","C. Pacific Ocean","D. Arctic Ocean","c"],
        ["Question 6. How many colours are there in a rainbow?","A. 5","B. 6","C. 7","D. 8","c"],
        ["Question 7. Which animal is known as the King of the Jungle?","A. Tiger","B. Lion","C. Elephant","D. Leopard","b"],
        ["Question 8. Which gas do plants absorb from the atmosphere?","A. Carbon dioxide","B. Nitrogen","C. Oxygen","D. Hydrogen","a"],
        ["Question 9. How many continents are there in the world?","A. 5","B. 6","C. 7","D. 8","c"],
        ["Question 10. Which is the national animal of India?","A. Lion","B. Elephant","C. Leopard","D. Bengal Tiger","d"]]

amt = 0

for i in ql:
    for j in i[0:5]:
        print(j)

    while True:
        choice = input("Enter your choice: ").strip().casefold()

        if choice in ["a", "b", "c", "d"]:
            break
        
        print("Invalid option! Try again.")

            
    if choice == i[5]:
        amt+=10000
        print(f"Bravo! correct answer,current amount = {amt}")
            
    else:
        print(f"That was a wrong answer, you're taking {amt} rupees home")   
        break
        
        
