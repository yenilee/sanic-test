import asyncio
import time

from sanic import Sanic, json
from sanic.response import text, HTTPResponse
from sanic.request import Request

from config import MyConfig

app = Sanic("MyHelloWorldApp", config=MyConfig())

@app.get("/")
async def hello_world(request):
    print(app.config.FOO)
    return text("Hello, world.")


@app.get("/test/<test_number>")
async def test(request, test_number):
    print(test_number)
    return json({"created": True, "test_numer": test_number}, status=200)

@app.get("/sync")
def sync_handler(request):
    time.sleep(10)
    return text("Sync Done.")

@app.get("/async")
async def async_handler(request: Request) -> HTTPResponse:
    await asyncio.sleep(10)
    return text("Async Done.")
