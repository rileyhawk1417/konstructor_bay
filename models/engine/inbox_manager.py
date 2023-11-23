#!/usr/bin/env python3
"""
manage inboxes of users
"""
from models import storage
from models.inbox import Inbox, Message

class Inbox_manager:
    """
    inbox manager class
    """
    def __init__(self):
        pass
    
    @staticmethod   
    def create_inbox(user_id):
        """
        create inbox
        """
        inbox = Inbox()
        inbox.user_id = user_id
        storage.new(inbox)
        storage.save()
        return inbox

    @staticmethod
    def read_inbox(user_id):
        """
        read inbox
        """
        inboxes = storage.new_get(Inbox, user_id)
        print(inboxes)

    @staticmethod
    def delete_inbox(user_id):
        """
        delete inbox
        """
        inbox = storage.new_get(Inbox, user_id)
        if inbox is None:
            print ("inbox not found")
            return 'inbox not found'
        storage.delete(inbox)
        storage.save()
        return inbox
    
class Message_manager:
    """
    manage messanges
    """
    @staticmethod
    def create_message(sender_id, reciever_id, inbox_id, content):
        message = Message(sender_id=sender_id, receiver_id=reciever_id, inbox_id=inbox_id, content=content)
        storage.new(message)
        storage.save()
        return message
    @staticmethod
    def read_message(message_id):
        return storage.new_get(Message, message_id)

    def delete_messange(message_id):
        message = storage.new_get(Message, message_id)
        if message is None:
            print ("message not found")
            return 'message not found'
        storage.delete(message)
        storage.save()
        return message
    def update_messange(message_id, content):
        message = storage.new_get(Message, message_id)
        if message is None:
            print ("message not found")
            return 'message not found'
        message.content = content
        storage.save()
        return message

    