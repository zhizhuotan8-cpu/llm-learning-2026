"""
Conversation 类需要实现：
add_message() 添加消息
delete_message() 删除消息
clear() 清空记录
history() 查看历史记录
"""

class Conversation:

    def __init__(self,titie='new conversation'):
        #会话的标题
        self.titie = titie
        #用于保存历史信息
        self.messages = []

    """
    add_message() 添加消息
    rale:user 用户    assistant AI助手
    """
    def add_message(self,rale,content):
        message={
            'rale' : rale,
            'message' : content
        }
        self.messages.append(message)
        print('添加成功')

    def delete_message(self,index):
        if 0 <= index < len(self.messages) :
            cmp = self.messages.pop(index)
            print("删除消息",cmp)
        else:
            print("消息不存在")


    def clear(self):
        self.messages.clear()
        print("删除成功")

    def history(self):
        for i in self.messages:
            print(i,end="\n")


p1 = Conversation()
p1.add_message('user','你好')
p1.add_message('assistant','Hello World')

p1.history()

p1.delete_message(1)
p1.history()
p1.clear()

p1.history()