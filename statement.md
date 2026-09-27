Project Statement: IQ & EQ Assessment Tool
Problem Statement

Most people have limited, informal ways of gauging their own cognitive reasoning ability (IQ) and emotional intelligence (EQ). Formal assessments are often expensive, time-consuming, or require professional administration, making them inaccessible for quick, everyday self-reflection. There is a need for a simple, free, and immediate way for individuals to test both their logical reasoning skills and their emotional/social decision-making, without needing specialized tools or supervision.

Scope of the Project

This project is a command-line based assessment application built in Python that allows a user to:

Take a 10-question IQ test covering logical, numerical, and pattern-based reasoning.
Take a 20-question EQ test covering realistic social and emotional scenarios.
Take both tests in a single session and receive a combined report.

The scope is limited to:

A single-user, single-session, text-based experience (no persistent storage, accounts, or history across sessions).
A fixed, pre-written question bank (questions and answers are not dynamically generated or externally sourced).
Local execution via a terminal/console — there is no web, GUI, or mobile interface.

Out of scope for this version:

User authentication or multi-user support.
Saving/exporting past results or generating historical trends.
Adaptive or randomized question selection.
Statistical validation against standardized/professional IQ or EQ testing models.
Target Users
Students and individuals curious about their reasoning and emotional intelligence in an informal, low-stakes setting.
Hobbyist learners and beginner developers who want a simple example project demonstrating menu-driven CLI logic in Python.
Educators or trainers who want a lightweight, no-installation-hassle tool to informally introduce the concepts of IQ and EQ during a workshop or class.
Recruiters or team leads looking for a casual, non-certified way to spark discussion around reasoning and emotional intelligence (not intended for formal hiring decisions).
High-Level Features
Personalized Greeting — Captures the user's name and tailors all messages throughout the session.
Menu-Driven Navigation — A simple, repeatable menu offering IQ Test, EQ Test, Both Tests, or Exit.
IQ Assessment Module — 10 multiple-choice questions with instant correct/incorrect feedback and a final score out of 10.
EQ Assessment Module — 20 scenario-based multiple-choice questions evaluating empathetic and socially intelligent responses, scored out of 20.
Combined Assessment & Report — Runs both tests sequentially and generates a consolidated summary of IQ and EQ scores.
Automatic Performance Grading — Converts raw scores into descriptive performance tiers (e.g., Superior, Above Average, Average, Below Average) for easier interpretation.
Graceful Exit — Allows the user to leave the application cleanly at any point from the main menu.