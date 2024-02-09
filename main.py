import random

class wordle:

    def __init__(self):
        # Counter for matches played.
        self.match_counter = 0
        # Player's current score. 
        self.player_score = 0
        # Attempts made in a round.
        self.attempts = 0
        # Max attempts in a round.
        self.max_attempts = 5
        # Count of guesses not in the word.
        self.totally_wrong_guesses = 0 
        # Count of guesses placed in wrong positions .
        self.incorrect_position_guesses = 0  
        # boolean that stores if the word is guessed correctly.
        self.correct_guess = False
        # Variable that stores the word length.
        self.word_length = None

    def logic(self):
        # Checks every inputted letter against the secret word's letter.
        feedback = []
        matched_letters = []

        for index in range(len(self.users_word)):
            if self.users_word[index] == self.secret[index]:
                feedback.append(self.users_word[index])
                # if the letter is not in another index of the secret, it will mark it correct, so next elif won't mistake it
                if self.users_word[index] not in self.secret[index + 1:]:
                    matched_letters.append(self.users_word[index])
            elif self.users_word[index] in self.secret and self.users_word[index] not in self.users_word[index + 1:] and self.users_word[index] not in matched_letters:
                self.incorrect_position_guesses += 1
                feedback.append(f"^")
            else:
                self.totally_wrong_guesses += 1
                feedback.append("-")
                # to-be-added remove the letter from the keyboard

        # Print the user's word and feedback
        print(self.users_word)
        print("".join(feedback))
        
        # if the game finished it will add the score in relation to the attempts remaining.
        if self.incorrect_position_guesses == 0 and self.totally_wrong_guesses == 0:
            self.correct_guess = True
            self.player_score += (5 - self.attempts) * ((self.word_length * 10) - 10)
            print(self.player_score)
        else:
            # adds player points and end game if out of attempts.
            print(self.points_logic())
            self.attempts += 1
            if self.attempts < 5:
                print(f"You have {5 - self.attempts} remaining.")
            else:
                print("You are out of moves")

    def points_logic(self):
        # Adds score in relation to incorrectly positioned guesses and resets not correct guesses variables.
        self.player_score += self.incorrect_position_guesses * self.word_length
        self.incorrect_position_guesses = 0
        self.totally_wrong_guesses = 0
        return self.player_score

    def play_again(self):
        # Asks user if they want to play again.
        # If yes, calles Play game funtion and resets necessary variables.
        print("I hope you enjoyed it!\nWould you like to play again? (\"Y\" to continue, press anything else to quit)")
        self.play_again_choice = input(">").lower()
        if self.play_again_choice == "y":
            self.attempts = 0
            self.correct_guess = False
            self.play_game()
        else:
            print(f"Your total score is {self.player_score}.\nHope to see you again!")

    def difficulty(self):
        # Asks user what difficulty they want.
        # Uses a try block to ensure correct intput.
        while True :
            print("Choose how long the secret word is.\nPress:\n1 for 3 letters\n2 for 4 letters\n3 for 5 letters")
            
            while True:
                try:
                    chosen_difficulty = input(">")
                    if not chosen_difficulty.isdigit() or int(chosen_difficulty) not in range(1,4):
                        raise ValueError("Input must contain only digits.")
                    chosen_difficulty = int(chosen_difficulty)
                    break
                except ValueError:
                    print("\nInvalid input. Please enter 1, 2 or 3 only.\n\nChose how long the secret word is.\nPress:\n1 for 3 letters\n2 for 4 letters\n3 for 5 letters")
            if chosen_difficulty == 1:
                self.word_length = 3
                self.secret_list = ["fly", "eat", "say", "run", "see", "hot", "dry", "new", "fat", "wet",
                "big", "fun", "sun", "god", "man", "art", "oil", "ice", "key", "log"]
                break
            elif chosen_difficulty == 2:
                self.word_length = 4
                self.secret_list = ["bath", "wish", "hope", "soft", "gift", "cake", "knee", "deaf", "time", "rain", "love", "work", "play", "talk", "walk", "blue", "cold", "good", "deep", "wide"]
                break
            elif chosen_difficulty == 3:
                self.word_length = 5
                self.secret_list = ['books', 'music', 'happy', 'dream', 'world', 'light', 'taste', 'clear', 'teach', 'plant',
                'laugh', 'speak', 'color', 'quiet', 'dance', 'fresh', 'brave', 'faith', 'clean', 'smile']
                break
            else:
                print("Plsease enter 1, 2 or 3.\n")
                
    def play_game(self):
        # Calls logic, difficulty, and play again functions and selects the secret word.
        self.difficulty()
        self.secret =  random.choice(self.secret_list)
        while self.attempts < self.max_attempts and not self.correct_guess:
            self.users_word = input("\nenter a word: ")
            while len(self.users_word) != len(self.secret):
                self.users_word = input(f"Please enter a word of {self.word_length} letters long: ")
            self.users_word = self.users_word.lower()
            print("\n'-' if the letter is not in the word\n'^' if it is wrongly placed\n")
            self.logic()
        self.play_again()

if __name__ == '__main__':
    play = wordle()
    play.play_game()

