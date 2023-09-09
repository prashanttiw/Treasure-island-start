print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
way=input("<--U have two ways to go which one u choice Right or left??-->\n").lower()
if way=="left":
  print("<--Wunder full u cross the road.-->")
  water=input("<--Now u came accros river.-->\n<--So you want to swim or wait??-->\n").lower()
  if (water=="wait"):
    print("<--Awesome u cross the river.-->")
    door=input("<--Now you are in front of a house which has three doors.-->\n<--So which one u choose Red,Blue or Yellow??-->\n").lower()
    if door=="blue":
      print("<--OOPS you eaten by lion.-->\n#_#_GAME OVER_#_#")
    elif door=="red":
       print("<--OMG you burned by fire.-->\n#_#_GAMAE OVER_#_#")
    elif door=="yellow":
      print("YES!!\nYOU GOT THE TREASURE!!\n     *     \n    ***    \n   *****   \n  *******  \n ********* \n***********\n!!YOU WIN!!")
    else:
      print("#_#_GAME OVER_#_#")
  else:
    print("<--During swimming in river u attacked by trout.--\n#_#_GAME OVER_#_# ")
else:
  print("<--By moving in that road You fall in the hole.-->\n#_#_GAME OVER_#_#")