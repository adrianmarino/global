import smtplib

# ---------------------------------------------------------------
# Mailer Service.
#
# ---------------------------------------------------------------
class Mailer(object):

# ---------------------------------------------------------------
# Constructors
# ---------------------------------------------------------------

    def __init__(self, smtpUrl, user, password, fromAddress, toAddress,
                 broadCastAddress):
        self.smtpUrl = smtpUrl
        self.user = user
        self.password = password
        self.fromAddress = 'Service Account <'
        self.fromAddress += fromAddress
        self.fromAddress += '>'
        self.toAddress = toAddress.split()
        self.broadCastAddress = broadCastAddress



# ---------------------------------------------------------------
# Public methods
# ---------------------------------------------------------------

    def send(self, subject, body):
        tmpBody = ('From: %s\r\nTo: %s\r\nBcc: %s\r\nSubject: %s\r\n\r\n' %
                   (self.fromAddress, ', '.join(self.toAddress),
                    self.broadCastAddress, subject))
        tmpBody += body

        server = smtplib.SMTP(self.smtpUrl)
#        server.set_debuglevel()

        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(self.user, self.password)
        server.sendmail(self.fromAddress, self.toAddress, tmpBody)
        server.quit()

