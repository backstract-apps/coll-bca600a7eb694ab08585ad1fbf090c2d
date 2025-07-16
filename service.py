from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
from pathlib import Path


async def get_profile(db: Session):

    query = db.query(models.Profile)

    profile_all = query.all()
    profile_all = (
        [new_data.to_dict() for new_data in profile_all] if profile_all else profile_all
    )
    res = {
        "profile_all": profile_all,
    }
    return res


async def get_profile_id(db: Session, id: int):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))

    profile_one = query.first()

    profile_one = (
        (
            profile_one.to_dict()
            if hasattr(profile_one, "to_dict")
            else vars(profile_one)
        )
        if profile_one
        else profile_one
    )

    res = {
        "profile_one": profile_one,
    }
    return res


async def post_profile(
    db: Session,
    id: int,
    name: str,
    address: str,
    mobile: str,
    password: str,
    email: str,
    amount: int,
    test: str,
    test1: str,
    saffds: str,
    gdfgdf: str,
):

    record_to_be_added = {
        "id": id,
        "name": name,
        "test": test,
        "email": email,
        "test1": test1,
        "amount": amount,
        "gdfgdf": gdfgdf,
        "mobile": mobile,
        "saffds": saffds,
        "address": address,
        "password": password,
    }
    new_profile = models.Profile(**record_to_be_added)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    profile_inserted_record = new_profile.to_dict()

    res = {
        "profile_inserted_record": profile_inserted_record,
    }
    return res


async def put_profile_id(
    db: Session,
    id: int,
    name: str,
    address: str,
    mobile: str,
    password: str,
    email: str,
    amount: int,
    test: str,
    test1: str,
    saffds: str,
    gdfgdf: str,
):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))
    profile_edited_record = query.first()

    if profile_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "test": test,
            "email": email,
            "test1": test1,
            "amount": amount,
            "gdfgdf": gdfgdf,
            "mobile": mobile,
            "saffds": saffds,
            "address": address,
            "password": password,
        }.items():
            setattr(profile_edited_record, key, value)

        db.commit()
        db.refresh(profile_edited_record)

        profile_edited_record = (
            profile_edited_record.to_dict()
            if hasattr(profile_edited_record, "to_dict")
            else vars(profile_edited_record)
        )
    res = {
        "profile_edited_record": profile_edited_record,
    }
    return res


async def delete_profile_id(db: Session, id: int):

    query = db.query(models.Profile)
    query = query.filter(and_(models.Profile.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        profile_deleted = record_to_delete.to_dict()
    else:
        profile_deleted = record_to_delete
    res = {
        "profile_deleted": profile_deleted,
    }
    return res


async def get_records(db: Session):

    query = db.query(models.Records)

    records_all = query.all()
    records_all = (
        [new_data.to_dict() for new_data in records_all] if records_all else records_all
    )
    res = {
        "records_all": records_all,
    }
    return res


async def get_records_id(db: Session, id: int):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))

    records_one = query.first()

    records_one = (
        (
            records_one.to_dict()
            if hasattr(records_one, "to_dict")
            else vars(records_one)
        )
        if records_one
        else records_one
    )

    res = {
        "records_one": records_one,
    }
    return res


async def post_records(
    db: Session, id: int, username: str, address: str, pincode: str, user_amount: int
):

    record_to_be_added = {
        "id": id,
        "address": address,
        "pincode": pincode,
        "username": username,
        "user_amount": user_amount,
    }
    new_records = models.Records(**record_to_be_added)
    db.add(new_records)
    db.commit()
    db.refresh(new_records)
    records_inserted_record = new_records.to_dict()

    res = {
        "records_inserted_record": records_inserted_record,
    }
    return res


async def put_records_id(
    db: Session, id: int, username: str, address: str, pincode: str, user_amount: int
):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))
    records_edited_record = query.first()

    if records_edited_record:
        for key, value in {
            "id": id,
            "address": address,
            "pincode": pincode,
            "username": username,
            "user_amount": user_amount,
        }.items():
            setattr(records_edited_record, key, value)

        db.commit()
        db.refresh(records_edited_record)

        records_edited_record = (
            records_edited_record.to_dict()
            if hasattr(records_edited_record, "to_dict")
            else vars(records_edited_record)
        )
    res = {
        "records_edited_record": records_edited_record,
    }
    return res


async def delete_records_id(db: Session, id: int):

    query = db.query(models.Records)
    query = query.filter(and_(models.Records.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        records_deleted = record_to_delete.to_dict()
    else:
        records_deleted = record_to_delete
    res = {
        "records_deleted": records_deleted,
    }
    return res


async def get_class(db: Session):

    query = db.query(models.Class)

    class_all = query.all()
    class_all = (
        [new_data.to_dict() for new_data in class_all] if class_all else class_all
    )
    res = {
        "class_all": class_all,
    }
    return res


async def get_class_id(db: Session, id: int):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))

    class_one = query.first()

    class_one = (
        (class_one.to_dict() if hasattr(class_one, "to_dict") else vars(class_one))
        if class_one
        else class_one
    )

    res = {
        "class_one": class_one,
    }
    return res


async def post_class(db: Session, id: int, subject: str):

    record_to_be_added = {"id": id, "subject": subject}
    new_class = models.Class(**record_to_be_added)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    class_inserted_record = new_class.to_dict()

    res = {
        "class_inserted_record": class_inserted_record,
    }
    return res


async def put_class_id(db: Session, id: int, subject: str):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))
    class_edited_record = query.first()

    if class_edited_record:
        for key, value in {"id": id, "subject": subject}.items():
            setattr(class_edited_record, key, value)

        db.commit()
        db.refresh(class_edited_record)

        class_edited_record = (
            class_edited_record.to_dict()
            if hasattr(class_edited_record, "to_dict")
            else vars(class_edited_record)
        )
    res = {
        "class_edited_record": class_edited_record,
    }
    return res


async def delete_class_id(db: Session, id: int):

    query = db.query(models.Class)
    query = query.filter(and_(models.Class.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        class_deleted = record_to_delete.to_dict()
    else:
        class_deleted = record_to_delete
    res = {
        "class_deleted": class_deleted,
    }
    return res


async def get_test123(db: Session):

    query = db.query(models.Test123)

    test123_all = query.all()
    test123_all = (
        [new_data.to_dict() for new_data in test123_all] if test123_all else test123_all
    )
    res = {
        "test123_all": test123_all,
    }
    return res


async def get_test123_id(db: Session, id: int):

    query = db.query(models.Test123)
    query = query.filter(and_(models.Test123.id == id))

    test123_one = query.first()

    test123_one = (
        (
            test123_one.to_dict()
            if hasattr(test123_one, "to_dict")
            else vars(test123_one)
        )
        if test123_one
        else test123_one
    )

    res = {
        "test123_one": test123_one,
    }
    return res


async def post_test123(db: Session, id: int, test123: str, test1234: int):

    record_to_be_added = {"id": id, "test123": test123, "test1234": test1234}
    new_test123 = models.Test123(**record_to_be_added)
    db.add(new_test123)
    db.commit()
    db.refresh(new_test123)
    test123_inserted_record = new_test123.to_dict()

    res = {
        "test123_inserted_record": test123_inserted_record,
    }
    return res


async def put_test123_id(db: Session, id: int, test123: str, test1234: int):

    query = db.query(models.Test123)
    query = query.filter(and_(models.Test123.id == id))
    test123_edited_record = query.first()

    if test123_edited_record:
        for key, value in {"id": id, "test123": test123, "test1234": test1234}.items():
            setattr(test123_edited_record, key, value)

        db.commit()
        db.refresh(test123_edited_record)

        test123_edited_record = (
            test123_edited_record.to_dict()
            if hasattr(test123_edited_record, "to_dict")
            else vars(test123_edited_record)
        )
    res = {
        "test123_edited_record": test123_edited_record,
    }
    return res


async def delete_test123_id(db: Session, id: int):

    query = db.query(models.Test123)
    query = query.filter(and_(models.Test123.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test123_deleted = record_to_delete.to_dict()
    else:
        test123_deleted = record_to_delete
    res = {
        "test123_deleted": test123_deleted,
    }
    return res


async def get_test(db: Session):

    query = db.query(models.Test)

    test_all = query.all()
    test_all = [new_data.to_dict() for new_data in test_all] if test_all else test_all
    res = {
        "test_all": test_all,
    }
    return res


async def get_test_id(db: Session, id: int):

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))

    test_one = query.first()

    test_one = (
        (test_one.to_dict() if hasattr(test_one, "to_dict") else vars(test_one))
        if test_one
        else test_one
    )

    res = {
        "test_one": test_one,
    }
    return res


async def post_test(db: Session, id: int, testqw23: str):

    record_to_be_added = {"id": id, "testqw23": testqw23}
    new_test = models.Test(**record_to_be_added)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    test_inserted_record = new_test.to_dict()

    res = {
        "test_inserted_record": test_inserted_record,
    }
    return res


async def put_test_id(db: Session, id: int, testqw23: str):

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))
    test_edited_record = query.first()

    if test_edited_record:
        for key, value in {"id": id, "testqw23": testqw23}.items():
            setattr(test_edited_record, key, value)

        db.commit()
        db.refresh(test_edited_record)

        test_edited_record = (
            test_edited_record.to_dict()
            if hasattr(test_edited_record, "to_dict")
            else vars(test_edited_record)
        )
    res = {
        "test_edited_record": test_edited_record,
    }
    return res


async def delete_test_id(db: Session, id: int):

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test_deleted = record_to_delete.to_dict()
    else:
        test_deleted = record_to_delete
    res = {
        "test_deleted": test_deleted,
    }
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def post_students(db: Session, id: int, name: str, age: str):

    record_to_be_added = {"id": id, "age": age, "name": name}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        "students_inserted_record": students_inserted_record,
    }
    return res


async def put_students_id(db: Session, id: int, name: str, age: str):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {"id": id, "age": age, "name": name}.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_id(db: Session, id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_trujghyr(db: Session):

    query = db.query(models.Trujghyr)

    trujghyr_all = query.all()
    trujghyr_all = (
        [new_data.to_dict() for new_data in trujghyr_all]
        if trujghyr_all
        else trujghyr_all
    )
    res = {
        "trujghyr_all": trujghyr_all,
    }
    return res


async def get_trujghyr_id(db: Session, id: int):

    query = db.query(models.Trujghyr)
    query = query.filter(and_(models.Trujghyr.id == id))

    trujghyr_one = query.first()

    trujghyr_one = (
        (
            trujghyr_one.to_dict()
            if hasattr(trujghyr_one, "to_dict")
            else vars(trujghyr_one)
        )
        if trujghyr_one
        else trujghyr_one
    )

    res = {
        "trujghyr_one": trujghyr_one,
    }
    return res


async def post_trujghyr(db: Session, id: int, fsg: str):

    record_to_be_added = {"id": id, "fsg": fsg}
    new_trujghyr = models.Trujghyr(**record_to_be_added)
    db.add(new_trujghyr)
    db.commit()
    db.refresh(new_trujghyr)
    trujghyr_inserted_record = new_trujghyr.to_dict()

    res = {
        "trujghyr_inserted_record": trujghyr_inserted_record,
    }
    return res


async def put_trujghyr_id(db: Session, id: int, fsg: str):

    query = db.query(models.Trujghyr)
    query = query.filter(and_(models.Trujghyr.id == id))
    trujghyr_edited_record = query.first()

    if trujghyr_edited_record:
        for key, value in {"id": id, "fsg": fsg}.items():
            setattr(trujghyr_edited_record, key, value)

        db.commit()
        db.refresh(trujghyr_edited_record)

        trujghyr_edited_record = (
            trujghyr_edited_record.to_dict()
            if hasattr(trujghyr_edited_record, "to_dict")
            else vars(trujghyr_edited_record)
        )
    res = {
        "trujghyr_edited_record": trujghyr_edited_record,
    }
    return res


async def delete_trujghyr_id(db: Session, id: int):

    query = db.query(models.Trujghyr)
    query = query.filter(and_(models.Trujghyr.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        trujghyr_deleted = record_to_delete.to_dict()
    else:
        trujghyr_deleted = record_to_delete
    res = {
        "trujghyr_deleted": trujghyr_deleted,
    }
    return res
