import random



def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey I said 1~10!')

answer = random.randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number 1~10:  '))
        run_guess(guess, answer)
    except ValueError:
        print('Please enter a number')
        continue