from iq_test import run_iq_questions
from eq_test import run_eq_questions
from both_tests import run_both_tests


n = input("Enter your name: ").strip()
print("\nHi " + n + ", welcome to the IQ and EQ Assessment Tool.")

while True:
    print("\n1. IQ Test (10 questions)")
    print("2. EQ Test (20 scenarios)")
    print("3. Both tests + report")
    print("4. Exit")

    choice = input("Pick an option (1-4): ").strip()

    if choice == '1':
        print("\nStarting IQ test for " + n)
        print("[+1 for correct, 0 for wrong]")
        run_iq_questions(n)

    elif choice == '2':
        print("\nStarting EQ test for " + n)
        run_eq_questions(n)

    elif choice == '3':
        run_both_tests(n)

    elif choice == '4':
        print("\nBye " + n + "!")
        break

    else:
        print("\nThat's not a valid option, try 1-4.")