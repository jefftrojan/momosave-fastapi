#!/usr/bin/python3

from fastapi import FastAPI
from typing import List
from uuid import uuid4
from models import Role, User

app = FastAPI()

# Initialize Db
db: List[User] = [
    User(
    id=uuid4(),
    first_name="jeff",
    last_name="dauda",
    roles=[Role.user],
    ),
    User(
    id=uuid4(),
    first_name="jefftrojan",
    last_name="dauda",
    roles=[Role.user],
    ),
    User(
    id=uuid4(),
    first_name="trojan",
    last_name="dauda",
    roles=[Role.user],
    ),
]