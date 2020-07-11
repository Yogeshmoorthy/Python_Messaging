from twilio.rest import Client
import pandas_usage

our_msg = pandas_usage.strt_df_conv
#Your Account Sid and Auth Token from twilio.com/console
#DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC459bfa38c65cea239782ecb0366742'
auth_token = 'fa44e3a2f26c8ed8f4839260a9439e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=our_msg,
                     from_='+12512903468',
                     to='+918940606699'
                 )
print(message.sid)
