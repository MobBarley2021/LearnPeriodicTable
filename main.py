import random
import pandas as pd


class colors:
    GREEN = '\u001b[32m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

wrong = []
correct = 0
take = input("How many of the first n elements would you like to be tested on?\n>> ")

df = pd.read_csv("elementlist.csv")
df = df.head(int(take))

df_copy = df.copy()
df_copy[["symbol", "name"]] = df[["name", "symbol"]]
shuffled = pd.concat([df, df_copy]).sample(frac=1);


def askQuestion(row):
    global correct, answered
    
    ans = input(f"\n{row['symbol']}\n>> ")
    if ans == row["name"]:
        print(f"{colors.GREEN}Correct! {row['symbol']} is {row['name']}.{colors.ENDC}")
        correct += 1
    else:
        print(f"{colors.FAIL}Sorry, {row['symbol']} is {row['name']}.{colors.ENDC}")
        wrong.append({"symbol": row["symbol"], "name": row["name"]})


for index, row in shuffled.iterrows():
    askQuestion(row)
    
print(f"\nScore: {correct}/{len(shuffled)}")


while(len(wrong) != 0):
    print("This is your review!\n")
    correct = 0
    
    wrong_questions = random.sample(wrong, len(wrong))
    wrong.clear()
    for question in wrong_questions:
        askQuestion(question);
    
    print(f"\nReview Score: {correct}/{len(wrong_questions)}")