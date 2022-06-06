from typing import Dict, Optional, Any

# FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

# Starlette
from starlette.responses import RedirectResponse

# Models
from app.models.person import Person, PersonOut

app: FastAPI = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs/")

@app.post("/person/new", response_model=PersonOut)
def create_person(person: Person = Body(...)):
    return person

@app.get("/person/detail")
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


@app.get("/person/detail/{person_id}")
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

@app.put("/person/{person_id}")
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
