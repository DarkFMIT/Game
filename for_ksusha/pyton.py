import os
cor = 0
incor = 0
done = True
file = open("./names_of_test", "r+")
while done:
    try:
        str = file.readline()
        os.system(f".\\main.exe {str} >.\\tmp.txt 2>&1")
        correct_results = open(f"./correct/correct_for_{str}", "r+")
        my_results = open("./tmp.txt")
        done1 = True
        while done1:
            try:
                correct = correct_results.readline()
                tmp = my_results.readline()
                if correct != tmp:
                    incor += 1
                    done1 = True
                    correct_results.close()
                    my_results.close
            finally:
                done1 = False
                cor += 1
                correct_results.close()
                my_results.close

    finally:
        done = False
        file.close()
print(f"Correct: {cor}, Incorrect: {incor}")