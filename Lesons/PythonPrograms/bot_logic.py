import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923",":nerd:"]
    return random.choice(emodji)

def divideC(Number1, Number2):
    return Number1 / Number2 

def AddC(Number1, Number2):
    return Number1 + Number2 

def SubtractC(Number1, Number2):
    return Number1 - Number2 

def MultiplyC(Number1, Number2):
    return Number1 * Number2 

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"