from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from routers import users, login

desc = """
simple-user-db-API
## Users

You will be able to 
* **Create User**
* **Get all Users**
* **Delete User**
* **Update User**
"""
app = FastAPI(
    title="user-db-API",
    description=desc,
    version="0.0.1",
    contact={"name": "Ammar-Azman", "url": "https://github.com/Ammar-Azman"},
)
app.include_router(users.router)
app.include_router(login.router)


@app.get("/")
def root():
    return {"Health": "Good!", "CI/CD": "Succed!"}


@app.get("/header")
def read_header(user_agent=Header(None)):
    """
    NOTE: Not understand about
    why it supposed to be underscore
    instead of hypen
    """
    print(user_agent)
    content = {"message": "hello-world!"}
    return {"content": content, "User-Agent": user_agent}
