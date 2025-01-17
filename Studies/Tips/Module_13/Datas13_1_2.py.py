import asyncio
import time


async def get_temp():                         # Температура
    print("Первое показание")
    await asyncio.sleep(2)
    print("25 C")


async def get_pres():                         # Давление
    print("Второе показание")
    await asyncio.sleep(3)
    print("101 kPa")


async def main():
    print("Cтaрт")
    task1=asyncio.create_task(get_temp())
    await task1
    task2=asyncio.create_task(get_pres())
    await task2
    print("Финиш")


start = time.time()                         # Время начала работы
asyncio.run(main())
finish = time.time()                        # Время конца работы

print(f"Working time = {round(finish - start, 2)} seconds")