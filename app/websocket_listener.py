async def listen():
    uri = "wss://stream.binance.com:9443/ws/!miniTicker@arr"
    async with websockets.connect(uri) as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            for ticker in data:
                if ticker['s'] == "BTCUSDT":  # Adjust symbol as needed
                    price = float(ticker['c'])
                    await check_alerts_and_notify(price)

def start_price_tracking():
    asyncio.run(listen())
