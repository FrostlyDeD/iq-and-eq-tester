from iq_test import run_iq_questions
from eq_test import run_eq_questions


def run_both_tests(n):
    print("\n Running both tests for" + n)

    print("\n IQ test")
    iq = run_iq_questions(n)
    print("\n IQ score: " + str(iq) + "/10")

    print("\n EQ test")
    eq = run_eq_questions(n)
    print("\n EQ score: " + str(eq) + "/20")

    print("\n Final report")
    print(n + " - IQ: " + str(iq) + "/10")
    print(n + " - EQ: " + str(eq) + "/20")

    return iq, eq