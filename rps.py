import random
import time

moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(.5)


print_pause("Welcome to Rock, Paper, Scissors!")
print_pause("You will be playing 5 rounds with a Computer.")


class Player:  # player that plays rock
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Player1(Player):  # player with random moves
    def move(self):
        return random.choice(moves)


class Player2(Player):  # human player
    def move(self):
        result = None
        while result not in moves:
            result = str.lower(input(f"Please pick ({moves}):\n"))
            result = str.strip(result)

        return result


class Player3(Player):  # player that cycles moves
    def __init__(self):
        self.player3 = None

    def move(self):
        if self.player3 is None:
            index = 0
        else:
            index = moves.index(self.player3)
            index = (index + 1) % len(moves)

        self.player3 = moves[index]

        return self.player3


class Player4(Player):   # player with refelctive moves
    def __init__(self):
        self.player4 = None

    def move(self):
        if self.player4 is None:
            return moves[0]
        else:
            return self.player4

    def learn(self, my_move, their_move):
        self.player4 = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_computer = 0
        self.p2_player = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Computer played {move1}.\nYou played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.Show_Winner(move1, move2)

    def Show_Winner(self, move1, move2):
        p1_won_round = beats(move1, move2)
        winner = ""
        if p1_won_round:
            winner = "Computer won"
            self.p1_computer += 1
        elif move1 != move2:
            winner = "You won"
            self.p2_player += 1
        else:
            winner = "It was a tie"
        print(f"{winner} this round!")
        print(f"Current Score: Computer: {self.p1_computer} " +
              f"You: {self.p2_player}")

    def Show_Scores(self):
        print(f"\nFinal Score: Computer: {self.p1_computer} " +
              f"You: {self.p2_player}")
        winner = ""
        if self.p1_computer > self.p2_player:
            winner = "Computer won"
        elif self.p2_player > self.p1_computer:
            winner = "You won"
        else:
            winner = "It was a tie"
        print(f"{winner} this game!")

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        self.Show_Scores()


def choose_computer():
    computer_types = [Player, Player1, Player3, Player4]
    computer_players = random.choice(computer_types)
    return computer_players


if __name__ == '__main__':
    computer_players = choose_computer()
    game = Game(computer_players(), Player2())
    game.play_game()
