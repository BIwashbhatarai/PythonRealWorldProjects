from time import * 
import random as r

def mistake(paragraphtest, userTest):
    error = 0
    for i in range(len(paragraphtest)):
        try:
            if paragraphtest[i] != userTest[i]:
                error += 1
        except Exception as e:
            error += 1
    return error

 
def speed(s_time, e_time, testInput):
        time_delay = e_time - s_time
        time_r = round(time_delay,2)
        speed = (len(testInput)/ time_r)*60
        return round(speed)
    
while True:
    Words = ["The quick brown fox jumps over the lazy dog", "Hello world this is a typing speed test", "Practice makes a man perfect", "She sells seashells by the seashore every summer", "Programming challenges improve logical thinking skills", "Complex algorithms often require efficient data structures"]
    randomWord = r.choice(Words)
    print("     *****Typing speed*****")
    print("Sentence: ",randomWord) 
    input("Hit enter if you are ready")
    start_time = time()
    userinput = input("Enter: ")
    end_time = time()
    
    print(f"speed: {speed(start_time, end_time, userinput)} w/min" )
    print("Error: ",  mistake(randomWord, userinput))
    
    LeaveTest = input("Do you want to do more test? (y/n):")
    if LeaveTest.lower() != "y":
        print("Thanks for using our speed calculator app!")
        break