
from Conversation import Conversations
from Chat_history import Chat_history_manage
conversation_1 = Conversations('第一个')
conversation_2 = Conversations('第二个')
conversation_3 = Conversations('第三个')

conversation_1.addmessage('user','hello world!')
conversation_2.addmessage('user','hello world!')
conversation_3.addmessage('user','hello world!')

for i in conversation_2.history():
    print(i,end='\n')

manage = Chat_history_manage()
manage.save(conversation_1)
manage.load(0)
manage.save(conversation_2)
manage.list_conversations()
manage.save(conversation_3)
manage.delete(0)
manage.list_conversations()
