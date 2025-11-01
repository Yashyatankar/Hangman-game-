from words_list import words
import random


def display_hint(hint):

    print("  ".join(hint))
        
def display_answer(answer):
    print(" ".join(answer))


def main():

    lives = 7
    is_running = True
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    
    while is_running:

        display_hint(hint)

        guess = input('Enter your guess: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Invalid word')
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            print('wrong answr')
            wrong_guesses += 1
            if wrong_guesses == lives:
                print('u lose')
                break
        if "_" not in hint:
            print('U have guessed', wrong_guesses, 'this many wrong guesses ')
            print('u won') 
            is_running = False

if __name__ == '__main__':
    main()

