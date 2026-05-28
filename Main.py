from fastapi import FastAPI, Request

app = FastAPI()

# simple database for testing purpose
data = [
    {"id": 1, "username": "user1"},
    {"id": 2, "username": "user2"},
    {"id": 3, "username": "user3"}
]

@app.get("/hi")
def read_root():
    return data


@app.get("/hello")
def hello():
    return {"message": "Hello with Hruthik"}


@app.post("/postlist")
async def create_user(request: Request):
    body = await request.json()
    data.append(body)
    return {"message": "User added", "data": body}

@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in data:
        if user["id"] == user_id:
            return user

    return {"message": "User not found"}
@app.put("/users/{user_id}")
async def update_user(user_id: int, request: Request):

    body = await request.json()

    for user in data:
        if user["id"] == user_id:
            user["id"] = body["id"]
            user["username"] = body["username"]
            return {"message": "User updated successfully", "user": user}

    return {"message": "User not found"}
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in data:
        if user["id"] == user_id:
            data.remove(user)
            return {"message": "User deleted successfully", "deleted_user": user}

    return {"message": "User not found"}