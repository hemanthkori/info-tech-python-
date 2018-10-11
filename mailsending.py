import smtplib
server=smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login("hemanthkori007@gmail.com","heyyooo")
msg="hai ,helllo"
server.sendmail("hemanthkori007@gmail.com","ikhlaasrasib@gmail.com",msg)
server.quit()