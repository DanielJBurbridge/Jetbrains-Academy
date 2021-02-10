# write your code here

class GameBoard:
    def __init__(self):
        state = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


    def get_state_from_user(self):
        #define board size
        size = 3

        usr_input = input("Enter cells:")

        state = []
        for i in range(size):
            row = []
            for k in range(size):
                row.append(usr_input[(i*3 + k)])
            state.append(row)

        return state


    def set_state(self, mode):
        if mode == "from_user":
            self.state = self.get_state_from_user()

    # TODO CHECK IF STATE IS VALID
    def valid_state(self):
        if self.game_won("X") and self.game_won("O"):
            # print("Double Win")
            return False

        num_of_X = sum([row.count("X") for row in self.state])
        num_of_O = sum([row.count("O") for row in self.state])

        if num_of_X - num_of_O > 1 or num_of_X - num_of_O < -1:
            print(f"X count = {num_of_X}")
            print(f"O count = {num_of_O}")
            print(f"Difference = {num_of_X - num_of_O}")
            print("A player took too many moves")
            return False

        return True

    # TODO CHECK IF GAME IS FINISHED
    def game_finished(self):
        return sum([row.count("_") for row in self.state]) == 0

    def game_won(self, player):
        return self.game_won_on_row(player) or self.game_won_on_col(player) or self.game_won_on_diag(player)

    def game_won_on_row(self, player):
        for row in self.state:
            if row.count(player) == len(row):
                # print("Game won on row")
                return True

        return False

    def game_won_on_col(self, player):
        # TODO figure out how this line works -- found on Stackoverflow.
        rotated_state = [[self.state[j][i] for j in range(len(self.state))] for i in range(len(self.state[0])-1, -1, -1)]

        for row in rotated_state:
            if row.count(player) == len(row):
                # print("Game won on col")
                return True
        return False

    def game_won_on_diag(self, player):
        count = 0

        while count < len(self.state):
            if self.state[count][count] != player:
                break
            else:
                count += 1

        if count == len(self.state):
            # print("Won on forwards Diag")
            return True

        count = 0

        while count < len(self.state):
            if self.state[count][len(self.state) - (count + 1)] != player:
                break
            else:
                count += 1

        if count == len(self.state):
            # print("Won on backwards Diag")
            return True

        return False

    def __repr__(self):
        return f'State={self.state}'

    def __str__(self):
        string = ""
        string += "-" * len(self.state) * 3
        for row in self.state:
            string += "\n|"
            for cell in row:
                string += f" {cell}"
            string += " |"
        string += "\n"
        string += "-" * len(self.state) * 3

        return string


board = GameBoard()

board.set_state("from_user")
print(board)


# TODO COMPLETE VALID STATE & GAME FINISHED METHODS
if board.valid_state():
    if board.game_won("X"):
        print("X wins")
    elif board.game_won("O"):
        print("O wins")
    else:
        if board.game_finished():
            print("Draw")
        else:
            print("Game not finished")
else:
    print("Impossible")



