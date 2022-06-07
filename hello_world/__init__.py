from typing import Optional

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import (
    Body,
    Path,
    Query,
    Form,
    Header,
    Cookie,
    File,
    UploadFile
)

# Starlette
from starlette.responses import RedirectResponse

# Pydantic
from pydantic import SecretStr
from pydantic import EmailStr

# Models
from hello_world.models.person import Person, PersonOut
from hello_world.models.login import LoginOut

app: FastAPI = FastAPI()

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"]
)
def root():
    return RedirectResponse(url="/docs/")

@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create Person in the app"
)
def create_person(person: Person = Body(...)):
    """
    Create Person

    This path operation creates a person in the app and
    save the information in the database.

    Parameters:
    - Request Body Parameter:
        - **person: Person** -> A person model with first name, last name, age, hair color and martal status

    Returns a person model with first name, last name, age, hair color and martal status
    """
    return person

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    deprecated=True
)
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        regex=r"\S",
        example="Rocio"
    ),
    age: int = Query(
        ...,
        ge = 18,
        example=59
    )
):
    return {name: age}


persons  = [1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title = "Person ID",
        description = "This is the Person ID. It's gt 0",
        example=123456
    )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exist!"
        )
    return { person_id: "It exists!"}

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Persons"]
)
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID.",
        example=123456
    ),
    person: Person = Body(...)
):
    result = person.dict()
    return result

# Forms

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Auth"]
)
def login(
    username: str = Form(...),
    password: SecretStr = Form(...)
):
    print(username, password)
    return LoginOut(username=username, message="Login Succesfuly!")

# Cookies and Headers parameters
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent

@app.post("/post-image")
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, 2)
    }
