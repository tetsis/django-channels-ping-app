# Django Channels Ping App
This app is web application to measure delay time by WebSocket.

# Pages
This app has two pages.

## Private
This page displays only delay time of single client.
If multiple clients access this page, they can see only themselves delay time.

## Public
This page displays delay times of all clients who access this page.

# Measurement method of delay time
This app uses WebSocket for measurement of delay time.

```
Clent                    Server
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

# Run
```
pip install -r requirements.txt
cd pingapp
python manage.py migrate
python manage.py runserver
```