import speech_recognition as sr
import random
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia
import smtplib
from translate import Translator

print(
        "\n----------------------------------------------------------------------------------------------------------------------")
print("for  telugu  te,\nfor  tamil  Ta,\nfor  English  En,\nfor  hindi  hi")
print(
        "\n----------------------------------------------------------------------------------------------------------------------")

Name = input('Type your name : ')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def tell(voice):
    engine.say(voice)
    engine.runAndWait()

def play1():
    print(
        "\n----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print(" Choose           R   for  Rock"
          "\n                  P   for  paper"
          "\n                  S   for  scissor"
          "\n Q to quit ")

    print(
        "\n----------------------------------------------------------------------------------------------------------------------")

    # code start

    '''user_input = 0
    computer_input = 0'''
    computer_score = 0
    user_score = 0
    options = ['r', 'p', 's']

    while True:

        user_input = input("\nyour choice : ")
        if user_input == "q":
            break

        if user_input not in options:
            continue
        random_number = random.randint(0, 2)

        # rock:0 paper:1 scissor:2

        computer_pick = options[random_number]

        print("computer picked", computer_pick + ".")

        if user_input == 'p' and computer_pick == 'r':
            print('\nYou won')
            user_score += 1
            print(
                "\n----------------------------------------------------------------------------------------------------------------------")


        elif user_input == 's' and computer_pick == 'p':
            print('\nYou won')
            user_score += 1
            print(
                "\n----------------------------------------------------------------------------------------------------------------------")

        elif user_input == 'r' and computer_pick == 's':
            print('\nYou won')
            user_score += 1
            print(
                "\n----------------------------------------------------------------------------------------------------------------------")

        else:
            print("computer won!")
            print(
                "\n----------------------------------------------------------------------------------------------------------------------")
            computer_score += 1
    print("you win ", + user_score, "times")
    print("computer won ", + computer_score, "times")
    print("good bye!")


def play():
    print(
        "\n----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print(" Choose    numbers    from     "
          "1 TO 6  for play game "
          "0 TO quit"
          "  ")
    print('\nEnter    7   for  Quit ')

    print(
        "\n----------------------------------------------------------------------------------------------------------------------")
    tell(" enter your name ")
    Name = trans().lower()



    score1 = 0
    count = 1
    options = [1, 2, 3, 4, 5, 6]
    while True:
        print('you are playing from ', count, 'times')
        user_input = (input("Your choice : "))
        if user_input.isalpha():
            tell(f"enter the valid number{Name}")
        else:
            user_input = int(user_input)
        if user_input == 7:
            break
        if user_input not in range(0, 8) and user_input == ' ':
            tell("enter the valid number ")
            continue

        random_number = random.randint(0, 5)

        computer_pick = options[random_number]

        print("Computer choice : ", computer_pick)

        # scoring

        if user_input != computer_pick:
            score1 += user_input
            count += 1
            print(' your score', score1)
            tell(f'{Name},your score is {score1} ')
            print(
                "\n----------------------------------------------------------------------------------------------------------------------")


        else:
            score = 0
            print(' your score', score)
            tell(f'{Name}, your score is {score},you lost the match')

            tell(f'{Name} ,your final score is {score1} ')


            print(" -------------------------------<-----Out!----->------------------------------- ")
            break
    print('0 for replay the game')
    print(f'{Name},your final score is  ', score1)
    print(
        "\n----------------------------------------------------------------------------------------------------------------------")

def eml():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        tell('tell me your email id')
        command = trans().lower()
        server.starttls()
        command = command.replace(" ", "")
        user_mail = command+'@gmail.com'
        print(user_mail)
        tell('Enter your password')
        password = input('Enter your email password : ')
        server.login(user_mail, password)
        print('login complete...')

        tell('tell me receiver email id')
        command = trans().lower()
        command = command.replace(" ", "")
        receiver = command + '@gmail.com'
        print(receiver)
        tell('tell me what the information you want to send : ')
        command = trans().lower()
        text = command
        server.login(user_mail, password)
        server.sendmail(user_mail, receiver, text)
        tell('email sent')
        print('mail sent')
    except Exception as err:
        tell('enter correct details..')
        print(err)

    return 'None'



def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        tell(f"Good Morning!,{Name}")

    elif 12 <= hour < 18:
        tell(f"Good Afternoon!,{Name}")

    else:
        tell(f"Good Evening!,{Name}")


    tell('You can call me as,anand')

your_language = input('Enter you speaking language : ')
print(
        "\n----------------------------------------------------------------------------------------------------------------------")




def cmd():

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('listening...')
        recordedaudio = recognizer.listen(source, timeout=10)

        print('done recording')

    try:
        command = recognizer.recognize_google(recordedaudio, language=your_language)
        print(f'Your message:{command}')
        print(
            "\n----------------------------------------------------------------------------------------------------------------------")


    except Exception as ex:
        print(ex)
        return 'None'

    return command


def trans():
    command = cmd()
    translator = Translator(from_lang=your_language, to_lang="en")
    translation_text = translator.translate(command)
    print(f"After translation : {translation_text}")
    print(
        "\n----------------------------------------------------------------------------------------------------------------------")
    return translation_text


def run_assistant():
    wishme()

    tell('tell me how may i, help you')
    while True:

        command = trans().lower()

        if 'open google' in command:
            a = 'opening google...'
            tell(a)

            webbrowser.open("google.com")

        elif 'whatsapp' in command:
            a = 'opening whatsapp'
            tell(a)
            webbrowser.open('https://web.whatsapp.com/')

        elif 'chrome' in command:
            tell('opening chrome..')
            program = "c:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([program])
        elif 'open youtube' in command:
            tell('opening youtube...')
            webbrowser.open('https://www.youtube.com/')

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M")
            tell(f"Sir, the time is {strTime}")

        elif 'search ' in command and 'google' in command:
            tell('searching..., ')
            command = command.replace('in google', '')
            command = command.replace('search', '')
            pywhatkit.search(command)
            tell('done sir')

        elif 'wikipedia' in command:
            tell('searching in wikipedia...')
            command = command.replace('wikipedia', '')
            command = command.replace('search', '')
            command = command.replace('in', '')
            results = wikipedia.summary(command, sentences=5)
            tell('according to wikipedia...')
            print(results)
            tell(results)

        elif 'send' in command or 'email' in command:
            eml()

        elif 'play a game' in command or 'game' in command:
            tell('what game do you want to play..')
            command = trans().lower()
            if 'hand cricket' in command or 'cricket' in command:
                play()
            else:
                play1()

        elif 'play' in command and 'video' in command:
            command = command.replace('in youtube', '')
            command = command.replace('play', '')
            tell(' searching in youtube')
            tell('here the list of videos')
            webbrowser.open('https://www.youtube.com/results?search_query=' + command)

        elif 'open youtube' in command:
            tell('opening youtube...')
            webbrowser.open('https://www.youtube.com')

        elif 'music' in command:
            tell("Tell the name")
            musicName = cmd()
            pywhatkit.playonyt(musicName)
        elif 'website' in command:

            command = command.replace("anand", "")
            command = command.replace("website", "")
            web1 = command.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            tell('Launching' + web1 + ' Sir')
            webbrowser.open(web2)
            tell("launched sir")

        elif'bye' in command or 'bhai' in command:
            tell('thank you , sir,i hope you like this')
            break

        else:
            continue



run_assistant()