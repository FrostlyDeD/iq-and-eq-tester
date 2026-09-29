Problem Statement
Project: IQ and EQ Assessment Tool
The problem

A lot of people want to check how they do on logical thinking (IQ) and on handling emotions and people (EQ). Most of the quizzes online ask you to sign up, need internet, show ads, or do not explain how the score is worked out. Many of them also only test one of the two.

For someone learning programming, there is also not much choice of small projects that put together user input, loops, functions, multiple files and simple scoring rules in one working program.

Aim

To build a simple offline program in Python that:

Asks 10 multiple-choice IQ questions and gives feedback after each answer
Asks 20 situation-based EQ questions and gives a score at the end
Lets the user pick one test or both from a menu
Calculates the score with clear, easy rules and gives a rating such as Excellent, Good or Average
Prints a final report with both scores when both tests are taken
Scope

Included:

Terminal based menu program using only the Python standard library
10 fixed IQ questions and 20 fixed EQ questions, each with options A to D
Score of 1 point for each correct (or best) answer
Rating bands for both tests
Combined IQ and EQ report

Not included:

Real psychological or clinical testing of IQ or EQ
Login, user accounts or saving results
Graphical or web interface
Random or adaptive questions
How the program is organised
File	Purpose
main.py	Takes the user's name, shows the menu and calls the right function
iq_test.py	Runs the IQ test and returns the score (0 to 10)
eq_test.py	Runs the EQ test and returns the score (0 to 20)
both_tests.py	Runs both tests one after the other and prints the final report
Scoring

IQ out of 10: 9 to 10 Excellent, 7 to 8 Good, 4 to 6 Average, 1 to 3 Below average, 0 Needs practice.

EQ out of 20: 17 to 20 Excellent, 13 to 16 Good, 8 to 12 Average, 0 to 7 Needs practice.

Expected result

A program that anyone can run with python main.py without installing anything, and that gives them a quick idea of how they did in logical reasoning and in emotional situations. The scores are only for self-reflection and are not a proper test.