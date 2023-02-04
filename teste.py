
from twilio.rest import Client

accont_sid = "ACf1ef8fb2ded21784e7354aaf2e33ceae"
auth_token = "09ab2d190d0cd98acc322254c3943438"
client = Client(accont_sid,auth_token)
client.messages.create(from_="+16064412876",body="merda",to="+5518981288077")