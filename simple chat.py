users = {}

def register_user(username):
    users[username] = []

def send_message(send, receiver, message_text):
    message = {'send': send, 'receiver': receiver, 'message': message_text}
    users[send].append(message)
    users[receiver].append(message)


def view_messages(username):
    for message in users[username]:
        print(f"{message['send']} to {message['receiver']}: {message['message']}")

register_user("Mohamed")
register_user("Ali")
send_message("Mohamed", "Ali", "Hello, Ali!")
view_messages("Ali")
send_message("Ali", "Mohamed", "Hi, Ali!")
view_messages("Mohamed")
