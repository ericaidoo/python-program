from smtp import SendEmail

input("Press Enter to send an email")
# set email list (emails for the subscribers)
emailLists = ["sportsnewstk@mail.com", "aidooessuan@gmail.com"]

# Use this function to retrieve email addresses and start sending to all the subscribers
for email in emailLists:
    SendEmail(email) 
