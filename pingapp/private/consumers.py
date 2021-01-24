import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']
        if command == 'ping':
            await self.send(text_data=json.dumps({
                'command': 'pong'
            }))