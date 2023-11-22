#!/usr/bin/env python3
"""
trials to see if inbox_manager gives expected output
"""

from models import storage
from models.engine.inbox_manager import Message_manager, Inbox_manager

im = Inbox_manager()
im.create_inbox('9af311e1-eafe-4549-a4d3-117408627b16')

mm = Message_manager()

#create_message(<sender_id>, <reciever_id>, <inbox_id>, <content>)
mm.create_message('1c24003b-64d6-485b-9a59-bafc81db081b', '9af311e1-eafe-4549-a4d3-117408627b16', 'a1ab2a2f-cb4c-45f8-8f8c-81bc541279d5', 'hello world')
mm.read_message('9af311e1-eafe-4549-a4d3-117408627b16', )
