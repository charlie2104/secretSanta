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



presents = ['charlie bishop','sam cardy','adam houldershaw','joseph jones','halley woods']
santas = ['charlie bishop','sam cardy','adam houldershaw','joseph jones','halley woods']

emails = {'charlie bishop':'charliebishop21@live.co.uk',
          'sam cardy':'sam@gmail.com',
          'adam houldershaw':'adam@hotmail.co.uk',
          'joseph jones':'joseph@aldergrange.com',
          'halley woods':'halley@live.co.uk'}

choices = len(presents)
while choices > 0:
    
    present = random.choice(presents)
    santa = random.choice(santas)

    if str(present) != str(santa):
        presents.remove(present)
        santas.remove(santa)
        print (emails[santa])

        sendemail(from_addr    = 'test@gmail.com', 
                  to_addr_list = [emails[santa]],
                  subject      = 'your secret santa', 
                  message      = present, 
                  login        = 'test@gmail.com', 
                  password     = '1234')    

        choices -= 1


