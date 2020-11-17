from fastapi import FastAPI

import uvicorn


app = FastAPI()


@app.get("/")
async def read_root():
    return {"hello": 'World'}


@app.get("/course/{course_id}")
async def my_course(course_id: int):
    return {"course_id": course_id}


@app.get("/values/")
async def read_values(page: int = 0, limit: int = 0, skip: int = 1):
    user_data = [i for i in range(100)]
    return user_data[page*5:limit*5:skip]

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
