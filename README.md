# LEARN-THAT-EXAM
For exam signing and learning your. Also you can sign to a dorm
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>selin.py — Code Viewer</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      background: radial-gradient(circle at top, #1e293b 0%, #0f172a 80%);
      color: #e2e8f0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      padding: 18px 22px;
      border-bottom: 1px solid rgba(226, 232, 240, 0.12);
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(12px);
    }

    header h1 {
      margin: 0;
      font-size: 1.4rem;
      letter-spacing: 0.03em;
    }

    header p {
      margin: 4px 0 0;
      opacity: 0.75;
      font-size: 0.95rem;
    }

    main {
      flex: 1;
      padding: 16px;
      overflow: auto;
    }

    .code-wrapper {
      max-width: 1100px;
      margin: 0 auto;
      border-radius: 16px;
      border: 1px solid rgba(226, 232, 240, 0.14);
      background: rgba(15, 23, 42, 0.68);
      box-shadow: 0 14px 26px rgba(0, 0, 0, 0.6);
      overflow: hidden;
    }

    pre {
      margin: 0;
      padding: 18px;
      overflow-x: auto;
      font-size: 0.92rem;
      line-height: 1.45;
      white-space: pre;
      tab-size: 4;
      color: #e2e8f0;
    }

    .toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 16px;
      background: rgba(30, 41, 59, 0.9);
      border-bottom: 1px solid rgba(226, 232, 240, 0.12);
      gap: 10px;
    }

    .toolbar button {
      padding: 8px 12px;
      border-radius: 10px;
      border: 1px solid rgba(226, 232, 240, 0.18);
      background: rgba(226, 232, 240, 0.06);
      color: #e2e8f0;
      cursor: pointer;
      font-weight: 600;
    }

    .toolbar button:hover {
      background: rgba(226, 232, 240, 0.11);
    }

    .toolbar span {
      opacity: 0.8;
      font-size: 0.9rem;
    }

    a {
      color: #a5b4fc;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .hint {
      padding: 14px 18px;
      background: rgba(226, 232, 240, 0.06);
      border-top: 1px solid rgba(226, 232, 240, 0.1);
      font-size: 0.9rem;
      opacity: 0.9;
      line-height: 1.5;
    }

    .hint a {
      color: #7dd3fc;
    }
  </style>
</head>
<body>
  <header>
    <h1>selin.py — code viewer</h1>
    <p>Displaying your script so you can copy or review it in the browser.</p>
  </header>

  <main>
    <div class="code-wrapper">
      <div class="toolbar">
        <span>Code file: <strong>selin.py</strong></span>
        <div>
          <button id="copyButton">Copy to clipboard</button>
          <button id="downloadButton">Download as .py</button>
        </div>
      </div>

      <pre id="codeBlock"></pre>

      <div class="hint">
        Tip: Use <strong>Ctrl+F</strong> to search in the code. If you want an editable version, open <code>selin.py</code> in an editor like Visual Studio Code.
        <br />
        If you run <code>python mail_server.py</code> and set up HTTPS (see the server instructions), you can open this page at <code>https://localhost:8000/selin.html</code>.
      </div>
    </div>
  </main>

  <script>
    const codeText = `#This codes belongs to SERRA SELİN AKPOLAT

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

print("  /\\------/\")
print(' /  \\    /  \\ ')

print("path:   C:User\\Exam and Homeworks")

print('Exam Score1\\nExam Score2')

print("YOUR EXAM PATH:
      \t-CHEMISTRIAL INDUSTRIES
      \t-PRE-INTERNING TEST
      \t-SAFETY AND HYGENE")
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
print(r"C:\\Users\\Lenovo\\Downloads\\indir (10).webp")


"""Simple local mail server for sending messages to a teacher.

Usage:

    Python mail_server.py

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

Feel free to add more quizzes by extending the 

    const codeBlock = document.getElementById('codeBlock');
    codeBlock.textContent = codeText;

    const copyButton = document.getElementById('copyButton');
    copyButton.addEventListener('click', () => {
      navigator.clipboard.writeText(codeText).then(() => {
        copyButton.textContent = 'Copied!';
        setTimeout(() => (copyButton.textContent = 'Copy to clipboard'), 1500);
      });
    });

    const downloadButton = document.getElementById('downloadButton');
    downloadButton.addEventListener('click', () => {
      const blob = new Blob([codeText], { type: 'text/x-python' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'selin.py';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  </script>
</body>
</html>

server = HTTPServer(('0.0.0.0', port), MailHandler)

server.socket = ssl.wrap_socket(
    server.socket,
    keyfile="key.pem",
    certfile="cert.pem",
    server_side=True,)""Simple local mail server for sending messages to a teacher.

Usage:
  python mail_server.py

Then open in your browser:
  http://localhost:8000/mail.html

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

To run HTTPS locally, create a self-signed certificate and key (example using OpenSSL):
  openssl req -x509 -nodes -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

Then set these environment variables:
  - HTTPS_CERT (path to cert.pem)
  - HTTPS_KEY  (path to key.pem)

When configured, the server will accept connections via https://localhost:8000
"""

import json
import os
import ssl
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
    print(' - Set TEACHER_EMAIL in your environment before running, e.g.:')
    print('     set TEACHER_EMAIL=teacher@example.com')
    print(' - For local debugging use:')
    print('     python -m smtpd -c DebuggingServer -n localhost:1025')

    cert_file = os.environ.get('HTTPS_CERT')
    key_file = os.environ.get('HTTPS_KEY')

    if cert_file and key_file:
        print(' - HTTPS enabled (using cert/key):', cert_file, key_file)
        protocol = 'https'
    else:
        print(' - HTTPS not configured. To enable, set HTTPS_CERT and HTTPS_KEY.')
        protocol = 'http'

    print(f' - Open {protocol}://localhost:{port}/mail.html in your browser')

    server = HTTPServer(('0.0.0.0', port), MailHandler)

    if cert_file and key_file:
        try:
            server.socket = ssl.wrap_socket(
                server.socket,
                keyfile=key_file,
                certfile=cert_file,
                server_side=True,
            )
        except Exception as ex:
            print('ERROR: Failed to wrap socket for HTTPS:', ex)
            print('Falling back to HTTP.')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        server.server_close()


if __name__ == '__main__':
    main()

import ssl
