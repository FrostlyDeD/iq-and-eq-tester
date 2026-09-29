def run_iq_questions(n):
    sc = 0

  #
    print("\nQ1: What is the next number in the series: 5, 10, 15, 20, ...?")
    print("A) 22")
    print("B) 25")
    print("C) 30")
    print("D) 35")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'B':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was B)")

   #
    print("\nQ2: Which is the largest ocean on Earth?")
    print("A) Atlantic Ocean")
    print("B) Indian Ocean")
    print("C) Pacific Ocean")
    print("D) Arctic Ocean")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'C':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was C)")

  #
    print("\nQ3: What is 12 + 8 * 2?")
    print("A) 40")
    print("B) 28")
    print("C) 20")
    print("D) 32")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'B':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was B)")

  #
    print("\nQ4: Which of the following is the odd one out?")
    print("A) Piano")
    print("B) Guitar")
    print("C) Violin")
    print("D) Hammer")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'D':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was D)")

 #
    print("\nQ5: Hot is to Cold as Day is to...?")
    print("A) Sun")
    print("B) Night")
    print("C) Light")
    print("D) Morning")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'B':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was B)")

#
    print("\nQ6: What is the next number in the series: 1, 4, 9, 16, ...?")
    print("A) 20")
    print("B) 24")
    print("C) 25")
    print("D) 36")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'C':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was C)")

#
    print("\nQ7: If you are facing East and turn 180 degrees, which direction are you facing?")
    print("A) North")
    print("B) South")
    print("C) East")
    print("D) West")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'D':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was D)")

 # 
    print("\nQ8: What is 25% of 80?")
    print("A) 15")
    print("B) 20")
    print("C) 25")
    print("D) 40")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'B':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was B)")

#
    print("\nQ9: Which word does not belong with the others?")
    print("A) January")
    print("B) March")
    print("C) Monday")
    print("D) July")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'C':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was C)")

#
    print("\nQ10: If a car travels at 45 km/h, how far will it travel in 3 hours?")
    print("A) 90 km")
    print("B) 120 km")
    print("C) 135 km")
    print("D) 150 km")
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans == 'C':
        print("Correct! +1 point")
        sc += 1
    else:
        print("Incorrect! 0 points. (Correct answer was C)")

    print("\nIQ test done.")
    print(n + ", your IQ score is " + str(sc) + " out of 10.")

    if sc >= 9:
        print("Result: Excellent")
    elif sc >= 7:
        print("Result: Good")
    elif sc >= 4:
        print("Result: Average")
    elif sc >= 1:
        print("Result: Below average")
    else:
        print("Result: Needs practice")

    return sc