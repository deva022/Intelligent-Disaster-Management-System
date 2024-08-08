class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

class CommunicationChannel:
    def __init__(self):
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)
        print(f"Message from {message.sender} to {message.receiver}: {message.content}")

channel = CommunicationChannel()
message = Message('Dispatcher', 'Rescue Team 1', 'Proceed to location X')
channel.send_message(message)
