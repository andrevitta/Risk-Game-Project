# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:15:54 2020
Run Risk Game

 Strategy Game for 2 - 6 players
  Version has 13 countries and Attack mode only , not alowed to move trops, only when victory

 
@author: Andre Vitta
"""
###############################################################################
### importing libraries

import random
#import numpy as np
import class_country as ct
import class_player as pl
from termcolor import colored
###############################################################################
#################### defining some functions###################################
###############################################################################
#Defining the class_country
class country:
    
    # global variables 
    Noa = 0
    
    # atributes
    def __init__(self,name,Noa=Noa, bor=None,cont=None,ruler=None):
        self.name = name
        self.number_armies=Noa
        self.borders=bor # list
        self.continent=cont
        self.ruler=ruler
        
    # methods
    def addArmies(self,Narmies):
          self.number_armies+=Narmies
          
    def iswiped(self):
        if self.number_armies==0:
            return True
        else:
            return False
      
    def dice(self):
          
          return random.choice(range(1,7))

      
    def display_borders(self):

            for i in range ( len(self.borders) ):
                                 
                  print ('Index -',i,':',self.borders[i].name)

   
    def attack_country(self,opponent) :
          
       if self.number_armies == 1 : 
           
             return f'Sorry, {self.name} you need more then 1 army to attack.'
       
       elif opponent in [i for i in self.borders] :
        
             while self.number_armies > 1 :
                   
                   print ( ' ' )
                   print ( ' #######   ATTACK HAS BEGUN ! ########')
                   print ( ' ' )
                   
                   
                   attack = self.dice()

                   defence = opponent.dice()
                   
                   print('         Dices \n','Attack: ', attack, 'Defence: ', defence)
                   print ( ' ' )
                   
                   if attack > defence :
                         
                     print(f"{opponent.name} loses one army while defending against {self.name}.")
                     print ( ' ' )
                     opponent.addArmies(-1)
                     
                     #print (self.ruler,opponent.ruler)
                     print (f'{self.name} has {self.number_armies} Armies,{opponent.name} has {opponent.number_armies} Armies')
                     
                     
                     if opponent.iswiped() :
                           
                           print (f'{self.name} has invaded {opponent.name}')
                           print ( ' ' )
                           
                           # change country ruler
                           
                           opponent.ruler.countries.remove(opponent)
                           self.ruler.countries.append(opponent)
                          
                           opponent.ruler = self.ruler
                           
                           
                           
                           while True :
                                 try : 
                                    n = int( input ( 'Enter No of Armies to move: ') )
                                    
                                    if n not in range(int(self.number_armies)):
                                          
                                          print(f"You can move that many armies .You can only place {self.number_armies-1}" )
                                          raise ValueError
                                 except ValueError :
                                       print ("Please enter a valid number")
                                       continue
                                 else :
                                       break
                           
                           opponent.addArmies(n)
                           self.addArmies(-n)
                           
                           
                           
                           #print (self.ruler,opponent.ruler)
                           print (self.number_armies,opponent.number_armies)
                           break
                   
                   else : 
                     
                     print(f"{self.name} loses one army while attacking {opponent.name}")
                     self.addArmies(-1)
                     
                     #print (self.ruler,opponent.ruler)
                     print (f'{self.name} has {self.number_armies} Armies,{opponent.name} has {opponent.number_armies} Armies')
               

       else : 
           print(f"Sorry {self.name}, you don't have any common borders with {opponent.name}. Please choose another country to  attack.")
###############################################################################
class Player :   
   
      number_of_armies=0
      number_of_cards =0
      color='red'
      
      def __init__(self,name, ctr = None , na = number_of_armies , nc = number_of_cards,color=color):
        
        self.name= name
        self.countries = list()
        self.number_of_armies = na
        self.number_of_cards = nc
        self.color = color
     
      # methods
      def addArmies(self,Narmies):
          self.number_of_armies+=Narmies

      
      def addCountry(self,country):
            
          self.countries.append(country)
          country.ruler = self
         
      def display_countries(self):
            for i in range ( len( self.countries)):
 
                  print ('Index -',i,':',self.countries[i].name ,'No Armies:', self.countries[i].number_armies)

      def countries_check(self,opponent):
            
            for i in range ( len( self.countries)):
                  
                  if self.countries[i].ruler != self:
                        
                        self.countries.remove(self.countries[i])          
##############################################################################
                        
## Diplays the board and the current player countries and armies
def display_board():
      

      water = '  Water '
      cwater ='blue'
      color1 = LoC[0].ruler.color
      color2 = LoC[1].ruler.color
      color3 = LoC[2].ruler.color
      color4 = LoC[3].ruler.color
      color5 = LoC[4].ruler.color
      color6 = LoC[5].ruler.color
      color7 = LoC[6].ruler.color
      color8 = LoC[7].ruler.color
      color9 = LoC[8].ruler.color
      color10 = LoC[9].ruler.color
      color11 = LoC[10].ruler.color
      color12 = LoC[11].ruler.color
      color13 = LoC[12].ruler.color
      
      print ('          ___________________________________')
      print (' ')
      print ('                 RISK SPECIAL EDITION       ')
      print ('          **** Battle for Middle Earth  ****')
      print ('          ___________________________________')
      print (' ')
    
      
      print (' __________________________________________')
      print (f'|{colored(LoC[0].name,color1)} | {colored(LoC[1].name,color2)} | {colored(LoC[2].name,color3)} | {colored(LoC[3].name,color4)} |')
      print (f'|    {colored(LoC[0].number_armies,color1)}    |     {colored(LoC[1].number_armies,color2)}    |     {colored(LoC[2].number_armies,color3)}    |     {colored(LoC[3].number_armies,color4)}    |    ')
      print ( '|_________|__________|__________|__________|')
      print (f'|         | {colored(LoC[4].name,color5)} |          | {colored(LoC[5].name,color6)} |')
      print (f'|{colored(water,cwater)} |     {colored(LoC[4].number_armies,color5)}    |{colored(water,cwater)}  |     {colored(LoC[5].number_armies,color6)}    |    ')
      print ( '|_________|__________|__________|__________|')
      print (f'|{colored(LoC[6].name,color7)} | {colored(LoC[7].name,color8)} | {colored(LoC[8].name,color9)} | {colored(LoC[9].name,color10)}|')
      print (f'|    {colored(LoC[6].number_armies,color7)}    |     {colored(LoC[7].number_armies,color8)}    |     {colored(LoC[8].number_armies,color9)}    |     {colored(LoC[9].number_armies,color10)}    |    ')
      print ( '|_________|__________|__________|__________|')
      print (f'|{colored(LoC[10].name,color11)}| {colored(LoC[11].name,color12)}| {colored(LoC[12].name,color13)}|          |')
      print (f'|    {colored(LoC[10].number_armies,color11)}    |     {colored(LoC[11].number_armies,color12)}    |     {colored(LoC[12].number_armies,color13)}    | {colored(water,cwater)} |')
      print ( '|_________|__________|__________|__________|')
      
      print(' ')
      
 
###############################################################################

## Distribute Armies

#
# We must include a input control to prevent crashes and error handeling
#
       
def dist_armies (players):
      
      global Nplayers
      
      for i in range (Nplayers):
            while players[i].number_of_armies!=0:
                  
                  # Display Board and Countries  ruled by player
                  
                  display_board()
                  
                  print (f'{colored(players[i].name.upper(),players[i].color)} IS PLAYING NOW' )
                  print (' ')
                  
                  players[i].display_countries()
                  
                  
                  
                  # Adds the selected anumber of armies to country
                  print(' ')
                  print (f' Your have {players[i].number_of_armies} Armies to be placed')
                  print(' ')
                  print ( 'Please enter  Where you want to place your armies' )
                  
                  # Menu for choosing Country and amount of armies to place
                  while True : 
                      try : 
                          x = int( input ( 'Enter Country index: ') )
                          
                          if players[i].countries[x] not in players[i].countries : 
                              print("Please enter a valid index")
                              
                      except ValueError :
                          print ("Please enter a valid number")
                          continue
                      else :
                          break
                          
                      print ( f'Please enter How many armies you whish to place in {players[i].countries[x].name}' )
                      
                  while True :
                          try : 
                              y = int( input ( 'Enter No of Armies: ') )
                              
                              if y not in range(int(players[i].number_of_armies)+1):
                                    print(f"You don't have that many armie to deploy.You can only place {players[i].number_of_armies}" )
                                    raise ValueError
                          except ValueError :
                              print ("Please enter a valid number")
                              continue
                          else :
                              break 
                  
                  # Adds the selected anumber of armies to country
                  
                  players[i].countries[x].addArmies(y)
                  players[i].addArmies(-y)


###############################################################################
###############################################################################
            ### Creating The Board ###

cnames = [' Shire  ','  Moria ',' Lindon ','Gundabad', ' Rohan  ',' Agnamar','Rivendel', ' Gondor ', ' Mordor ','Isengard ', '   Rhun  ', '  Arnor  ','  Dale   ']
# create all countries
Ncountries = 13
LoC =[ country(cnames[i]) for i in range(Ncountries)]

# define all borders

LoC[0].borders = [LoC[1]]
LoC[1].borders = [LoC[0],LoC[2],LoC[4]]
LoC[2].borders = [LoC[1],LoC[3]]
LoC[3].borders = [LoC[2],LoC[5]]
LoC[4].borders = [LoC[1],LoC[7]]
LoC[5].borders = [LoC[3],LoC[9]]
LoC[6].borders = [LoC[7],LoC[10]]
LoC[7].borders = [LoC[4],LoC[6],LoC[8],LoC[11]]
LoC[8].borders = [LoC[7],LoC[9],LoC[12]]
LoC[9].borders=[LoC[5],LoC[8]]
LoC[10].borders=[LoC[6],LoC[11]]
LoC[11].borders=[LoC[10],LoC[7],LoC[12]]
LoC[12].borders=[LoC[8],LoC[11]]


###############################################################################

      ############### Setting Game ################
 
### Creating the players ###

# get number of players

while True :
    
    try : 
        Nplayers = int( input ( ' Enter the number of players  (2 - 6) : '))
   
        if type(Nplayers)!=int or ( Nplayers not in [i for i in range(2,7)] ):
              raise ValueError
              
    except ValueError :
        print("Please, enter a valid number of players")
        continue
    else :
        break

  

# getting names
names = [ input(f'Enter name of Player {i+1}: ') for i in range(Nplayers)]

# creating players objects
players = [ Player(name) for name in names ]

# color list
colors = ['red','green','yellow','grey','magenta','cyan']  

for i in range (Nplayers):
      players[i].color = colors[i]

       ##### Distribute the countries for the players ###

### Inputs: List of countries, players
### Output: players

# Shuffling the countries

### teste 
cards_countries = [i for i in range(len(LoC))]
random.shuffle(cards_countries)

# drawing cards of countries for each player
while len(cards_countries)!=0:
      
      # round draw
      for i in range( len(players) ):
            
            if len(cards_countries)!=0 :
                  players[i].addCountry (LoC[cards_countries.pop()])


              
###############################################################################

                  ###### START GAME ########

###############################################################################

                     #### ROUND 1 ####

######## Laying out for 1st round ###################################      
### distributing initial armies
   
for i in range (Nplayers):
      players[i].number_of_armies = 2* round( Ncountries/Nplayers)

### deciding who start

# create list of players order to play
random.shuffle(players)

# Prints the 1st Player

print (f'{players[0].name} Starts to play !!!' )

### Placing one army in each starting country ###

for i in range (Nplayers):
     
      for j in range ( len( players[i].countries)):
            players[i].countries[j].addArmies(1)
            players[i].addArmies(-1)            

######################################################################
### distributing remaining armies
            
dist_armies(players)

print (' #### ROUND 1 HAS TERMINATED ####')

###############################################################################


                   ### Round 2 and on ###

### Check whos is playing
while len(players)!=1:
      
      # start runing the round #
      
      for i in range(Nplayers):
            
            # To make easier to write just assing current turn player
            player = players[i]
            
            # calculate armies
            player.number_of_armies = len(player.countries)
            if player.number_of_cards == 3:
                  player.number_of_armies +=2 
                  player.number_of_cards=0
           
            ### distributing armies
            dist_armies(players)
      
            ## Decide what to do
      
            print (' What Do You want to do?\n \
                     1 - To Attack until dead\n \
                     2 - Pass Turn to next player\n \
                     3 - Save and Quit')
            
            while True :
                try : 
                    choice = int( input('Enter Choice: ') )
                except ValueError :
                    print("Enter a choice in the following list :\n \
                     1 - To Attack until dead\n \
                     2 - Pass Turn to next player\n \
                     3 - Save and Quit")
                    continue
                if choice not in [1,2,3]:
                    continue
                else :
                    break

      ### ATTACK ###
            if choice == 1: 
                  
                  display_board()
                  players[i].display_countries()
                  
                  print ( 'Please enter  WHERE  you want to attack FROM: \n' )
                  
                  while True :
                      try :
                          x = int( input ( 'Enter Country index: ') )
                          if players[i].countries[x] not in players[i].countries : 
                              print("Please enter a valid index")
                              continue
                      except ValueError : 
                          print("Please enter the correct index")
                          continue
                      else : 
                          break 
      
                  players[i].countries[x].display_borders()
      
                  print ( f'Please enter WHERE you want to attack from : {players[i].countries[x].name}' )
             
                  while True : 
                      try : 
                          z = int( input ( 'Enter Country index: ') )
                          
                          if players[i].countries[x].borders[z] not in players[i].countries[x].borders:
                              print("Enter a valid index")
                              continue
                      except ValueError:
                          print("Please enter a valid index")
                          continue
                      else : 
                          break
      
                  print ( f' So the Figth Begins !!!!!\n \n {players[i].countries[x].name} ATTACKS {players[i].countries[x].borders[z].name}' )
                  
                  players[i].countries[x].attack_country(players[i].countries[x].borders[z])
                  
                  
            elif choice == 2:
                  ## move armies
                  continue # continue for loop              
            elif choice == 3:
                  # save variables to continue game
                  # stop while
                  break
            # move armies   


print ( 'GAME OVER' )




