# write your code here

class GameBoard:
    def __init__(self):
        state = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


    def get_state_from_user(self):
        # define board size
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

        if mode == "game_start":
            self.state = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def make_move(self, player):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        need_input = True

        while need_input:
            x, y = input("Enter the coordinates: ").split()
            need_input = False

            if x not in numbers or y not in numbers:
                print("You should enter numbers!")
                need_input = True
                continue
            else:
                x, y = int(x), int(y)
                if (x > len(self.state) or x < 1) or (y > len(self.state) or y < 1):
                    print("Coordinates should be from 1 to 3!")
                    need_input = True
                    continue
                elif self.state[x-1][y-1] != "_":
                    print("This cell is occupied! Choose another one!")
                    need_input = True
                    continue
                else:
                    self.state[x-1][y-1] = player
                    print(self)




    def valid_state(self):
        if self.game_won("X") and self.game_won("O"):
            # print("Double Win")
            return False

        num_of_X = sum([row.count("X") for row in self.state])
        num_of_O = sum([row.count("O") for row in self.state])

        if num_of_X - num_of_O > 1 or num_of_X - num_of_O < -1:
            # print(f"X count = {num_of_X}")
            # print(f"O count = {num_of_O}")
            # print(f"Difference = {num_of_X - num_of_O}")
            print("A player took too many moves")
            return False

        return True

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

board.set_state("game_start")
print(board)

p = "X"

while True:
    board.make_move(p)

    if board.valid_state():
        if board.game_won(p):
            print(f"{p} wins")
            break
        elif board.game_finished():
            print("Draw")
            break
    if p == "X":
        p = "O"
    else:
        p = "X"


