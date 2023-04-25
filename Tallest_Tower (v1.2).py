# Import needed modules
import time as t
import random as ran
import sys

def startUp(): # Cool Text Art
      
  print("""
 ,--.--------.     ,---.                                    ,----.     ,-,--.   ,--.--------.          ,--.--------.      _,.---._              ,-.-.        ,----.                
/==/,  -   , -\  .--.'  \        _.-.        _.-.        ,-.--` , \  ,-.'-  _\ /==/,  -   , -\        /==/,  -   , -\   ,-.' , -  `.   ,-..-.-./  \==\    ,-.--` , \   .-.,.---.   
\==\.-.  - ,-./  \==\-/\ \     .-,.'|      .-,.'|       |==|-  _.-` /==/_ ,_.' \==\.-.  - ,-./        \==\.-.  - ,-./  /==/_,  ,  - \  |, \=/\=|- |==|   |==|-  _.-`  /==/  `   \  
 `--`\==\- \     /==/-|_\ |   |==|, |     |==|, |       |==|   `.-. \==\  \     `--`\==\- \            `--`\==\- \    |==|   .=.     | |- |/ |/ , /==/   |==|   `.-. |==|-, .=., | 
      \==\_ \    \==\,   - \  |==|- |     |==|- |      /==/_ ,    /  \==\ -\         \==\_ \                \==\_ \   |==|_ : ;=:  - |  \, ,     _|==|  /==/_ ,    / |==|   '='  / 
      |==|- |    /==/ -   ,|  |==|, |     |==|, |      |==|    .-'   _\==\ ,\        |==|- |                |==|- |   |==| , '='     |  | -  -  , |==|  |==|    .-'  |==|- ,   .'  
      |==|, |   /==/-  /\ - \ |==|- `-._  |==|- `-._   |==|_  ,`-._ /==/\/ _ |       |==|, |                |==|, |    \==\ -    ,_ /    \  ,  - /==/   |==|_  ,`-._ |==|_  . ,'.  
      /==/ -/   \==\ _.\=\.-' /==/ - , ,/ /==/ - , ,/  /==/ ,     / \==\ - , /       /==/ -/                /==/ -/     '.='. -   .'     |-  /\ /==/    /==/ ,     / /==/  /\ ,  ) 
      `--`--`    `--`         `--`-----'  `--`-----'   `--`-----``   `--`---'        `--`--`                `--`--`       `--`--''       `--`  `--`     `--`-----``  `--`-`--`--'  
        (Tallest Tower, Text-Based Adventure Game, v1.2)

        """)

name = ""

def waitfunc(time): # Function to wait time, as not to print large bodies of text
      t.sleep(time)

def ranch(num1, num2): # Ran(dom)ch(ance), Random Number Generation Handeler
      dip = ran.randint(num1, num2)
      return dip

def playagain(): # Ask to play again
      uinv.clear()
      ans = input("Do you want to play again?: ")
      if "y" in ans.lower():
            game()
            
      else:
            print("Exiting!")
            sys.exit()
      
def play(): # Ask to play game
     global name
     uinv.clear()
     startUp()
     waitfunc(2)
     ans = input("Would you like to play the game?: ")
     if "y" in ans.lower():
          name = input("What is your name?: ")
          game()

     else:
          print("Exiting!")
          sys.exit()

def cellchoice(): # Choices in the Cell
     dialogue = input("What will you do? (type a letter) \nA. Talk to the guard \nB. Examine the hay pile\nC. Something... bad?\nD. Pick Lock\n")
     if dialogue.lower() == "a":
          talkguard()
          dialogue = input("What will you say/do? (type a letter)\nA. Bribe Guard\nB. Claim innocence\nC. Offer Orb\n")
          if dialogue.lower() == "a":
                bribeguard()

          elif dialogue.lower() == "b":
                claiminnocence()

          elif dialogue.lower() == "c":
                offerorb()
          
          elif dialogue.lower() == "d":
               pick_lock()

          elif "die" in dialogue.lower():
                combust()

          elif "4th Wall" in dialogue.lower():
              wallbreak()
          
          elif "jump" and "window" in dialogue.lower():
               window()

          elif "Convince" and "not real" in dialogue.lower():
               wallbreak()
          
          else:
               print("I don't understand that.")

     elif dialogue.lower() == "b":
          haypile()

          dialogue = input("What will you say/do? (type a letter)\nA. Talk to the guard\nB. Something... bad?\nC. Pick the lock\nD. Use cell key\n")
          if dialogue.lower() == "a":
               bribeguard()

          elif dialogue.lower() == "b":
               attackguard2()
          
          elif dialogue.lower() == "c":
               pick_lock()
          
          elif dialogue.lower() == "d":
               escape_jailcell()
          
          elif "jump" and "window" in dialogue.lower():
               window()
      
          elif "die" in dialogue.lower():
               combust()
     
          elif "4th Wall" in dialogue.lower():
              wallbreak()

          elif "Convince" and "not real" in dialogue.lower():
               wallbreak()
     
          else:
               print("I don't understand that.")

     elif dialogue.lower() == "c":
          attackguard2()
     
     elif dialogue.lower() == "d":
          pick_lock()

     elif "jump" and "window" in dialogue.lower():
           window()
      
     elif "die" in dialogue.lower():
          combust()

     elif "4th Wall" in dialogue.lower():
          wallbreak()

     elif "Convince" and "not real" in dialogue.lower():
          wallbreak()
     
     else:
          print("I don't understand that.")

def cellchoice2(): # Cell Choices after failing to pick lock
     dialogue = input("What will you do? (type a letter) \nA. Talk to the guard \nB. Examine the hay pile\nC. Something... bad?\n")
     if dialogue.lower() == "a":
          talkguard()
          dialogue = input("What will you say/do? (type a letter)\nA. Bribe Guard\nB. Claim innocence\nC. Offer Orb\n")
          if dialogue.lower() == "a":
                bribeguard()

          elif dialogue.lower() == "b":
                claiminnocence()

          elif dialogue.lower() == "c":
                offerorb()

          elif "die" in dialogue.lower():
                combust()

          elif "4th Wall" in dialogue.lower():
              wallbreak()

          elif "Convince" and "not real" in dialogue.lower():
               wallbreak()
          
          elif "jump" and "window" in dialogue.lower():
               window()
          
          else:
               print("I don't understand that.")

     elif dialogue.lower() == "b":
          haypile()

          dialogue = input("What will you say/do? (type a letter)\nA. Talk to the guard\nB. Something... bad?\nC. Use cell key\n")
          if dialogue.lower() == "a":
               bribeguard()

          elif dialogue.lower() == "b":
               attackguard2()
          
          elif dialogue.lower() == "c":
               escape_jailcell()
          
          elif "jump" and "window" in dialogue.lower():
               window()
      
          elif "die" in dialogue.lower():
               combust()
     
          elif "4th Wall" in dialogue.lower():
              wallbreak()

          elif "Convince" and "not real" in dialogue.lower():
               wallbreak()
     
          else:
               print("I don't understand that.")

     elif dialogue.lower() == "c":
          attackguard2()

     elif "jump" and "window" in dialogue.lower():
           window()
      
     elif "die" in dialogue.lower():
          combust()

     elif "4th Wall" in dialogue.lower():
          wallbreak()

     elif "Convince" and "not real" in dialogue.lower():
          wallbreak()
          
     else:
          print("I don't understand that.")

def pick_lock(): # Pick lock function
    print("There are 10 angles that can possibly be used to pick the lock. \nAngle 0, 20, 40, 60, 80, 100, 120, 140, 160, 180.")
    print("Work quickly. The guard will return soon.")
    ch = ran.randint(1, 10)
    turn = 0
    while turn < 9:
        if ch == 1:
            angle = 0
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 2:
            angle = 20
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 3:
            angle = 40
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 4:
            angle = 60
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 5:
            angle = 80
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 6:
            angle = 100
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 7:
            angle = 120
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 8:
            angle = 140
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
        elif ch == 9:
            angle = 160
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1    
        elif ch == 10:
            angle = 180
            anglepick = input("Pick the angle to try: ")
            if int(anglepick) == angle:
                print("You pick the lock and escape.")
                escape_jailcell()
                break
            elif int(anglepick) + 20 == angle or int(anglepick) - 20 == angle:
                print("You are close. Try again.")
                turn = turn + 1
            elif int(anglepick) != angle:
                print("That did not work. Try again.")
                turn = turn + 1
    print("The guard has returned. You have failed to pick the lock")
    waitfunc(2)
    cellchoice2()
   
    
guarddeaths = 0

# Define Wins

def windowwin(): # Jump from window win
      print("You feel a weird tingling.")
      print("You grab ahold of the outer window, and then make a leap for it.")
      print('There is only one thing you find appropriate to yell as you fall from the window: "YEET!"')
      waitfunc(2)
      print("Somehow, and by some miracle, you survive (your legs don't).")
      print("With your legs out of service, you crawl forward foot by foot until the tower comes out of view.")
      waitfunc(2)
      print("You managed to escape! Congrats on the Window Win (1/4).")
      playagain()

def impersonation(): # Impersonate guard win
     waitfunc(2)
     print("You somehow manage to blend in with the guards. \nYou are never given the chance to escape. You work alongside the other guards in the prison until your fateful death.")
     waitfunc(2)
     print("You Won? At least it's considered a win. Congrats on the Impersonation Win (2/4).")
     playagain()

def genocide(): # Kill all guards win
     waitfunc(2)
     print("After somehow managing to kill every guard in the Tower the gate remains unguarded and unlocked.")
     waitfunc(2)
     print("You waltz through the gate, and into the outside.\n Only for the many dead to haunt you for the remainder of your life.")
     waitfunc(2)
     print("You managed to escape, you monster. This was the Genocide Win (3/4).")
     playagain()

def escape(): # Normal (and boring) escape win
     waitfunc(2)
     print("You unlock the gate, revealing the outside, which for whatever reason remains unguarded.")
     print("You managed to escape! Congrats on the Escape Win (4/4). ")
     playagain()



# User inventory
uinv = []

# Define Events
def intro():
       print("You wake up in a cube-shaped prison cell.\n")
       print("You are facing south. There is a wall of iron bars with extremely narrow spaces between them.\n")
       print("There is a guard standing at the door, which is also made of iron bars.\n")
       print("To the north (behind you), there is an open window. It is large enough to sit in and still have wiggle room. There is no barrier on this window.\n")
       print("To the east (on your left), there is a pile of hay, a couple pieces of paper, and something else.\n")
       print("To the west (on your right), there is a skeleton and nothing else. It has a blue gem in its left eye socket. \nYou'd best not disturb it, unless you wanna have a bad time.\n")

def castle_door(): # Get to castle door/escape
     if "door_key" in uinv:
          waitfunc(3)
          print("You pull out the key you found, it fits the gate to the outside.")
          escape()
          

     elif "unlock_spell" in uinv:
          waitfunc(3)
          print("You chant the unlocking spell you found earlier.")
          waitfunc(2)
          print("The gate shakes, before the lock opens.")
          escape()

     elif guarddeaths == 3:
          genocide()



def attackguard2(): # Attack Guard, when unarmed
     global guarddeaths
     print("You decide you are somehow fit enough to take down a fully armed guard, can't tell if you're just brave or stupid. Maybe both.")
     ch = ranch(1, 3)
     if ch == 3:
          print("By some miracle (because it definitely wasn't skill) you manage to take down the guard. \nYou grab them through the bars of your cell, strangling them and obtaining their keys.\n Allowing you to unlock the gate.")
          waitfunc(1)
          guarddeaths += 1
          takesword = input("Do you want to take the guard's sword?: (y/n)\n")

          if "y" in takesword.lower():
               uinv.append("sword")
               print("You take the sword.")
               waitfunc(1)
               pass_guard()
                    

          elif "n" in takesword.lower():
               print("You leave the sword behind.")
               waitfunc(1)
               pass_guard()

     else:
          print("Almost effortlessly the guard strikes you down.")
          print("You died.")
          waitfunc(1)
          playagain()

def attackguard(): # Attack guard, when armed
     global guarddeaths
     if "sword" in uinv:
          print("You run at the guard, sword in hand.")
          ch = ranch(1, 4)
          if ch == 3:
               print("Almost effortlessly the guard strikes you down.")
               print("You died.")
               waitfunc(1)
               playagain()

          else:
               print("You easily strike down the guard")
               guarddeaths += 1
               waitfunc(1)
                    

               


     else:

          print("You decide you are somehow fit enough to take down a fully armed guard, can't tell if you're just brave or stupid. Maybe both.")
          ch = ranch(1, 3)
          if ch == 3:
               guarddeaths += 1
               print("By some miracle (because it definitely wasn't skill) you manage to take down the guard. \nYou grab their sword from them and cut them down.\n Leaving the doorway wide open.")
               waitfunc(1)

          else:
               print("Almost effortlessly the guard strikes you down.")
               print("You died.")
               waitfunc(1)
               playagain()


def stunguard(): # Stunguard Dialogue
     waitfunc(2)
     print('You: "Way to stay alert soldier. Carry on.')
     waitfunc(2)
     print("The guard is too stunned to stop you from passing by.")
     pass_guard()


def convinceinvis(): # Easter Egg to convice guard you're invisible
     print("You feel a weird tingling.")
     print('You: "...You can see me? Wilson, do you see what this means?"')
     waitfunc(2)
     print('Guard: "Huh?"')
     waitfunc(2)
     print('You: "I was able to make myself turn invisible through sheer mental will. Pretty soon I will be exploding rabbits just by thinking about it."')
     ch = ranch(1, 3)

     if ch == 3:
          waitfunc(2)
          print("The guard is too stunned to stop you from passing by.")
          pass_guard()
     else:
          print('Guard: "You are so obviously one of the prisoners here."')
          waitfunc(2)
          print("You are dragged back to your cell.")
          playagain()


def actguard(): # Act like a guard choice
     print('You: "Woah, wait I am a guard too!"')
     ch = ranch(1, 2)
     if ch == 2:
               print("You feel a weird tingling.")
               waitfunc(2)
               print('Guard: “YOU ARE OUT OF UNIFORM, SOLDIER! WHERE IS YOUR POWER ARMOR!?”')
               waitfunc(2)
               print('You: "Some guy stole it!"')
               waitfunc(2)
               print('Guard: "THE TRUTH IS YOU LOST AN EXPENSIVE PIECE OF ARMY-ISSUE EQUIPMENT.')
               waitfunc(2)
               print('Guard: “AND YOU WILL REMAIN IN THIS MANS ARMY UNTIL YOU ARE...\nFIVE HUNDRED AND TEN YEARS OLD, WHICH IS THE NUMBER OF YEARS IT WILL TAKE FOR YOU TO PAY FOR A MARK II POWERED COMBAT ARMOR YOU HAVE LOST!”')
               waitfunc(2)
               print('You: "Sorry, sergeant."')
               ch = ranch(1, 3)
               if ch == 2:
                    print('Guard: "Report back to the Armory and have a new suit issued to you immediately. Dismissed!"')
                    impersonation()
               else:
                    print('Guard: "Wait....You are not one of my soldiers."')
                    waitfunc(2)
                    print("The Guard reconizes you, dragging you back to your cell.")
                    playagain()
     else:
          print("You are dragged back to your cell.")
          uinv.clear()
          waitfunc(2)
          game()

def guard_check(): # Checks for items to pass or convince guard
     if "charm_spell" in uinv:
          waitfunc(3)
          print("You cast the charming spell on the nearby Guard, near instantly they begin to look at you seductively.\n")
          waitfunc(2)
          print('Guard: "Why hello there, what brings you here?"\n')
          print('You: "I need to get something past you, mind if you let me through?"\n')
          waitfunc(2)
          print('Guard: "No problem at all my dear."\n')
          print("You wink at the guard, they step aside and let you through.")
          waitfunc(2)
          pass_guard()


     elif "guard_armor" in uinv:
          waitfunc(3)
          print("You slip on the Guard's armor and confidently waltz past them.\n")
          waitfunc(2)
          print("The Guard stares as you for a moment but nods approvingly.\n")
          print("You manage to fool the Guard and walk right past, towards the exit.\n")
          waitfunc(2)
          pass_guard()

     else:
          print("You stand face to face with the Guard, they stare at you baffled.\n")
          print('Guard: "Hey, you! What are you doing here?!"')
          waitfunc(2)
          guardinteract = input("What will you say/do? (type a letter)\nA. Say you're a guard.\nB. Convice them you're invisible.\nC. Stun Guard.\nD. Attack.\n")

          if guardinteract.lower() == "a":
               actguard()
               

          elif guardinteract.lower() == "b":
               convinceinvis()

          elif guardinteract.lower() == "c":
               stunguard()

          elif guardinteract.lower() == "d":
               attackguard()
               pass_guard()


def escape_jailcell(): # Escaoe jail cell dialogue and options
     print("You have escaped your cell. After many, many flights of stairs, you come to a hallway with three options.")
     hall = input("Will you go: \nA. Left?\nB. Right?\nC. Straight?\n(type a letter)\n")
     if hall.lower() == "a":
          print("You go into the door on the left. Inside is a library. You see a mysterious book with a leather cover on a table.\nIt seems to be calling you.")
          book = input("Will you take it?\nYes\nNo \n")
          if book.lower() == "yes":
                print("You pick up the book and open it. There are several spells and some missing pages. \nOne particular spell is a charming spell. You make a mental note.\nYou look around the library for a little while before you get bored and leave.\n")
                uinv.append("charm_spell")
                guard_check()

          elif book.lower() == "no":
                print("You leave the book on the table. \nYou look around the library for a little while before you get bored and leave.\n")
                guard_check()

          elif book.lower() == "die":
                print("You say a random spell from the book to test it out. You immediately die of dysentery.")
                playagain()

     elif hall.lower() == "b":
            print("You go right and end up in the guards' quarters. There are several beds and one set of armor.")
            print("No one is here now. Nobody would see you take the armor...")
            armor = input("Steal the armor?\nYes\nNo \n")

            if "y" in armor.lower():
                  print("You quickly grab the armor and put it on. \nYou're now disguised as a guard. This will be very useful.")
                  print("There is nothing else to see, so you leave the guards' quarters.\n")
                  uinv.append("guard_armor")
                  guard_check()

            elif "n" in armor.lower() == "no":
                  print("You leave the armor and quickly make your exit.\n")
                  guard_check()

            elif armor.lower() == "die":
                  print("Your determination fizzled out and you died of dysentery.")
                  playagain()

     elif hall.lower() == "c":
          guard_check()

     elif hall.lower() == "die":
          print("You gave up on escaping and died of dysentery.")
          playagain()

def pass_guard(): # after passing guard, dialogue and choices
     global name
     print("After dealing with the guard, you look down the horizontal hallway that intersects the hallway you've been traveling.\nDirectly in front of you is the locked door to the castle.\nTo finally escape, you must find a way to unlock the door.\n")
     intsect = input("Which way will you go?\nA. Right\nB.Left\n(type a letter)\n")

     if intsect.lower() == "a":
          print("You head right.\nDown the hallway is a room full of books and a single desk. \nThere is a spell to unlock the door on the desk. You take it.")
          uinv.append("unlock_spell")
          egg = input("There is a sheet of paper next to the unlocking spell. Read it?\nYes\nNo\n")
          if egg.lower() == "yes":
               print("The sheet is labelled Easter Eggs.")
               print("Try this next time you play:")
               print("*Jumping out of the window in your cell\n*Convincing the guard at your cell that he's not real\n*Just type 'die'\n")
               print("Odd.")
               print("You return to the castle entrance, spell in hand")
               castle_door()
        
          elif egg.lower() == "no":
               print("Too bad. You're getting out of here.")
               print("You return to the castle entrance, spell in hand")
               castle_door()
        
          elif egg.lower() == "die":
               print("You gave up on escaping and died of dysentery.")
               playagain()

     elif intsect.lower() == "b":
          print("You head left.\nDown the hallway is a room with a wall of keys and a desk with files on top. \nThere is also key to unlock the door on the desk. You take the key.")
          uinv.append("door_key")
          file = input("While you are grabbing the key, you see a file on the desk with your name on it. \nDo you want to read it?\nYes\nNo\n")
    
          if file.lower() == "yes":
               print("You open the file and read it. The file says you are wanted for treason, and states the exact reason:\n")
               note = "{0} was imprisoned because they said, 'Honestly? King's kinda mid.'".format(name)
               print(note)
               fair = input("Do you believe that is fair?\nYes\nNo\n")
        
               if "y" in fair.lower():
                    print("That's fair.")
                    
               elif "n" in fair.lower():
                    print("That's a stupid reason.")
                    
               elif fair.lower() == "die":
                    print("The reason was so absurd that you died of dysentery.")
                    playagain()
            
               print("You return to the castle entrance, key in hand.")
               castle_door()
        
          elif "n" in file.lower():
               print("You return to the castle entrance, key in hand.")
               castle_door()
        
          elif file.lower() == "die":
               print("You gave up on escaping and died of dysentery.")
               playagain()
        
     elif intsect.lower() == "die":
          print("You gave up on escaping and died of dysentery.")
          playagain()

def bribeguard(): # Bribe the guard
     print('You: "I can get money. I will make a dead drop once I am out."')
     waitfunc(2)
     ch = ranch(1, 3)
     if ch == 3:
          waitfunc(1)
          print('Guard: "Hmm...Fine I will let you out. If you get caught, I have nothing to do with your escape."')
          escape_jailcell()

     else:
          print('Guard: "Ha. Nice Try."')
          dialogue = input("What will you say/do? (type a letter)\nA. Search haypile\n")
          if dialogue.lower() == "a":
            haypile()
            dialogue = input("What will you say/do? (type a letter)\nA. Unlock Jailcell\n")

            if dialogue.lower() == "a":
                 escape_jailcell()

def haypile(): # Check haypile
     print("You examine the hay pile.")
     waitfunc(2)
     print("After running your hands through the hay you manage to find a key.")
     uinv.append("cell_key")


def combust(): # Literally just explode
     print("You randomly combust.")
     waitfunc(2)
     print("You died!\nGame Over.")
     waitfunc(2)
     playagain()   

def claiminnocence(): # Claim you're innocent
     print('You: "I am not the guy you think I am. There has been a mistake!')
     waitfunc(2)
     ch = ranch(1, 4)
     if ch == 4:
          print('Guard: "Hmm...Fine I will let you out. If you get caught, I have nothing to do with your escape."')
          escape_jailcell()
     else:
          print('Guard: "Ha. Nice Try."')
          dialogue = input("What will you say/do? (type a letter)\nA. Search haypile\n")
          if dialogue.lower() == "a":
            haypile()
            dialogue = input("What will you say/do? (type a letter)\nA. Unlock Jailcell\n")
            if dialogue.lower() == "a":
                 escape_jailcell()

def offerorb(): # Offer Guard an Orb
     print('You: "I...can give you... this cool orb I found...??" ')
     waitfunc(2)
     print('Guard: "Hmm...Fine I will let you out. If you get caught, I have nothing to do with your escape."')
     escape_jailcell()

def talkguard(): # Talk to Guard from jailcell
     
    print('You: "Hey...Hey, guard!"')
    print('The guard looks at you with an annoyed expression before responding, "What?!"\n')
    waitfunc(2)
    print('You: "Listen. I need out of here. You have a key, right?"\n')
    waitfunc(2)
    print('The guard does not respond.\n')
    waitfunc(1)

def window(): # Jump from window easter egg
     ch = ranch(1, 2)
     if ch == 2:
              windowwin()
     else:
          print("You jump from the window and plummet to your death.")
          waitfunc(1)
          print("You died!\nGame Over.")
          waitfunc(1)
          playagain()

def wallbreak(): # Break the 4th wall easter egg
     print("You feel a weird tingling")
     waitfunc(2)
     print('You: "You are not real."')
     waitfunc(2)
     print('Guard: "What?"')
     waitfunc(2)
     print('You: "You are literally not real, this is a video game."')
     waitfunc(2)
     print('Guard: "No wonder you are in here, you are crazy."')
     waitfunc(2)
     print('You: "No, I am not. You are part of this game I am playing."')
     waitfunc(2)
     print('Guard: "W-What?"')
     waitfunc(2)
     print('You: "That is why you have no family and no personality. You are part of a game.')
     waitfunc(2)
     print('Guard: "N-No. No. No way. No no no."')
     waitfunc(2)
     print('You: "And since I am real and you are not, how about you let me out?"')
     waitfunc(2)
     print("The Guard opens the jail cell, and weeps on the floor, having come to the realization that they are not real.")
     escape_jailcell()


# Main Game Function
def game():
     intro()
     cellchoice()

play()