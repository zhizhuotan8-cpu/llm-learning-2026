"""
历史会话管理
save_data()
load_date
save()
load()
delete()
list()
"""
from pathlib import Path
import json
from Conversation import Conversations
class Chat_history_manage:

    def __init__(self,file_path = 'date/conversation.json'):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(exist_ok=True)

        if not self.file_path.exists():
            self.file_path.touch()
            self.save_data([])

    def save_data(self,data):
        with open(
            self.file_path,
            'w',
            encoding='UTF-8'
        ) as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )

    def load_data(self):

        """
        加载JSON文件
        """

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)

    def save(self, conversation):

        """
        保存一次聊天
        """

        data = self.load_data()
        if data is None:
            data = []

        data.append(
            conversation.to_dict()
        )

        self.save_data(data)

        print("保存成功")

    def load(self,index):
        data = self.load_data()
        if index >= len(data):
            print('不存在')
            return
        return Conversations.from_dict(data[index])

    def delete(self,index):
        data = self.load_data()
        if index >= len(data):
            print('不存在')
            return
        tmp = data.pop(index)
        print("删除数据：",tmp['title'])

    def list_conversations(self):
        data = list(self.load_data())
        for i,item in enumerate(data):
            print(
                i,
                item['title']
            )





