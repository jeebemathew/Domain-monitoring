import requests
import smtplib, ssl
import email
urls = [
  'https://freevideolectures.com',
  'https://www.guru99.com/',
  'https://linuxjourney.com',
  'https://www.quora.com',
  'https://www.tecmint.com',
  'https://linuxsurvival.com',
  'https://www.tutorialspoint.com',
  'https://www.computerworld.com',
  'https://hackernoon.com',
  'https://www.howtoforge.com',
  'https://asdfg.com',
  'https://www.ubuntupit.com/',
  'https://www.techworm.net',
  'https://www.2daygeek.com/',
  'https://www.linux.org',
  'https://linuxacademy.com',
  'https://www.cyberciti.biz',
  'https://itsfoss.com',
  'https://blog.feedspot.com',
  'https://www.techradar.com',
  'https://phoenixts.com/',
  'https://training.linuxfoundation.org',
  'https://www.reallinuxuser.com/',
  'https://linuxconfig.org',
  'https://sourceforge.net',
  'https://www.makeuseof.com'
]


file= open('myfile.txt','w')

for url in urls:
    try:
     response = requests.get(url)

     if response.status_code == requests.codes.OK:
        print('{:40} [ {} ] : Up'. format( url,response.status_code))
    
     else:
        print('{:40} [ {} ] : DOWN' .format( url, response.status_code))

        file.write(url + ' is offline \n')
    except:
       print('{:40} [ {} ] : Error' .format(url,'000'))

       file.write(url + ' is getting an error \n')

file.close()


username = 'je****@gmail.com'
password = input(' Enter your  email account password : ')


report = email.message.EmailMessage()

report['From'] = username
report['Subject'] = 'Scanning Report attached'
report['To'] = [ 'jee****@gmail.com','je****@hotmail@com' ]

with open('myfile.txt','r') as fh:
  data = fh.read()
  
report.add_attachment(data,subtype='text',filename='myfile.txt')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
  smtp.login(username,password)
  smtp.send_message(report)
print( 'The report is sending..... ')  
