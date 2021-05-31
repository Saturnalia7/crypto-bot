import json
import os
import logging
import sys 

from twisted.python import log
from twisted.interent import reactor

from autobahn import WebSocketServerFactory
from autobahn import WebSocketServerProtocol

API_KEY = os.environ.get('PUBLIC_KEY') 
API_KEY = os.environ.get('PRIVATE_KEY') 
PUBLIC_CHANNEL = 'ws.kraken.com'
PRIVATE_CHANNEL = 'ws-auth.kraken.com'

# autobahn.websocket.interfaces.IWebSocketChannel.onConnect()
# autobahn.websocket.interfaces.IWebSocketChannel.onConnecting()
# autobahn.websocket.interfaces.IWebSocketChannel.onOpen()
# autobahn.websocket.interfaces.IWebSocketChannel.onMessage()
# autobahn.websocket.interfaces.IWebSocketChannel.onClose()

'''The token should be used within 15 minutes of creation. 
The token does not expire once a connection to a WebSockets API 
private message (openOrders or ownTrades) is maintained.'''
AUTH_CHANNEL = 'https://api.kraken.com/0/private/GetWebSocketsToken'

obj = json.loads(payload.decode('utf8'))
payload = json.dumps(obj, ensure_ascii=False).encode('utf8')

key = 657593

class KrakenClient(WebSocketServerProtocol):
    def __init__():
        pass

    def onConnect(self, request):
        logging.info(f'Client connecting: {request.peer}')
    
    def onOpen(self):
        logging.info(f'Connection open')
        pass

    def onMessage(self):
        pass
    
    def onClose(self):
        pass


if __name__ == '__main__':
    factory = WebSocketServerFactory()
    factory.protocol = MyServerProtocol

    reactor.listenTCP(9000, factory)
    reactor.run()