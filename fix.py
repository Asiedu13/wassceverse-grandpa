import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='101ffcc471c203d5366944aae214abfb83ba179c7c09578afa5693d47896579e'
)


class send_sms():
    def __init__(self):
        self.sms = africastalking.SMS

    def send(self):

        # TODO: Send message
        recipients = ["+233551442796"]
        # Set your message
        message = "Hey AT Ninja!"
        # Set your shortCode or senderId
        sender = "23421"
        try:
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')
