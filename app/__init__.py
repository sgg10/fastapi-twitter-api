from typing import Optional

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Path, Query

# Starlette
from starlette.responses import RedirectResponse

# Models
from app.models.person import Person, PersonOut

app: FastAPI = FastAPI()

@app.get(
    path="/",
    status_code=status.HTTP_200_OK
)
def root():
    return RedirectResponse(url="/docs/")

@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
)
def create_person(person: Person = Body(...)):
    return person

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
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


@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK
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
    return { person_id: "It exists!"}

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_204_NO_CONTENT
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
