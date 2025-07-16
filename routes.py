from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/profile/')
async def get_profile(db: Session = Depends(get_db)):
    try:
        return await service.get_profile(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profile/id')
async def get_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profile/')
async def post_profile(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], mobile: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], amount: int, test: Annotated[str, Query(max_length=100)], test1: str, saffds: str, gdfgdf: str, db: Session = Depends(get_db)):
    try:
        return await service.post_profile(db, id, name, address, mobile, password, email, amount, test, test1, saffds, gdfgdf)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/profile/id/')
async def put_profile_id(id: int, name: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], mobile: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], amount: int, test: Annotated[str, Query(max_length=100)], test1: str, saffds: str, gdfgdf: str, db: Session = Depends(get_db)):
    try:
        return await service.put_profile_id(db, id, name, address, mobile, password, email, amount, test, test1, saffds, gdfgdf)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/profile/id')
async def delete_profile_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_profile_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/')
async def get_records(db: Session = Depends(get_db)):
    try:
        return await service.get_records(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/records/id')
async def get_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/records/')
async def post_records(id: int, username: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], pincode: Annotated[str, Query(max_length=100)], user_amount: int, db: Session = Depends(get_db)):
    try:
        return await service.post_records(db, id, username, address, pincode, user_amount)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/records/id/')
async def put_records_id(id: int, username: Annotated[str, Query(max_length=100)], address: Annotated[str, Query(max_length=100)], pincode: Annotated[str, Query(max_length=100)], user_amount: int, db: Session = Depends(get_db)):
    try:
        return await service.put_records_id(db, id, username, address, pincode, user_amount)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/records/id')
async def delete_records_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_records_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/')
async def get_class(db: Session = Depends(get_db)):
    try:
        return await service.get_class(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/class/id')
async def get_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/class/')
async def post_class(id: int, subject: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_class(db, id, subject)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/class/id/')
async def put_class_id(id: int, subject: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_class_id(db, id, subject)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/class/id')
async def delete_class_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_class_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test123/')
async def get_test123(db: Session = Depends(get_db)):
    try:
        return await service.get_test123(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test123/id')
async def get_test123_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test123_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test123/')
async def post_test123(id: int, test123: Annotated[str, Query(max_length=100)], test1234: int, db: Session = Depends(get_db)):
    try:
        return await service.post_test123(db, id, test123, test1234)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test123/id/')
async def put_test123_id(id: int, test123: Annotated[str, Query(max_length=100)], test1234: int, db: Session = Depends(get_db)):
    try:
        return await service.put_test123_id(db, id, test123, test1234)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test123/id')
async def delete_test123_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_test123_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test/')
async def get_test(db: Session = Depends(get_db)):
    try:
        return await service.get_test(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test/id')
async def get_test_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test/')
async def post_test(id: int, testqw23: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_test(db, id, testqw23)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test/id/')
async def put_test_id(id: int, testqw23: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_test_id(db, id, testqw23)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test/id')
async def delete_test_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_test_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/id')
async def get_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(id: int, name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, id, name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/id/')
async def put_students_id(id: int, name: Annotated[str, Query(max_length=100)], age: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_students_id(db, id, name, age)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/id')
async def delete_students_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/trujghyr/')
async def get_trujghyr(db: Session = Depends(get_db)):
    try:
        return await service.get_trujghyr(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/trujghyr/id')
async def get_trujghyr_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_trujghyr_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/trujghyr/')
async def post_trujghyr(id: int, fsg: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_trujghyr(db, id, fsg)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/trujghyr/id/')
async def put_trujghyr_id(id: int, fsg: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_trujghyr_id(db, id, fsg)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/trujghyr/id')
async def delete_trujghyr_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_trujghyr_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

