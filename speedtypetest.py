from time import *
import random as r
def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R=round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__== '__main__':
    while True:
        ck=input(" Ready to test : yes / no : ")
        if ck == "yes":

            test = ["The best error message is the one that never shows up","First, solve the problem. Then, write the code","Talk is cheap. Show me the code"]
            test1 = r.choice(test)
            print("         ******TYPING SPEED CALCULATOR*****")
            print("           Enter the given sentences")

            print(test1)
            print()
            print()
            time_1=time()
            testinput = input("Enter : ")
            time_2=time()

            print('speed: ',speed_time(time_1,time_2,testinput),"word/sec")
            print("Error: ",mistake(test1,testinput))
            print("HERE ERROR SHOW THAT HOW MANY WORDS ARE INCORRECT OR REPLACED OR NOT WRITTEN FROM THE GIVEN SENTENCES")

        elif ck == "no":
            print("Thank you for using speed type test ")
            break
        else:
            print("Wrong Input")
