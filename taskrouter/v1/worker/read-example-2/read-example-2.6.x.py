# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

workers = client.taskrouter \
                .workspaces('WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                .workers \
                .list(target_workers_expression="type == 'leads'", limit=20)

for record in workers:
    print(record.sid)
