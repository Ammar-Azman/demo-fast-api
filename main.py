from fastapi import FastAPI
from routers import users

desc="""
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
    contact={
        "name":"Ammar-Azman", 
        "url":"https://github.com/Ammar-Azman"
    }, 
)
app.include_router(users.router)

@app.get("/")
def root():
    return {
        "Health":"Good!", 
        "CI/CD":"Succed!"
    }