import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):
    delay_times = {}

    async def connect(self):
        self.room_group_name = 'public_room'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        self.delay_times[self.channel_name] = {
            'name': self.channel_name,
            'delay_time': '-'
        }

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_connection',
                'channel_name': self.channel_name,
                'name': self.channel_name
            }
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        del self.delay_times[self.channel_name]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_disconnection',
                'channel_name': self.channel_name
            }
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']

        if command == 'ping':
            await self.send(text_data=json.dumps({
                'command': 'pong'
            }))
        elif command == 'delay_time':
            delay_time = text_data_json['delay_time']
            self.delay_times[self.channel_name]['delay_time'] = delay_time

            await self.send(text_data=json.dumps({
                'command': 'delay_times',
                'delay_times': self.delay_times
            }))
        elif command == 'change_name':
            name = text_data_json['name']
            self.delay_times[self.channel_name]['name'] = name

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'send_changing_name',
                    'channel_name': self.channel_name,
                    'name': name
                }
            )

    async def send_connection(self, event):
        channel_name = event['channel_name']
        name = event['name']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': 'connect',
            'channel_name': channel_name,
            'name': name
        }))

    async def send_changing_name(self, event):
        channel_name = event['channel_name']
        name = event['name']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': 'change_name',
            'channel_name': channel_name,
            'name': name
        }))

    async def send_disconnection(self, event):
        channel_name = event['channel_name']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': 'disconnect',
            'channel_name': channel_name
        }))
    