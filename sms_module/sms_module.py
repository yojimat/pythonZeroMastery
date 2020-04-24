from twilio.rest import Client

account_sid = "accoutn"
auth_token = "auth"
client = Client(account_sid, auth_token)

message = client.messages.create(
        from_ = "+99999999",
        body = "Mensagem SMS",
        to= "+556199999999"
    )

print(message.sid)b