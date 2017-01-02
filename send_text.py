from twilio.rest import TwilioRestClient

account_sid = "ACcad4a9fc4ba202d353ff0423fe76a63e" # Your Account SID from www.twilio.com/console
auth_token  = "874781380522fa0d054886ce2645d451"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Ha Ha Ha :) we are comming for you",
    to="+4571349209",    # Replace with your phone number
    from_="+46769439164") # Replace with your Twilio number

print(message.sid)