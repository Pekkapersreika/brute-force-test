import time
#Tells the final time it took to crack the password
def final_time(input_start, input_stop):
    finalTime = (float(input_start)-float(input_stop)) / -1
    minuteString = str(finalTime / 60)  
    if(minuteString[0] != '-'):
        minutes = int(minuteString[0])
        tens = int(minuteString[0]) * 10
    seconds = finalTime
    result = str(finalTime)
    if(finalTime < 60):
        finalTime = round(finalTime,2)
        result = str(finalTime)
        print("It took " + result + " seconds")
    if(finalTime > 60 and finalTime < 600):
        print("It took " + str(minutes) + " minutes and " + str(round(seconds - float(60 * minutes))) + " seconds")
    if(finalTime > 600):
        print("It took " + str(tens) + " minutes and " + str(round(seconds - float(60 * tens))) + " seconds")

#Starts the timer
def start_time(event = None):
    global start
    start = time.time()

#Stops the timer
def stop_time(event = None):
    stop = time.time()
    final_time(start, stop)

#Split time
def split_time():
    split = time.time()
    final_split(start, split)

#Tells the user how much time has elapsed
def final_split(splitStart, split):
    splitTime = (float(splitStart)-float(split)) / -1
    minuteString = str(splitTime / 60)
    if(minuteString[0] != '-'):
        minutes = int(minuteString[0])
        tens = int(minuteString[0]) * 10
    seconds = splitTime
    result = str(splitTime)
    if(splitTime < 60):
        splitTime = round(splitTime,2)
        result = str(splitTime)
        print("Time elapsed " + result + " seconds")
    if(splitTime > 60 and splitTime < 600):
        print("Time elapsed " + str(minutes) + " minutes and " + str(round(seconds - float(60 * minutes))) + " seconds")
    if(splitTime > 600):
        print("Time elapsed " + str(tens) + " minutes and " + str(round(seconds - float(60 * tens))) + " seconds")

def choose_complexity():
    selection = input("Select complexity:\n1: Basic\n2: Advanced\n3: Complex\n")
    print("----------------------------------------------------")
    if(selection == "1"):
        brute_force_basic()
    if(selection == "2"):
        brute_force_nmbrs()
    if(selection == "3"):
        brute_force_complex()

def brute_force_basic():
    password = input("Enter password: (six lowercase letters)\n")
    print("----------------------------------------------------")
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0
    index6 = 0
    tryNmbr = 0
    alphabet = ["a", "b", "c", "d",
                "e", "f", "g", "h",
                "i", "j", "k", "l",
                "m", "n", "o", "p",
                "q", "r", "s", "t",
                "u", "v", "w", "x",
                "y", "z"]
    start_time()
    while index1 < 26:
        first = alphabet[index1]

        split_time()
        print("Number of tried passwords = " + str(tryNmbr))
        print("----------------------------------------------------")
        print("Loading...", end="\r")

        while index2 < 26:
            second = alphabet[index2]
            index2 += 1

            while index3 < 26:
                third = alphabet[index3]
                index3 += 1
                guess = first + second + third
                
                while index4 < 26:
                    fourth = alphabet[index4]
                    index4 += 1

                    while index5 < 26:
                        fifth = alphabet[index5]
                        index5 += 1

                        while index6 < 26:
                            sixth = alphabet[index6]
                            index6 += 1
                            guess = first + second + third + fourth + fifth + sixth
                            tryNmbr += 1

                            if(guess == password):
                                print("Success")
                                print("Password = " + guess)
                                print("Number of tried passwords = " + str(tryNmbr))
                                print("----------------------------------------------------")
                                index1 = 26
                                index2 = 26
                                index3 = 26
                                index4 = 26
                                index5 = 26
                                index6 = 26
                        tryNmbr += 1
                        if(index6 == 26):
                            index6 = 0
                    tryNmbr += 1
                    if(index5 == 26):
                        index5 = 0
                tryNmbr += 1
                if(index4 == 26):
                    index4 = 0
            tryNmbr += 1
            if(index3 == 26):
                index3 = 0
        tryNmbr += 1
        if(index2 == 26):
            index2 = 0
        index1 += 1
    stop_time()

def brute_force_nmbrs():
    password = input("Enter password: (six lowercase letters and/or numbers)\n")
    print("----------------------------------------------------")
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0
    index6 = 0
    tryNmbr = 0
    alphabet = ["a", "b", "c", "d",
                "e", "f", "g", "h",
                "i", "j", "k", "l",
                "m", "n", "o", "p",
                "q", "r", "s", "t",
                "u", "v", "w", "x",
                "y", "z", "0", "1",
                "2", "3", "4", "5",
                "6", "7", "8", "9"]
    start_time()
    while index1 < 36:
        first = alphabet[index1]

        split_time()
        print("Number of tried passwords = " + str(tryNmbr))
        print("----------------------------------------------------")
        print("Loading...", end="\r")

        while index2 < 36:
            second = alphabet[index2]
            index2 += 1

            while index3 < 36:
                third = alphabet[index3]
                index3 += 1
                guess = first + second + third
                
                while index4 < 36:
                    fourth = alphabet[index4]
                    index4 += 1

                    while index5 < 36:
                        fifth = alphabet[index5]
                        index5 += 1

                        while index6 < 36:
                            sixth = alphabet[index6]
                            index6 += 1
                            guess = first + second + third + fourth + fifth + sixth
                            tryNmbr += 1

                            if(guess == password):
                                print("Success")
                                print("Password = " + guess)
                                print("Number of tried passwords = " + str(tryNmbr))
                                print("----------------------------------------------------")
                                index1 = 36
                                index2 = 36
                                index3 = 36
                                index4 = 36
                                index5 = 36
                                index6 = 36
                        tryNmbr += 1
                        if(index6 == 36):
                            index6 = 0
                    tryNmbr += 1
                    if(index5 == 36):
                        index5 = 0
                tryNmbr += 1
                if(index4 == 36):
                    index4 = 0
            tryNmbr += 1
            if(index3 == 36):
                index3 = 0
        tryNmbr += 1
        if(index2 == 36):
            index2 = 0
        index1 += 1
    stop_time()

def brute_force_complex():
    password = input("Enter password: (six letters and/or numbers)\n")
    print("----------------------------------------------------")
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0
    index6 = 0
    tryNmbr = 0
    alphabet = ["a", "b", "c", "d",
                "e", "f", "g", "h",
                "i", "j", "k", "l",
                "m", "n", "o", "p",
                "q", "r", "s", "t",
                "u", "v", "w", "x",
                "y", "z", "0", "1",
                "2", "3", "4", "5",
                "6", "7", "8", "9",
                "A", "B", "C", "D",
                "E", "F", "G", "H",
                "I", "J", "K", "L",
                "M", "N", "O", "P",
                "Q", "R", "S", "T",
                "U", "V", "W", "X",
                "Y", "Z"]
    start_time()
    while index1 < 62:
        first = alphabet[index1]

        split_time()
        print("Number of tried passwords = " + str(tryNmbr))
        print("----------------------------------------------------")
        print("Loading...", end="\r")

        while index2 < 62:
            second = alphabet[index2]
            index2 += 1

            while index3 < 62:
                third = alphabet[index3]
                index3 += 1
                guess = first + second + third
                
                while index4 < 62:
                    fourth = alphabet[index4]
                    index4 += 1

                    while index5 < 62:
                        fifth = alphabet[index5]
                        index5 += 1

                        while index6 < 62:
                            sixth = alphabet[index6]
                            index6 += 1
                            guess = first + second + third + fourth + fifth + sixth
                            tryNmbr += 1

                            if(guess == password):
                                print("Success")
                                print("Password = " + guess)
                                print("Number of tried passwords = " + str(tryNmbr))
                                print("----------------------------------------------------")
                                index1 = 62
                                index2 = 62
                                index3 = 62
                                index4 = 62
                                index5 = 62
                                index6 = 62
                        tryNmbr += 1
                        if(index6 == 62):
                            index6 = 0
                    tryNmbr += 1
                    if(index5 == 62):
                        index5 = 0
                tryNmbr += 1
                if(index4 == 62):
                    index4 = 0
            tryNmbr += 1
            if(index3 == 62):
                index3 = 0
        tryNmbr += 1
        if(index2 == 62):
            index2 = 0
        index1 += 1
    stop_time()
choose_complexity()
