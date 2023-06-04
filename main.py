from fastapi import FastAPI, Header, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from routers import users, login, upload
from pathlib import Path

desc = """
simple-user-db-API
## Users

You will be able to 
* **Create User**
* **Get all Users**
* **Delete User**
* **Update User**
"""


def get_active_branch_name():
    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as f:
        content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]


git_branch = get_active_branch_name()
app = FastAPI(
    title=f"user-db-API-{git_branch}",
    description=desc,
    version="0.0.1",
    contact={"name": "Ammar-Azman", "url": "https://github.com/Ammar-Azman"},
)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(upload.router)


# override error handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


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
