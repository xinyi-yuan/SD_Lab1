# from vonage https://dashboard.nexmo.com/getting-started/sms

import vonage

client = vonage.Client(key="b97abc26", secret="ognhX5rUby9tMLxy")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "15713965612",
        "to": "13194129046",
        "text": "Hello World!",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")