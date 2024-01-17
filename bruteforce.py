import time
#Tells the final time it took to crack the password
def final_time(input_start, input_stop):

    finaltime = float(input_start)-float(input_stop)
    finaltime = float(round(finaltime,2) / -1)
    result = ""
    result += (str(finaltime))
    print("It took " + result + " seconds")

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
    splitTime = float(splitStart)-float(split)
    splitTime = float(round(splitTime,2) / -1)
    result = ""
    result += (str(splitTime))
    print("Time elapsed " + result + " seconds")

def brute_force():
    start_time()
    #Input password here, later I might make the program ask the user to input the password
    password = "asdfgh"
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
    while index1 < 36:
        first = alphabet[index1]

        split_time()
        print("Number of password tries = " + str(tryNmbr))
        print("----------------------------------------------------")

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
                                print("Password = " + password)
                                print("Guess = " + guess)
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
        index1 += 1
        tryNmbr += 1
        if(index2 == 36):
            index2 = 0
    stop_time()
brute_force()