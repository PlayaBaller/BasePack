import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)

conn.ehlo()

conn.starttls()

conn.login('*********', '***************')

conn.sendmail('***********', '*********', 'Subject: Hello, Hustle!...\n\nStrive for '
                                                                        'greatness')
conn.quit()
