'''
Implement a class called player that represents a cricket player.   The  player class should have a
method called play() which prints "The player is playing cricket.derive two classes, Batsman and
Bowler,from the player class.   Override the play() "The batsman 
is batting" and "The bowler is bowling",respectivwly. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.'''

class player:
   def play(self):
     print("The player is playing cricket.")

class Batsman(player):
   def play(self):
     print("The batsman is batting.")

class Bowler(player):
  def play(self):
    print("The bowler is bowling .")

batsman = Batsman()     
bowler = Bowler()

batsman.play()
bowler.play()

   
   




