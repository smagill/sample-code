# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

sync_map_item = client.sync \
                      .services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                      .sync_maps('Players') \
                      .sync_map_items \
                      .create(ttl=864000, key='steph_curry', data={
                           'name': 'Stephen Curry',
                           'level': 30,
                           'username': 'spicy_curry'
                       })

print(sync_map_item.key)
