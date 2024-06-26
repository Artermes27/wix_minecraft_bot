import pyautogui as pt
from time import sleep
import os.path
import os

def auction(username, amount):
    sleep(5)
    print('starting the auctioning proses')
    pt.keyDown('e')
    pt.keyUp('e')
    sleep(0.5)
    pt.moveTo(450, 400)
    pt.click()
    pt.moveTo(900, 400)
    pt.click(button = 'right')
    pt.moveTo(450, 400)
    pt.click()
    pt.keyDown('esc')
    pt.keyUp('esc')
    pt.keyDown('/')
    pt.keyUp('/')
    pt.write('trade ' + username)
    pt.keyDown('enter')
    pt.keyUp('enter')
    sleep(10)
    pt.moveTo(900, 460)
    pt.click()
    sleep(10)
    pt.moveTo(630, 370)
    pt.click()
    sleep(120)
    #tell them to put it on the auction house
    pt.keyDown('/')
    pt.keyUp('/')
    pt.keyDown('backspace')
    pt.keyUp('backspace')
    pt.write('put the dimond block on the auction house for 1M and i will pay for it with the amount you orderd. in 2 minuits time!')
    pt.keyDown('enter')
    pt.keyUp('enter')
    sleep(1)
    #beging auctioning for the item with their amount
    pt.keyDown('/')
    pt.keyUp('/')
    command = 'ah ' + username
    pt.write(command)
    pt.keyDown('enter')
    pt.keyUp('enter')
    sleep(1)
    pt.moveTo(520, 250)
    pt.click()
    sleep(1)
    pt.moveTo(680, 280)
    pt.click()
    sleep(0.5)
    pt.write(str(amount))
    pt.moveTo(670, 580)
    pt.click()
    sleep(0.5)
    pt.moveTo(570, 280)
    pt.click()
    sleep(1)
    pt.moveTo(570, 250)
    pt.click()
    sleep(1)
    pt.keyDown('esc')
    pt.keyUp('esc')
    
def recon():
  pt.keyDown('alt')
  pt.keyDown('1')
  pt.keyUp('alt')
  pt.keyUp('1')
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
  sleep(10)
  #alow time to reconect if hypixle is being slow
  print('completed the recon now in the skyblock home island')

def discon():
  pt.keyDown('esc')
  pt.keyUp('esc')
  pt.moveTo(650,550)
  pt.click()
  pt.moveTo(700, 450)
  pt.click()
  pt.keyDown('alt')
  pt.keyDown('3')
  pt.keyUp('alt')
  pt.keyUp('3')

def file(order_number):
  #creating the folder for the records to go into
  new_file = '/home/artermes27/Documents/minecraft_bot/MinecraftCoinGifter/records/' + str(order_number)
  os.mkdir(new_file)
  coppy_command = 'cp /home/artermes27/Downloads/Orders.csv ' + new_file + '/Orders.csv'
  os.system(coppy_command)
  print('coppied orders.csv file into directory ' + str(order_number))
  os.system('rm /home/artermes27/Downloads/Orders.csv')
  #retreving the fufillment screenshot and puting it in a folder
  png_name = check_logs(2)
  png_name = png_name.split(' as ')
  png_name = str(png_name[1])
  png_name = png_name.replace('\n', '')
  print(png_name)
  #coppy_command = 'cp file:///home/user1/.minecraft/screenshots/' + ' ' + new_file + '/proof.png'
  os.system('touch ' + new_file + '/png_name.txt')
  coppy_command = 'echo ' + png_name + ' >> ' + new_file + '/png_name.txt'
  print(coppy_command)
  os.system(coppy_command)
  #moving back to the terminal so the logs can be seen
  pt.keyDown('alt')
  pt.keyDown('3')
  pt.keyUp('alt')
  pt.keyUp('3')

def check_for_order():
  #tries to download top order if it doesent exist returns false if it does then true
  sleep(2)
  pt.keyDown('alt')
  pt.keyDown('2')
  pt.keyUp('alt')
  pt.keyUp('2')
  sleep(1)
  #reload the sight
  pt.keyDown('ctrl')
  pt.keyDown('r')
  pt.keyUp('ctrl')
  pt.keyUp('r')
  sleep(15)
  #trying to download
  pt.moveTo(310, 420)
  pt.click()
  pt.moveTo(1150, 330)
  sleep(1)
  pt.click()
  pt.moveTo(920,650)
  sleep(1)
  pt.click()
  #going back to the previous blackarch page
  pt.keyDown('alt')
  pt.keyDown('3')
  pt.keyUp('alt')
  pt.keyUp('3')
  sleep(5)
  bol = os.path.isfile('/home/artermes27/Downloads/Orders.csv')
  return bol

def fufill_order(order_number):
  print('finished order ' + str(order_number))
  #moves it to firefox and fufills/archives the order
  pt.keyDown('alt')
  pt.keyDown('2')
  pt.keyUp('alt')
  pt.keyUp('2')
  pt.moveTo(900, 330)
  pt.click()
  sleep(5)
  pt.moveTo(1270, 330)
  pt.click()
  pt.keyDown('alt')
  pt.keyDown('3')
  pt.keyUp('alt')
  pt.keyUp('3')

def use_chat(message, switch_site, first_time):
  sleep(1)
  if switch_site == True:
    pt.keyDown('alt')
    pt.keyDown('2')
    pt.keyUp('alt')
    pt.keyUp('2')
  pt.keyDown('ctrl')
  pt.keyDown('tab')
  pt.keyUp('ctrl')
  pt.keyUp('tab')
  sleep(0.25)
  if first_time == True:
    pt.moveTo(360, 330)
    pt.click
  sleep(0.25)
  pt.moveTo(611, 660)
  pt.click
  pt.write(str(message))
  pt.moveTo(1280, 700)
  pt.click()
  pt.keyDown('ctrl')
  pt.keyDown('tab')
  pt.keyUp('ctrl')
  pt.keyUp('tab')
  if switch_site == True:
    pt.keyDown('alt')
    pt.keyDown('1')
    pt.keyUp('alt')
    pt.keyUp('1')

def custom_order(order_no, acount_variabe):
  order_no = str(order_no)
  order_no = order_no.replace(' \'', '')
  order_no = order_no.replace('"', '')
  acount_variabe = acount_variabe.split('|')
  acount_name = str(acount_variabe[1])
  acount_name = acount_name.split(':')
  acount_name = str(acount_name[1])
  acount_name = acount_name.replace('"', '')
  acount_name = acount_name.replace(']', '')
  acount_name = acount_name.replace("'", '')  
  acount_name = acount_name.replace('\\n', '')
  amount_of_coins = str(acount_variabe[0])
  amount_of_coins = amount_of_coins.split(':')
  amount_of_coins = str(amount_of_coins[1])
  amount_of_coins = amount_of_coins + '000000'
  amount_of_coins = amount_of_coins.replace(' ', '')
  return_aray = [order_no, amount_of_coins, acount_name]
  return return_aray

def interpret_orders():
  #start interpreting the orders file
  orders = open('/home/artermes27/Downloads/Orders.csv')
  orders.close
  orders = str(orders.readlines())
  orders_aray = orders.split(',')
  #turning the elements to strings
  order_number = str(orders_aray[4])
  order = str(orders_aray[5])
  quantity = str(orders_aray[6])
  acount = str(orders_aray[7])
  #put the order in the right format if it is not custom (removing the crap)
  order_number = order_number.replace("'", '')
  order_number = order_number.replace('"', '')
  order_number = order_number.replace(" ", '')
  order = order.replace("'", '')
  order = order.replace('"', '')
  order = order.replace(' ', '')
  quantity = quantity.replace('"', '')
  quantity = quantity.replace(',', '')
  quantity = int(quantity)
  acount = acount.replace("'", '')
  acount = acount.replace('"', '')
  acount = acount.replace(']', '')
  acount = acount.replace('\\n', '')
  #getting the true username out as a string
  acount = acount.split(':')
  acount = str(acount[1])
  #figuring out what amount the order is for
  if str(order) == 'customamountofcoins$0.20permil':
      order = 1000000
  if str(order) == '1Billionskyblockcoins':
    amount = '1000000000'
  if str(order) == '500Mskyblockcoins':
    amount = '500000000'
  if str(order) == '200Mskyblockcoins':
    amount = '200000000'
  if str(order) == '100Mskyblockcoins':
    amount = '100000000'
  if str(order) == '50Mskyblockcoins':
    amount = '50000000'
  if str(order) == '20Mskyblockcoins':
    amount = '20000000'
  if str(order) == '10Mskyblockcoins':
    amount = '10000000'
  print(order)
  print(quantity)
  print(acount)
  order = int(amount) * int(quantity)
  amount = str(order)
  return_aray = [order_number, amount, acount]
  return return_aray

def check_logs(posision):
  f = open('/home/artermes27/.minecraft/logs/latest.log', 'r')
  latest_aray = f.readlines()
  return latest_aray[int(len(latest_aray) - posision)]

def party(user):
  user = str(user)
  user = user.replace('\n', '')
  command = 'p ' + user
  pt.keyDown('/')
  pt.keyUp('/')
  pt.write(command)
  pt.keyDown('enter')
  pt.keyUp('enter')
  #check if the party request was sucsesfull
  online = str(check_logs(2))
  online = online.split(':')
  online = str(online[3])
  online = online.replace('\n', '')
  print(online)
  #add in here the contacting the user part that alows them to redo usernames or come online
  if online == " [CHAT] You cannot invite that player since they're not online.":
    use_chat('you are not online come online for skyblock the next request will happen in 1 minuite', True, False)
  if online == " [CHAT] Couldn't find a player with that name!":
    print('the username was not valid we will create a full refund')
    use_chat('the username you gave us was not valid and we canot transfer the coins to you because of it. a full refund will be isued within one day!', True, True)
  else:
    print('the party invite to ' + str(user) + ' has been sucsesfull')

def warp():
  command = 'p warp'
  pt.keyDown('/')
  pt.keyUp('/')
  pt.write(command)
  pt.keyDown('enter')
  pt.keyUp('enter')

def trade(user):
  command = 'trade ' + user
  pt.keyDown('/')
  pt.keyUp('/')
  pt.write(command)
  pt.keyDown('enter')
  pt.keyUp('enter')
  logs = str(check_logs(2))
  logs = logs.split()
  print('the trade with ' + user + ' has begun!')
  #this checks that they have acepted the trade
  sleep(11)
  online = str(check_logs(1))
  online = online.split(':')
  online = str(online[3])
  online = online.replace('\n', '')
  online = online.split('to')
  #online = online.replace('[VIP ]', '')
  #online = online.replace('[VIP+ ]', '')
  #online = online.replace('[MVP]', '')
  #online = online.replace('[MVP+ ] ', '')
  #online = online.replace('[MVP++] ', '')
  if str(online[0]) == ' [CHAT] Your /trade request ':
    print('the trade was not acepted in time')
    pt.keyDown('/')
    pt.keyUp('/')
    pt.keyDown('backspace')
    pt.keyUp('backspace')
    pt.write('you did not accept the trade request in time it will try again in 10 secconds')
    pt.keyDown('enter')
    pt.keyUp('enter')
    sleep(10)
    #trying the trade again
    pt.keyDown('/')
    pt.keyUp('/')
    pt.write(command)
    pt.keyDown('enter')
    pt.keyUp('enter')
    online = str(check_logs(1))
    online = online.split(':')
    online = str(online[3])
    online = online.replace('\n', '')
    online = online.split('to')
    if str(online[0]) == ' [CHAT] Your /trade request ':
      print('the trade was not acepted in time for a seccond time')
      pt.keyDown('/')
      pt.keyUp('/')
      pt.keyDown('backspace')
      pt.keyUp('backspace')
      pt.write('you did not accept the trade request for a seccond time you will have one more go')
      pt.keyDown('enter')
      pt.keyUp('enter')
      sleep(10)
      #trying the trade again
      pt.keyDown('/')
      pt.keyUp('/')
      pt.write(command)
      pt.keyDown('enter')
      pt.keyUp('enter')
      online = str(check_logs(1))
      online = online.split(':')
      online = str(online[3])
      online = online.replace('\n', '')
      online = online.split('to')
      if str(online[0]) == ' [CHAT] Your /trade request ':
        print('the trade was not acepted in time for the last time give a refund to the user ' + user + ' time')
        pt.keyDown('/')
        pt.keyUp('/')
        pt.keyDown('backspace')
        pt.keyUp('backspace')
        pt.write('you did not acept the trade request for the last time you will be isued a full refunded within 1 day')
        pt.keyDown('enter')
        pt.keyUp('enter')
        pt.keyDown('/')
        pt.keyUp('/')
        pt.keyDown('backspace')
        pt.keyUp('backspace')
        pt.write('you can order again but accept the trade request next time')
        pt.keyDown('enter')
        pt.keyUp('enter')
        return False

def coins_in(amount):
  pt.moveTo(465, 390)
  pt.click()
  sleep(1)
  pt.write(str(amount))
  pt.moveTo(685, 605)
  pt.click()
  print(str(amount) + ' coins has been enterd!')

def accept_trade(order_number):
  pt.moveTo(625, 390)
  pt.click()
  print('the user has accepted the trade!')
  #taking a screenshot
  sleep(5)
  pt.keyDown('f2')
  pt.keyUp('f2')
  pt.keyDown('/')
  pt.keyUp('/')
  pt.keyDown('backspace')
  pt.keyUp('backspace')
  pt.write('just took a screenshot of the trade you are order number ' + str(order_number))
  pt.keyDown('enter')
  pt.keyUp('enter')

def remove(user):
  pt.keyDown('alt')
  pt.keyDown('1')
  pt.keyUp('alt')
  pt.keyUp('1')
  sleep(1)
  pt.keyDown('/')
  pt.keyUp('/')
  command = 'p chat good doing buisness with you!'
  pt.write(command)
  pt.keyDown('enter')
  pt.keyUp('enter')
  sleep(1)
  pt.keyDown('esc')
  pt.keyUp('esc')
  command = 'party remove ' + str(user)
  pt.keyDown('/')
  pt.keyUp('/')
  pt.write(command)
  pt.keyDown('enter')
  pt.keyUp('enter')
  print(str(user) + ' has been removed from the party!')

choice = '1'
while choice != '0':
  print('0: quit the menue')
  print('1: run the full code')
  print('2: party someone')
  print('3: party warp the person')
  print('4: trade with someone')
  print('5: check the chat logs')
  print('6: check the interpreted order if it is custom(outdated)')
  print('7: download and interpret the orders file')
  print('8: chat to the website')
  print('9: fufill the order and archive')
  print('10: find out if orders.csv exists')
  print('11: file proof of purchase fufill order and remove Orders.csv file')
  print('12: disconect from minecraft (discon)')
  print('13: reconect to minecraft and load into the skyblock world')
  print('14: mark the order as fufilled and archive it on wix')
  print('15: give user the item and buy it back')
  print('------------------------------------------------------------------')
  choice = str(input('what do you chose:'))
  if choice == '1':
    #creating an indefinate loop for option 1
    while choice != '0':
      order_status = check_for_order()
      print(order_status)
      while order_status == False:
        sleep(45)
        orders_status = check_for_order()
      else:
        #creats an aray of the order in the format [order number, order(a value as a string), acount it goes to]
        order = interpret_orders()
        sleep(10)
        print(order)
        #conecting minecraft up to hypixel
        recon()
        sleep(10)
        if party(order[2]) == True:
            print('the party failed in some way shape or form')
            os.system('rm /home/artermes27/Downloade/Orders.csv')
            fufill_order()
            order_status = False
            discon()
            exit()
        sleep(10)
        warp()
        sleep(10)
        if int(order) <= 20000000:
            print('the order will be fufilled by trade')
            if trade(order[2]) == False:
                remove(order[2])
                os.system('rm /home/artermes27/Downloads/Orders.csv')
                discon()
                order_status = check_for_order()
                exit()
            sleep(10)
            coins_in(order[1])
            sleep(10)
            accept_trade(order[0])
            sleep(2)
            file(order[0])
            sleep(1)
            fufill_order(order[0])
            sleep(10)
            remove(order[2])
            sleep(1)
            discon()
            order_status = check_for_order()
            print('order has finsihed prosesing and has been fufilled going back to loop of searching')
        else:
            auction(str(order[1]), str(order[2]))
            sleep(0.5)
            file(order[0])
            sleep(1)
            fufill_order(order[0])
            sleep(10)
            remove(order[2])
            sleep(1)
            discon()
            order_status = check_for_order()
            print('order has finsihed prosesing and has been fufilled going back to loop of searching')
  
  if choice == '2':
    party('artermes1')
  if choice == '3':
    warp()
  if choice == '4':
    sleep(5)
    trade('artermes1')
  if choice == '5':
    print(check_logs(2))
  if choice == '6':
    custom_order('1006', '"how many coins (in million):10 | what account is it going to:artemes1"')
  if choice == '7':
    print(interpret_orders())
  if choice == '8':
    use_chat('hello user', True, False)
  if choice == '9':
    fufill_order()
  if choice == '10':
    print(check_for_order())
  if choice == '11':
    file(10004)
  if choice == '12':
    sleep(5)
    discon()
  if choice == '13':
    recon()
  if choice == '14':
    fufill_order(1004)
  if choice == '15':
      sleep(2)
      auction('artermes27', 1000000)
print('code has finished running!(somthing probly went wrong!')
