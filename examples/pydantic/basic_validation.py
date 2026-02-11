from fasthttp import FastHTTP
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    username: str


app = FastHTTP()


@app.get(
    url="https://jsonplaceholder.typicode.com/users/1",
    response_model=User
)
async def get_user(resp) -> User:
    return resp.json()


@app.get(
    url="https://jsonplaceholder.typicode.com/users",
    response_model=list[User]
)
async def get_all_users(resp) -> list[User]:
    return resp.json()

if __name__ == "__main__":
    app.run()
