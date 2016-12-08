import random
import smtplib
 
def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

def randomList(oldList):
    newList = []
    for i in range(0,len(oldList)):
        listIndex = random.randint(0,len(oldList) - 1)
        newList.append(oldList[listIndex])
        oldList.pop(listIndex)
    return newList

def shiftList(oldList):
    newList = []
    for element in oldList:
        newIndex = oldList.index(element)
        if newIndex >= len(oldList) - 1:
            newIndex = 0
        newList.insert(newIndex, element)
    return newList


presents = ['charlie bishop','sam cardy','adam houldershaw','joseph jones','halley woods']
santas = []

emails = {'charlie bishop':'charliebishop21@live.co.uk',
          'sam cardy':'sam@gmail.com',
          'adam houldershaw':'adam@hotmail.co.uk',
          'joseph jones':'joseph@aldergrange.com',
          'halley woods':'halley@live.co.uk'}

presents = randomList(presents)
santas = shiftList(presents)

for i in range(0,len(presents)):
    
    present = presents[i]
    santa = santas[i]
    
    print (emails[santa])
    
    sendemail(from_addr    = 'test@gmail.com', 
              to_addr_list = [emails[santa]],
              subject      = 'your secret santa', 
              message      = present, 
              login        = 'test@gmail.com', 
              password     = '1234')    



