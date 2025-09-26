def show_messages(messages):
    '''show the messages saved in a list'''
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    '''take messages from messages and send to sent_messages list.'''
    print("These messages are ready to print\n")
    print(messages)
    print("\nThese messages are already sent\n")
    print(sent_messages)

    while messages:
        current_message = messages.pop(0)
        print(f"\nYour message '{current_message}' is sent.")
        sent_messages.append(current_message)

    print("\nThese messages are more to print\n")
    print(messages)
    print("\nThese messages are sent\n")
    print(sent_messages)

sent = []
msgs = ['Hi boy', 'Hell yeah', 'Turn around']
show_messages(msgs)

send_messages(msgs,sent)
