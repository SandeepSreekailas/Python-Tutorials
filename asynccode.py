import asyncio

# async def Home():
#     print("welcome home")
#     await asyncio.sleep(3)
#     print("time for work homeee")

# async def getout():
#     print("Bye Bye Homee")
#     await asyncio.sleep(5)
#     print("get out bitches")


# async def main():
#     await asyncio.gather(Home(),getout())
    


# asyncio.run(main())


# Sequential vs Concurrent Execution
import time

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

#Sequential Execution
# async def main():
#     start=time.time()

#     await task1()
#     await task2()   

#     print("total time", time.time()-start)

# asyncio.run(main())

#Concurrent Execution
# async def main():
#     start=time.time()

#     await asyncio.gather(task1(), task2())

#     print("total time", time.time()-start)

# asyncio.run(main())