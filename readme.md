IQ and EQ Assessment Tool

This is a small Python program I made that runs in the terminal. You can take a short IQ quiz, an EQ quiz, or both one after the other and see your scores at the end. It has no extra libraries, no internet needed and nothing is saved anywhere.

The "IQ score" here is just how many of the 10 questions you got right. It is not a real IQ value, and the EQ result is only meant for fun and self-reflection.

What it does
Asks for your name and greets you
Shows a menu: IQ test, EQ test, both tests with a report, or exit
IQ test: 10 multiple-choice questions (number series, simple maths, odd one out, analogy, direction, percentage, speed and distance). It tells you right away if your answer was correct and shows the right option when you get one wrong.
EQ test: 20 everyday situations, each with 4 choices. It does not show which answer was best while you are going, only your score at the end.
Both tests: runs the IQ test, then the EQ test, then prints both scores together
Answers are not case sensitive, so b, B and b all work
If you type a wrong menu option it just tells you and shows the menu again
Files
main.py         menu and main loop (run this one)
iq_test.py      run_iq_questions(n)
eq_test.py      run_eq_questions(n)
both_tests.py   run_both_tests(n)

main.py imports the other three files. The IQ and EQ functions return the score, and run_both_tests uses those returned scores to print the final report.

How to run

You need Python 3 installed. Put all four files in the same folder, then run:

python main.py

(On some computers the command is python3 main.py.)

Type the menu number and press Enter. For each question, type A, B, C or D.

Example
Enter your name: Aarav

Hi Aarav, welcome to the IQ and EQ Assessment Tool.

1. IQ Test (10 questions)
2. EQ Test (20 scenarios)
3. Both tests + report
4. Exit
Pick an option (1-4): 1

Starting IQ test for Aarav
[+1 for correct, 0 for wrong]

Q1: What is the next number in the series: 5, 10, 15, 20, ...?
A) 22
B) 25
C) 30
D) 35
Your answer (A/B/C/D): B
Correct! +1 point

At the end of a test you get something like:

IQ test done.
Aarav, your IQ score is 8 out of 10.
Result: Good
How the scoring works

Each correct answer is 1 point. In the EQ test, the correct answer is the most mature and considerate response in the situation.

IQ (out of 10):

Score	Result
9 to 10	Excellent
7 to 8	Good
4 to 6	Average
1 to 3	Below average
0	Needs practice

EQ (out of 20):

Score	Result
17 to 20	Excellent
13 to 16	Good
8 to 12	Average
0 to 7	Needs practice
Things that could be better
The questions are written out one by one, so the code is long and repeats a lot. It would be neater to keep the questions in a list or a JSON file and use a loop.
Questions always come in the same order.
If you type something that is not A, B, C or D, it counts as wrong instead of asking again.
Scores are not saved, so there is no history.
The score bands are my own choice and are not based on any real psychology scale.
Ideas for later
Load questions from a file and shuffle them
Ask again when the answer is invalid
Save results to a file or a database
Break the EQ score into parts like empathy and self-control
Add a simple GUI
Author

[Jaivardhan singh kaurav] [Course / College]