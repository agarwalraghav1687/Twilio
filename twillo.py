from twilio.rest import Client 
import os

account_sid = os.environ('account_sid')
auth_token = os.environ('auth_token')
client = Client(account_sid, authtoken)

message = client.messages \
                .create(
                    body="Hello! I am Raghav",
                    from_='+17074143199',
                    to='+91 8273731481'
                )

print(message.sid)