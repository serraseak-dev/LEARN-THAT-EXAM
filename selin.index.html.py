<DOCTYPE>
<HTTPServer

#This codes belongs to SERRA SELİN AKPOLAT

# This is an Multi-Line comment
#1. Create user name
#2. Prin message to user
#3. Store data
from email.mime import image


print("The exam scores will be relased")

#  Store the final exam score
x=100
y=90  #final exam score

print("This is an site for exam scores and homeworks but you can also send messages to the theachers and editors")
print('Please do not send something about your exam score to the teachers you can press the "re-check my exam button"')

print('-------------------------------------------------------')
print('                 RE-CHECK MY EXAM                      ')
print('-------------------------------------------------------')

print("  /\------/\ ")
print(' /  \    /  \ ')

print("path:   C:User\\Exam and Homeworks")

print('Exam Score1\nExam Score2')

print("""YOUR EXAM PATH:
      \t-CHEMISTRIAL INDUSTRIES
      \t-PRE-INTERNING TEST
      \t-SAFETY AND HYGENE""")
name= 96
print("FIRST EXAM:" , name)
x= 86
print ("SECOND EXAM" , x)
y= 97
print("THIRD EXAM:"  , y)


print("This is an web for the students at the med-school only")

print('------------------------------------')
print('         EXAM APPLICATIONS        ')
print('------------------------------------')

name= input("Exam name:")
name= input("ID:")
name=input ("STUDENT NAME")
print(name, 'is applicated to the exam. Congrats and good luck!')

a = 93  #int
b = 86.8 #float
c = "PASS" #str
d = True #bool
e = False #bool



text = "PLEASE FOLLOW THE MESSAGES SENT BY TEACHER"
number= 12
print(text)
print ("Message will be sent after", number, 'messages')

print ("     STUDENT İNFORMATION FOR THE PHYSICAL CLASSES   ")
name=input("AGE:")
name=input("HEIGT WITH DECIMALS:")
name=input("NAME:")
name=input("WEIGHT:")
name=input("Internıng for:")

print("PLEASE TALK WITH YOUR TEACHER ABOUT THE SICKNESSES THAT CAUSES PHISICHAL PROBLEMS WHEN YOU MOVE")



password = input ("Password")
print (len(password))

if len(password) < 8:
    print("YOUR PASSWORD SHOULD BE LONGER THEN EIGHT DIGITS!!!!" \
    "")

print("SIGN UP TO THE DORMS")
age =int(input("AGE:"))


if age >= 25 or age <= 17:
        print("SORRY, YOU CAN NOT SIGN UP TO THE DORMS BECAUSE THE DORMS ARE FOR THE YOUNG AND AVVERAGE OLD STUDENTS")
else:
        print("CONGRATS, YOU CAN SIGN UP TO THE DORMS")
        name = input("NAME:")
        print(name, "YOU ARE SIGNED UP TO THE DORMS")
        print("YOU CAN CONNTACT FOR CHANGING YOUR ROOM FRIENDS OR ANY PROBLEMS ABOUT THE DORMS TO THE DORMITORY MANAGER")
print("CONTACT NUMBER: 0(530)970-13 19")
print(r"C:\Users\Lenovo\Downloads\indir (10).webp")


"""Simple local mail server for sending messages to a teacher.

Usage:
  python mail_server.py

Then open in your browser:
  https://localhost:8000/mail.html

Configuration (recommended):
  Set environment variables to avoid hardcoding credentials:
    - TEACHER_EMAIL (required)
    - SMTP_HOST (default: localhost)
    - SMTP_PORT (default: 1025)
    - SMTP_USER (optional)
    - SMTP_PASS (optional)

For local development you can run a debug SMTP server with:
  python -m smtpd -c DebuggingServer -n localhost:1025

The debug server prints outgoing messages to the terminal without sending them.
"""

import json
import os
import smtplib
from http.server import HTTPServer, SimpleHTTPRequestHandler

TEACHER_EMAIL = os.environ.get('TEACHER_EMAIL')
SMTP_HOST = os.environ.get('SMTP_HOST', 'localhost')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '1025'))
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASS = os.environ.get('SMTP_PASS')


class MailHandler(SimpleHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != '/send':
            self.send_error(404, 'Not found')
            return

        if TEACHER_EMAIL is None:
            self._send_json({'error': 'TEACHER_EMAIL is not configured.'}, status=500)
            return

        length = int(self.headers.get('Content-Length', '0'))
        raw = self.rfile.read(length).decode('utf-8')
        try:
            payload = json.loads(raw)
        except Exception as ex:
            self._send_json({'error': 'Invalid JSON payload: ' + str(ex)}, status=400)
            return

        for required in ('fromName', 'fromEmail', 'subject', 'message'):
            if not payload.get(required):
                self._send_json({'error': f'Missing required field: {required}'}, status=400)
                return

        from_name = payload['fromName'].strip()
        from_email = payload['fromEmail'].strip()
        subject = payload['subject'].strip()
        message = payload['message'].strip()

        full_message = (
            f"From: {from_name} <{from_email}>\n"
            f"To: {TEACHER_EMAIL}\n"
            f"Subject: {subject}\n\n"
            f"{message}\n"
        )

        try:
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
                smtp.ehlo()
                if SMTP_USER and SMTP_PASS:
                    smtp.starttls()
                    smtp.login(SMTP_USER, SMTP_PASS)
                smtp.sendmail(from_email, [TEACHER_EMAIL], full_message)
        except Exception as ex:
            self._send_json({'error': 'Mail send failed: ' + str(ex)}, status=502)
            return

        self._send_json({'ok': True})


def main():
    port = 8000
    print('Starting local mail server...')
    print(' - Open https://localhost:%d/mail.html in your browser' % port)
    print(' - Set TEACHER_EMAIL in your environment before running, e.g.:')
    print('     set TEACHER_EMAIL=teacher@example.com')
    print(' - For local debugging use:')
    print('     python -m smtpd -c DebuggingServer -n localhost:1025')

    server = HTTPServer(('0.0.0.0', port), MailHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        server.server_close()


if __name__ == '__main__':
    main()


"""University Practice Test Runner

This script provides several short practice quizzes for common university subjects.
Run it from the command line and choose which quiz to take.

Usage:
  python practice_tests.py

Features:
  - Multiple-choice questions
  - Immediate feedback
  - Score summary at the end

Feel free to add more quizzes by extending the `QUIZZES` data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Question:
    prompt: str
    options: List[str]
    answer: str  # correct option letter (A/B/C/D)


@dataclass
class Quiz:
    title: str
    questions: List[Question]


QUIZZES: List[Quiz] = [
    Quiz(
        title="Biology: Cell Biology",
        questions=[
            Question(
                prompt="Which organelle is responsible for producing ATP?",
                options=[
                    "A) Ribosome",
                    "B) Mitochondrion",
                    "C) Golgi apparatus",
                    "D) Endoplasmic reticulum",
                ],
                answer="B",
            ),
            Question(
                prompt="What is the primary function of the cell membrane?",
                options=[
                    "A) Store genetic information",
                    "B) Produce proteins",
                    "C) Control what enters and leaves the cell",
                    "D) Provide cellular energy",
                ],
                answer="C",
            ),
            Question(
                prompt="Which type of molecule carries genetic information?",
                options=[
                    "A) Carbohydrate",
                    "B) Lipid",
                    "C) Nucleic acid",
                    "D) Protein",
                ],
                answer="C",
            ),
        ],
    ),
    Quiz(
        title="Physics: Mechanics",
        questions=[
            Question(
                prompt="A 2-kg object is accelerated at 3 m/s². What is the net force on the object?",
                options=[
                    "A) 1.5 N",
                    "B) 3 N",
                    "C) 6 N",
                    "D) 9 N",
                ],
                answer="C",
            ),
            Question(
                prompt="Which quantity is a vector?",
                options=[
                    "A) Mass",
                    "B) Speed",
                    "C) Distance",
                    "D) Velocity",
                ],
                answer="D",
            ),
            Question(
                prompt="If an object moves in a circle at constant speed, what is true about its acceleration?",
                options=[
                    "A) It is zero",
                    "B) It points tangent to the circle",
                    "C) It points toward the center of the circle",
                    "D) It is constant in direction",
                ],
                answer="C",
            ),
        ],
    ),
    Quiz(
        title="Computer Science: Basics",
        questions=[
            Question(
                prompt="What does CPU stand for?",
                options=[
                    "A) Central Processing Unit",
                    "B) Computer Programming Unit",
                    "C) Central Program Utility",
                    "D) Core Processing Unit",
                ],
                answer="A",
            ),
            Question(
                prompt="Which data structure uses LIFO ordering?",
                options=[
                    "A) Queue",
                    "B) Stack",
                    "C) Tree",
                    "D) Hash table",
                ],
                answer="B",
            ),
            Question(
                prompt="In Python, which keyword is used to create a function?",
                options=[
                    "A) func",
                    "B) def",
                    "C) function",
                    "D) lambda",
                ],
                answer="B",
            ),
        ],
    ),
]


def ask_choice(prompt: str, choices: List[str]) -> str:
    """Ask the user to choose from a list of options."""
    print(prompt)
    for idx, choice in enumerate(choices, start=1):
        print(f"  {idx}) {choice}")

    while True:
        selected = input("Enter the number of your choice: ").strip()
        if not selected.isdigit():
            print("Please enter a number.")
            continue
        index = int(selected) - 1
        if 0 <= index < len(choices):
            return choices[index]
        print(f"Please choose a number between 1 and {len(choices)}.")


def run_quiz(quiz: Quiz) -> Tuple[int, int]:
    """Run a single quiz and return (score, total)."""
    print(f"\n=== {quiz.title} ===\n")
    score = 0
    total = len(quiz.questions)

    for idx, q in enumerate(quiz.questions, start=1):
        print(f"Question {idx}/{total}: {q.prompt}")
        for option in q.options:
            print(f"  {option}")

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in {"A", "B", "C", "D"}:
                break
            print("Please answer with A, B, C, or D.")

        if answer == q.answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {q.answer}\n")

    return score, total


def main() -> None:
    print("University Practice Test Runner")

    quiz_titles = [quiz.title for quiz in QUIZZES]
    chosen_title = ask_choice("Choose a quiz:", quiz_titles)
    chosen_quiz = next(q for q in QUIZZES if q.title == chosen_title)

    score, total = run_quiz(chosen_quiz)

    print(f"Your score: {score}/{total} ({score/total*100:.0f}% )")
    if score == total:
        print("🎉 Great job! You got a perfect score.")
    elif score >= total * 0.7:
        print("👍 Good work — keep practicing to improve.")
    else:
        print("📘 Review the material and try again.")


if __name__ == "__main__":
    main()
