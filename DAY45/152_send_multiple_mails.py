import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('adalovelace2003@gmail.com','donttrythispass')
subject = "test python"
body = "I love python "
message = f"subject: {subject}\n\n{body}"
listadd=['test1@gmail.com',"test2@gmail.com"]
ob.sendmail('adalovelace2003@gmail.com', listadd, message)
print(" Mail sent successfully!")
ob.quit()

 