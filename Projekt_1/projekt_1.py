'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

ODDELOVAC = "-"*39
x = 0
while x < len(TEXTS):
    TEXTS[x] = TEXTS[x].replace("\n", "")
    TEXTS[x] = TEXTS[x].strip(".")
    TEXTS[x] = TEXTS[x].split(" ")
    x += 1

LOGIN_DATA = {
 "bob": "123",
 "ann": "pass123",
 "mike": "password123",
 "liz": "pass123"}

# ============================================================
print(ODDELOVAC)
print("Welcome to the app. Please log in:")
USERNAME = input("USERNAME: ")
PASSWORD = input("PASSWORD: ")
print(ODDELOVAC)

if USERNAME not in LOGIN_DATA.keys() or not PASSWORD == LOGIN_DATA[USERNAME]:
    print("Incorrect username or password.")
    exit()
else:
    print("LOG IN succesful")

print(ODDELOVAC)
while bool:
    print(f"We have {len(TEXTS)} texts to be analyted.")
    USER_CHOICE_STR = input(f"Enter a number btw. 1 and {len(TEXTS)} : ")
    if USER_CHOICE_STR.isnumeric() and 1 <= int(USER_CHOICE_STR) <= len(TEXTS):
        break
    else:
        print(ODDELOVAC)
        print(f"Incorrect input, please insert number from 1 to {len(TEXTS)}")
        print(ODDELOVAC)
        print()
USER_CHOICE = int(USER_CHOICE_STR)-1

print(ODDELOVAC)

TEST1 = len(TEXTS[USER_CHOICE])
print(f"There are {TEST1} words in the selected text.")


TEST2 = 0
x = 0
while x < len(TEXTS[USER_CHOICE]):
    if TEXTS[USER_CHOICE][x].istitle():
        x += 1
        TEST2 += 1
    else:
        x += 1
print(f"There are {str(TEST2)} titlecase words.")

TEST3 = 0
x = 0
while x < len(TEXTS[USER_CHOICE]):
    if TEXTS[USER_CHOICE][x].isupper():
        x += 1
        TEST3 += 1
    else:
        x += 1
print(f"There are {TEST3} uppercase words.")

TEST4 = 0
x = 0
while x < len(TEXTS[USER_CHOICE]):
    if TEXTS[USER_CHOICE][x].islower():
        x += 1
        TEST4 += 1
    else:
        x += 1
print(f"There are {TEST4} lowercase words.")

TEST5 = 0
x = 0
while x < len(TEXTS[USER_CHOICE]):
    if TEXTS[USER_CHOICE][x].isnumeric():
        x += 1
        TEST5 += 1
    else:
        x += 1
print(f"There are {TEST5} numeric strings.")
print(ODDELOVAC)

WORD_LEN = 1
WORD_MAX_LEN = len(max(TEXTS[USER_CHOICE], key=len))
while WORD_LEN < WORD_MAX_LEN:
    WORD_INDEX = 0
    WORDS_COUNT = 0
    while WORD_INDEX < len(TEXTS[USER_CHOICE]):
        if len(TEXTS[USER_CHOICE][WORD_INDEX]) == WORD_LEN:
            WORDS_COUNT += 1
            WORD_INDEX += 1
        else:
            WORD_INDEX += 1
    STARS = "*"*WORDS_COUNT

    if WORDS_COUNT == 0:
        WORD_LEN += 1
    else:
        print(f"{WORD_LEN}{STARS}{WORDS_COUNT}")
        WORD_LEN += 1
print(ODDELOVAC)

NUMBERS_LIST = list()
x = 0
while x < len(TEXTS[USER_CHOICE]):
    if TEXTS[USER_CHOICE][x].isnumeric():
        NUMBERS_LIST.append(float(TEXTS[USER_CHOICE][x]))
        x += 1
    else:
        x += 1

SUM = sum(NUMBERS_LIST)
print(f"IF we summed all the numbers in this text we would get: {SUM}")
