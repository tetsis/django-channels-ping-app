# Django Channels Ping App
This app is web application to measure delay time by WebSocket.

# Pages
This app has two pages.

## Private
This page displays only delay time of single client.
If multiple clients access this page, they can see only themselves delay time.

## Public
This page displays delay times of all clients who access this page.

# WebSocket protocols
## Measurement method of delay time
This app uses WebSocket for measurement of delay time.

```
Client                   Server
  |                        |
  |-- Connect WebSocket -->|
  |                        |
 (Ts)                      |
  |--------- Ping -------->|
  |<-------- Pong ---------|
 (Tr)                      |
  |                        |

Delay time = Tr - Ts
```

## Connection (public page)
```
Client A                 Server                  Client B
  |                        |                        |
  |-- Connect WebSocket -->|                        |
  |<- [Broadcast] Connect -|                        |
  |                        |                        |
  |                        |<-- Connect WebSocket --|
  |<- [Broadcast] Connect -|- [Broadcast] Connect ->|
  |                        |                        |
```

## Send delay time to server and receive delay times of all clients (public page)
```
Client                   Server
  |                        |
  |----- Delay time ------>|
  |                Record delay time
  |<--- Delay time list ---|
  |                        |
```

## Disconnection (public page)
```
Client A                  Server                  Client B
  |                         |                         |
  |                Detect disconnection               |
  |<-[Broadcast] Disconnect-|-[Broadcast] Disconnect->|
  |                         |                         |
```

# Test run
```
pip install -r requirements.txt
docker run -p 6379:6379 -d redis:5
cd pingapp
python manage.py migrate
python manage.py runserver
```
Access to [http://127.0.0.1:8000](http://127.0.0.1:8000)

# Run by docker compose
```
docker-compose build
docker-compose up -d
```
Access to [http://127.0.0.1:8000](http://127.0.0.1:8000)

# References
- [Tutorial of Django Channels](https://channels.readthedocs.io/en/stable/tutorial/index.html)
- [Deploying of Django Channels](https://channels.readthedocs.io/en/stable/deploying.html)
- [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)
    - [クィックスタート: Compose と Django](https://docs.docker.jp/compose/django.html)