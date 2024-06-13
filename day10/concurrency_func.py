import asyncio
import time

async def sql_command1():
    await asyncio.sleep(2)
    print("Query executed 1")
    return {"col1": 1, "col2": 2}


async def sql_command2():
    await asyncio.sleep(3)
    print("Query executed 2")
    return {"col1": 1, "col2": 2}

async def sql_command3():
    await asyncio.sleep(3)
    print("Query executed 3")
    return {"col1": 1, "col2": 2}


async def main():
    
 start_time = time.time()

 sql1 = asyncio.create_task(sql_command1())
 sql2 = asyncio.create_task(sql_command2())
 sql3 = asyncio.create_task(sql_command3())

 res1 = await sql1
 res2 = await sql2
 res3 = await sql3

 end_time = time.time()
 exec_time = end_time - start_time
 print(f"re1 {res1}")
 print(f"re2 {res2}")
 print(f"re3 {res3}")
 print(f"total time {exec_time:.2f}")

if __name__ == "__main__":
     asyncio.run(main())