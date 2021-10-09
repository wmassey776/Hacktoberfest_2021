""" Simple API made with FastAPI to return the local time"""

import fastapi
import time

app = fastapi.FastAPI(title="Time API")

# Get time of the server
@app.get("/time")
async def read_time() -> str:
    return time.strftime("%H:%M:%S")


@app.get("/time/utc/{timezone}")
async def read_time_timezone(timezone: int) -> str:
    current_time = time.strftime("%H:%M:%S", time.gmtime()).split(":")
    current_time[0] = str((int(current_time[0]) + timezone) % 24)

    return ":".join(current_time)

