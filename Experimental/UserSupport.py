import time,sys,os,random
 
def typingPrint(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
  
def typingInput(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
    value = input()  
    return value

def clearScreen():
    os.system("clear")

#Correct answers increase score
score = 0
#Competence rewards first time correct answers
competence = 0
#Certain answers are learning experiences; unlocks some elements
skill = 0 
#Who said daring couldn't get you anywhere? Increased by out-of-the-box thinking
guts = 0
#The answer to each prompt
answer = None

def correct(n):
    attempt = 0
    x = False
    while x is False:
        if n == answer:
            score += 1
            if attempt == 0:
                competence += 1
            x = True
        else: 
            n = typingInput("Perhaps you should try that again.\n What would you like to do?: ")
        attempt += 1

name = typingInput("What is your name?: ")
time.sleep(1)
typingPrint(f"{name}.")
time.sleep(1)
typingPrint(f"\nHello, {name}.")
time.sleep(3)
clearScreen()

time.sleep(1)
typingPrint(f"{name}, it is your first night on the job but I'm afraid your trainer is unavailable.")
time.sleep(1)
typingPrint("\nInstead, I will be helping you as you resolve user tickets tonight.\n\nFor help, simply type HELP. Do you understand?")

def HELP(n):
    helpme = n
    helpcompetence = 0
    if score <= 0 and helpme == 0:
        return f'Yes, you do need help, {name}. Unfortunately, I am unqualified to provide it.'
    if score > 0 and helpme == 0:
        return "No, you're fine. Keep going."
    if 4 > helpme > 0:
        return "Now you're just being needy."
    if helpme == 4:
        return f"{name}."
    if helpme == 5:
        return "I'm beginning to think you're trying to be annoying."
    if 10 > helpme > 5: 
        return "THIS FUNCTION HAS BEEN DISABLED"
    if helpme == 10:
        return "No."
    if helpme > 10:
        return "ERROR"
    helpme += 1
    

response = typingInput("\nResponse (Y/N/HELP): ")
x = False

while x is False:
    if response == "Y":
        typingPrint("Good. We will proceed.\n")
        x = True
    elif response == "N": 
        typingPrint("What don't you understand? Never mind. I'm sure you'll figure it out.\n")
        x = True
    elif response == "HELP":
        typingPrint(f"{HELP(0)}\nPlease try again.")
        response = typingInput("\nResponse (Y/N/HELP): ")
    else:
        response = typingInput("Try typing more slowly.\nResponse (Y/N/HELP): ")

time.sleep(1)
typingPrint(f"Now that we are on the same page, {name}, I will present your first ticket.\n\nSince you are new, you are only expected to DISMISS, REPLY, or ESCALATE.")
time.sleep(1)
typingPrint(" DISMISS if the ticket should not be in the queue.")
time.sleep(1)
typingPrint(" REPLY if you can resolve the issue immediately.")
time.sleep(1)
typingPrint(" ESCALATE if you cannot DISMISS or REPLY.")
time.sleep(1)
clearScreen()

time.sleep(1)
typingPrint("For the first ticket, I will guide you. Let's begin.")
time.sleep(1)
typingPrint("\nProcessing .")
time.sleep(1)
typingPrint(" .")
time.sleep(1)
typingPrint(" .")
time.sleep(2)
clearScreen()

time.sleep(1)
typingPrint("*"*43)
typingPrint("\n*"+" "*10+"WELCOME TO TICKETCORP"+" "*10+"*\n")
typingPrint("*"*43)
time.sleep(4)
clearScreen()

ticket1 = random.randint(1000,9999)
typingPrint(f"TICKET #{ticket1}\n\n")
time.sleep(2)

typingPrint("Helpmyspacebardoesn'tworkhowdoIspace?")
time.sleep(2)
answer = typingInput("\n\nHow would you like to respond? (DISMISS/REPLY/ESCALATE/HELP): ")
#Tutorial to answer ticket

