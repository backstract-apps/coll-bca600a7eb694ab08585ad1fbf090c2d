from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Profile(BaseModel):
    id: int
    name: str
    address: str
    mobile: str
    password: str
    email: str
    amount: int
    test: str
    test1: datetime.time
    saffds: datetime.time
    gdfgdf: datetime.time


class ReadProfile(BaseModel):
    id: int
    name: str
    address: str
    mobile: str
    password: str
    email: str
    amount: int
    test: str
    test1: datetime.time
    saffds: datetime.time
    gdfgdf: datetime.time
    class Config:
        from_attributes = True


class Records(BaseModel):
    id: int
    username: str
    address: str
    pincode: str
    user_amount: int


class ReadRecords(BaseModel):
    id: int
    username: str
    address: str
    pincode: str
    user_amount: int
    class Config:
        from_attributes = True


class Class(BaseModel):
    id: int
    subject: str


class ReadClass(BaseModel):
    id: int
    subject: str
    class Config:
        from_attributes = True


class Test123(BaseModel):
    id: int
    test123: str
    test1234: int


class ReadTest123(BaseModel):
    id: int
    test123: str
    test1234: int
    class Config:
        from_attributes = True


class Test(BaseModel):
    id: int
    testqw23: str


class ReadTest(BaseModel):
    id: int
    testqw23: str
    class Config:
        from_attributes = True


class Students(BaseModel):
    id: int
    name: str
    age: str


class ReadStudents(BaseModel):
    id: int
    name: str
    age: str
    class Config:
        from_attributes = True


class Trujghyr(BaseModel):
    id: int
    fsg: str


class ReadTrujghyr(BaseModel):
    id: int
    fsg: str
    class Config:
        from_attributes = True


