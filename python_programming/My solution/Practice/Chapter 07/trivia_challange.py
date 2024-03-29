# Trivia Challange
# Trivia game that raeads a plain text file

import sys

def open_file(file_name, mode):
    """open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file",file_name, "Ending Programme.\n",e)
        input("\n\Press the enter key to exit.")
        sys.exit()
    else:
        return the_file
    
def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challange!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # Get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
          # ask question
          print(category)
          print(question)
          for i in range(4):
              print("\t", i+1, "-", answers[i])

          # get answer
          answer = input("What's your answer?: ")

          # Check answer
          if answer == correct:
              print("\nRight!", end="")
              score += 1
          else:
              print("\nWrong.", end="")
          print(explanation)
          print("Score:", score, "\n\n")

          # get next block
          category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("Your final score is", score)

main()

input("\n\nPress the enter key to exit.")

            
        
