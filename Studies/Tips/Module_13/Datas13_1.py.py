import time
import asyncio
from asyncio import create_task
from venv import create


async def notification():
    print("до доставки осталось 10 минут")
    time.sleep(10)


async def main():
    task = asyncio.create_task(notification())
    print("Собираемся в поездку")
    print("Eдим")


asyncio.run(main())