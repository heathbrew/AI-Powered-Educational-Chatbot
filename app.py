from flask import Flask, render_template, request, redirect, url_for
import csv
import openai
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

def check_credentials(username, password):
    with open('credentials.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == username and row[1] == password:
                return True
    return False

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

@app.route('/')
def index():
    return render_template('content.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password.'
    return render_template('signin.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/content')
def content():
    return render_template('content.html')

from helper import send_gptnew

@app.route('/chat_2', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat_2.html', question="NULL", res="Question can't be empty!",temperature="NULL")
        question = request.form['question']
        temperature = float(request.form['temperature'])
        print("======================================")
        print("Receive the question:", question)
        print("Receive the temperature:",temperature)
        res = send_gptnew(question.lower().title(),temperature)
        print("Q: \n", question)
        print("A: \n", res)

        return render_template('chat_2.html', question=question, res=str(res), temperature=temperature)
    return render_template('chat_2.html', question=0)

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/voice')
def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        prompt = r.recognize_google(audio)
        if prompt.lower() == "bye":
            print()
            print("Bye, tumharo din achha beete lala/lali")
        else:
            print("You said: " + prompt)
            bot_response = ask_gpt(prompt)
            print("Bot:", bot_response)

            engine = pyttsx3.init()
            engine.say(bot_response)
            engine.runAndWait()
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    return render_template('index2.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
