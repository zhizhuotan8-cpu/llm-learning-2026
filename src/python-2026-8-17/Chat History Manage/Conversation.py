"""
会话类：
addmanage()
history()
to_dict()
from_dict()
"""
class Conversations:

    def __init__(self,title = 'new title'):
        self.title = title

        self.messages = []

    def addmessage(self,rale,content):
        tmp = {
            'rale' : rale,
            'message' : content
        }

        self.messages.append(tmp)

    def history(self):
        return self.messages

    def to_dict(self):
        return {
            'title' : self.title,
            'messages' : self.messages
        }

    @classmethod
    def from_dict(cls,date):
        conversation = cls(date['title'])
        conversation.messages = date['messages']
        return  conversation

