import pyautogui as pt
from time import sleep

def check_logs(posision):
   f = open('/home/user1/.minecraft/logs/latest.log', 'r')
   latest_aray = f.readlines()
   return latest_aray[int(len(latest_aray) - posision)]

def back_and_forth(reps):
  x = 0
  while x != reps:
    sleep(1)
    pt.keyDown('i')
    sleep(1)
    pt.keyDown("d")
    sleep(30)
    pt.keyUp("d")
    sleep(1)
    pt.keyUp('i')
    pt.keyDown('d')
    sleep(1)
    pt.keyUp('d')
    pt.keyDown("w")
    sleep(1)
    pt.keyUp("w")
    pt.keyDown('i')
    pt.keyDown("a")
    sleep(30)
    pt.keyUp("a")
    pt.keyUp('i')
    pt.keyDown('a')
    sleep(1)
    pt.keyUp('a')
    pt.keyDown('w')
    sleep(1)
    pt.keyUp('w')
    x = x + 1

def back_and_forth_alt(reps):
   x = 0
   while x != reps:
     sleep(1)
     pt.keyDown('i')
     sleep(1)
     pt.keyDown("A")
     sleep(36)
     pt.keyUp("A")
     sleep(1)
     pt.keyUp('i')
     pt.keyDown('A')
     sleep(1)
     pt.keyUp('A')
     pt.keyDown("W")
     sleep(1)
     pt.keyUp("A")
     pt.keyDown('i')
     pt.keyDown("D")
     sleep(36)
     pt.keyUp("D")
     pt.keyUp('i')
     pt.keyDown('d')
     sleep(1)
     pt.keyUp('d')
     pt.keyDown('w')
     sleep(1)
     pt.keyUp('w')
     x = x + 1

def discon_recon(x):
  pt.keyDown('esc')
  pt.keyUp('esc')
  pt.moveTo(650,550)
  pt.click()
  pt.moveTo(650,450)
  pt.click()
  pt.moveTo(625,150)
  pt.click()
  pt.click()
  sleep(5)
  pt.keyDown('k')
  pt.keyUp('k')
  sleep(2)
  pt.moveTo(600, 200)
  pt.click()
  sleep(2)
  empty_inventory()
  pt.keyDown('i')
  sleep(1)
  pt.keyUp('i')
  pt.keyDown('1')
  pt.keyUp('1')
  print("finished")

def restart():
  pt.keyDown('esc')
  pt.keyUp('esc')
  pt.moveTo(650, 550)
  pt.click()
  pt.keyDown('esc')
  pt.keyUp('esc')
  pt.moveTo(900,650)
  pt.click()
  sleep(5)
  pt.write('./minecraft-launcher')
  pt.keyDown('enter')
  pt.keyUp('enter')
  pt.moveTo(600,400)
  sleep(10)
  pt.click()
  pt.click()
  pt.write('Country2.12')
  pt.keyDown('enter')
  pt.keyUp('enter')
  pt.moveTo(800, 575)
  sleep(2)
  pt.click()
  sleep(30)
  pt.moveTo(770, 460)
  pt.click()
  pt.keyDown('k')
  pt.keyUp('k')
  sleep(2)
  pt.moveTo(600, 200)
  pt.click()
  sleep(2)
  empty_inventory()
  pt.keyDown('i')
  sleep(1)
  pt.keyUp('i')
  pt.keyDown('1')
  pt.keyUp('1')
  print('the game launcher has reset!')

def empty_inventory():
  sleep(2)
  pt.keyDown('k')
  pt.keyUp('k')
  sleep(0.5)
  pt.moveTo(470, 500)
  pt.click()
  pt.click(button = 'right')
  pt.moveTo(890,510)
  pt.click()
  pt.keyDown('shift')
  pt.click()
  pt.keyUp('shift')
  pt.keyDown('esc')
  pt.keyUp('esc')
  print('dropped off netherwarts')

def hub_to_island():
  sleep(2)
  pt.keyDown('d')
  pt.keyUp('d')
  pt.keyDown('9')
  pt.keyUp('9')
  pt.keyDown('k')
  pt.keyUp('k')
  sleep(1)
  pt.moveTo(575, 420)
  pt.click()
  pt.moveTo(625, 255)
  pt.click()
  pt.keyDown('w')
  sleep(4)
  pt.keyUp('w')
  pt.keyDown('esc')
  pt.keyUp('esc')

def check_chat(statment):
  fileHandle = open ('/home/user1/.minecraft/logs/latest.log',"r" )
  lineList = fileHandle.readlines()
  fileHandle.close()
  print("The last line is:")
  last_line = lineList[len(lineList)-1]


choice = 0
while choice != 2:
  print("1: begin farming potatos")
  print("2: disconect the game and reconect")
  print("3: restart game launcher")
  print('4: show the mouse posision')
  print('5: empty potatos into chest')
  print('6: fast travel from hub to island')
  choice = int(input("what is your choice:"))
  if choice == 1:
    a = 0
    sleep(5)
    discon_recon('s')
    while a == 0:
      count1 = 0
      while count1 != 10:
        sleep(5)
        pt.keyDown("j")
        back_and_forth_alt(41)
        pt.keyUp("j")
        sleep(2)
        discon_recon('s')
        count1 = count1 + 1
      restart()

  if choice == 2:
    print("disconecting")
    sleep(5)
    discon_recon('s')

  if choice == 3:
    print('restarting game launcher')
    sleep(5)
    restart()
  if choice == 4:
    x = 0
    while x != 10:
      print(pt.position())
      x = x +1
      sleep(1)
  if choice == 5:
    empty_inventory()
  if choice == 6:
    sleep(5)
    discon_recon('s')
    hub_to_island()
    discon_recon('s')
  if choice == 7:
    statment = input('what do you want to search for in the last line:')
    check_chat(str(statment))
print("program ended")
