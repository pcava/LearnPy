import win32com.client

# https://www.makeuseof.com/send-outlook-emails-using-python/
ol = win32com.client.Dispatch("outlook.application")
olmailitem = 0x0 #size of the new email
newmail = ol.CreateItem(olmailitem)
newmail.Subject = 'Test email'
newmail.To = 'paolo.cavatore@efgbank.com'
newmail.CC = 'paolo.cavatore@efgbank.com'
newmail.Body = 'Hello, this is a test email from Python'
# attach = 'C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
# newmail.Attachments.Add(attach)

# https://stackoverflow.com/questions/24192252/python-sending-outlook-email-from-different-address-using-pywin32
# If you want to set which address the e-mail is sent from. 
# From = None
# for myEmailAddress in ol.Session.Accounts:
# if "bi@efgbank.com" in str(myEmailAddress):
#	From - myEmailAddress
#	break
#
#	if From != None:
#	# This line basically calls the "mail.SendUsingAccount = xyz@email.com" outlook VBA command
#	newmail._oleobj_.Invoke(*(64209, 0, 8, 0, From))

# To display the mail before sending it:
newmail.Display()

# To just send it:
# newmail.Send()

