
import random



def drawBoard(board):

      print('   |   |')

      print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

      print('   |   |')

      print('-----------')

      print('   |   |')

      print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

      print('   |   |')

      print('-----------')

      print('   |   |')

      print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

      print('   |   |')

def Letter():

      letter = ''

      while not (letter == 'X' or letter == 'O'):

          print('Do you want to be X or O?')

          letter = input().upper()

 

      if (letter == 'X'):

          return ['X', 'O']

      else:

          return ['O', 'X']

 
def First():

      if random.randint(0, 1) == 0:

          return 'player'

      else:

          return 'computer'

 
def repeat():

     print('Do you want to play again? (yes or no)')

     return input().lower().startswith('y')

 
def Move(board, letter, move):

      board[move] = letter

 

def Winner(bo, le):

      return ((bo[7] == le and bo[8] == le and bo[9] == le) or 

      (bo[4] == le and bo[5] == le and bo[6] == le) or 

      (bo[1] == le and bo[2] == le and bo[3] == le) or 

      (bo[7] == le and bo[4] == le and bo[1] == le) or 

      (bo[8] == le and bo[5] == le and bo[2] == le) or 

      (bo[9] == le and bo[6] == le and bo[3] == le) or
              
      (bo[7] == le and bo[5] == le and bo[3] == le) or 

      (bo[9] == le and bo[5] == le and bo[1] == le)) 



def Copy(board):

      dupeBoard = []



      for i in board:

         dupeBoard.append(i)

 

      return dupeBoard


def Space(board, move):

      return board[move] == ' '

 
def Player(board):

     move = ' '

     while move not in '1 2 3 4 5 6 7 8 9'.split() or not Space(board, int(move)):

         print('What is your next move? (1-9)')

         move = input()

     return int(move)

 

def choose(board, movesList):

     possibleMoves = []

     for i in movesList:

          if Space(board, i):

              possibleMoves.append(i)

 

     if len(possibleMoves) != 0:

          return random.choice(possibleMoves)

     else:

          return None

 

def ComputerMove(board, playerLetter):

      if playerLetter == 'X':

          computerLetter = 'O'

      else:

         computerLetter = 'X'

      for i in range(1, 10):

         copy = Copy(board)

         if Space(copy, i):

             Move(copy, playerLetter, i)

             if Winner(copy, playerLetter):

                 return i

      for i in range(1, 10):

         copy = Copy(board)

         if Space(copy, i):

             Move(copy, computerLetter, i)

             if Winner(copy, computerLetter):

                 return i

      move = choose(board, [1, 3, 7, 9])

      if move != None:

         return move

      if Space(board, 5):

         return 5


      return choose(board, [2, 4, 6, 8])



def Full(board):

     for i in range(1, 10):

         if Space(board, i):

             return False

     return True





print('Welcome to Tic Tac Toe!')



while True:

     theBoard = [' '] * 10

     computerLetter, playerLetter = Letter()

     turn = First()

     print('The ' + turn + ' will go first.')

     Playing = True



     while Playing:

         if turn == 'player':

             drawBoard(theBoard)

             move = Player(theBoard)

             Move(theBoard, playerLetter, move)


             if Winner(theBoard, playerLetter):

                 drawBoard(theBoard)

                 print('You have won the game!')

                 Playing = False

             else:

                 if Full(theBoard):

                     drawBoard(theBoard)

                     print('The game is a tie!')

                     break

                 else:

                     turn = 'computer'


         else:

             move = ComputerMove(theBoard, computerLetter)

             Move(theBoard, computerLetter, move)



             if Winner(theBoard, computerLetter):

                 drawBoard(theBoard)

                 print('The computer has beaten you! You lose.')

                 Playing = False

             else:

                 if Full(theBoard):

                     drawBoard(theBoard)

                     print('The game is a tie!')

                     break

                 else:

                     turn = 'player'



     if not repeat():

         break

