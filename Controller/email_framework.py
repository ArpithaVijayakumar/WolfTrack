import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def s_email(company_name,location,job_Profile,salary,username,password,email,security_question,security_answer,notes,date_applied,status):

    sender_email = "wolftrackproject@gmail.com"
    receiver_email = email
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack++ - Job Application Added"
    body = "WOLFTRACK++ APPLICATION \n\n" \
           "You have applied to " + company_name + " for the job profile - " + job_Profile + \
           ". \nPlease find the details below: \n" \
           "Date Applied: " + date_applied + "\n" "Location: " + location + "\n" \
                                                                            "Salary: " + salary + "\n" \
                                                                                                  "User_name: " + username + "\n" \
                                                                                                                         "Password: " + password + "\n" \
                                                                                                                                                  "Security Question: " + security_question + "\n" \
                                                                                                                                                                                         "Security Answer: " + security_answer + "\n" "Status: " + status + "\n" \
                                                                                                                                                                                                                            "Notes: " + notes + "\n\n\n" \
                                                                                                                                                                                                                                        "All the best for you Application!\n" \
                                                                                                                                                                                                                                        "The WolfTrack++ Team."
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",
                          465,
                          context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True

if __name__ == "__main__":
    s_email('IBM','Raleigh','SDE','1','2','3','swetha11895@gmail.com','Favorite Sport','Badminton','11/25/2021','d','d')

