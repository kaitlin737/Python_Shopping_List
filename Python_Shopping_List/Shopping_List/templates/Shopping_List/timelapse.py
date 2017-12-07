from picamera import PiCamera
from os import system
from time import sleep
import smtplib
import subprocess
import imaplib
import email
import time

def checkEmail():
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('kcstark11@gmail.com','=********')
    mail.list()

    count=0
    while count < 120:
        try:
            mail.select("inbox")
            result,data=mail.search(None,'(UNSEEN FROM "kcstark11@gmail.com")')
            ids=data[0]
            id_list=ids.split()

            latest_email_id=id_list[-1]
            result,data=mail.fetch(latest_email_id,"(RFC822)")
            raw_email=data[0][1]

            recv_msg=email.message_from_string(raw_email)
            #checks for message
            if recv_msg['Subject']=="Start camera" or "Start Camera":
                #camera detected
                commandResult=subprocess.check_output("vcgencmd get_camera", shell=True)
                if commandResult==b'supported=1 detected=1\n':
                    print("connected")
                else:
                    print("not camera connected")

                camera=PiCamera()
                camera.capture('image.jpg')

                #takes photo
                for i in range(20):
                    camera.capture('image{0:04d}.jpg'.format(i))
                    sleep(1800)
                    #system('convert -delay 10 -loop 0 image*.jpg animation.gif')


                smtpUser='kcstark11@gmail.com'
                smtpPass='=********'

                #sends email that it is done
                toAdd='kcstark11@gmail.com'
                fromAdd=smtpUser

                subject='Motion Finished'
                header='To: ' +toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject

                body='Time  lapse completed'

                print header + '\n' +body

                s=smtplib.SMTP('smtp.gmail.com',587)

                s.ehlo()
                s.starttls()
                s.ehlo()

                s.login(smtpUser,smtpPass)
                s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

                s.quit()
            else:
                print("Denied")

            count=120
#continues checking if email is received
        except IndexError:
            time.sleep(30)
            if count < 119:
                count=count+1
                continue
            else:
                print("No response")
            count=120
checkEmail()

print('done')
