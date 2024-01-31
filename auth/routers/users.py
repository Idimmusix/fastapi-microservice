from schemas.user_schemas import User, UserCreate
from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks
from fastapi.responses import Response
from services.user_service import user_create
# from core.dependencies import is_authenticated
from sqlalchemy.orm import Session
from db.database import get_db


app = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@app.post("/signup", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: UserCreate,
                      response: Response,
                      background_tasks: BackgroundTasks,
                db: Session = Depends(get_db),):
    new_user = await user_create(user, db)
    return new_user


@app.get("/me", response_model=User)
async def get_current_user():#user: User = Depends(is_authenticated)):
    """intro-->This endpoint allows you to retrieve details about the currently logged in user, to use this endpoint you need to make a get request to the  /users/me endpoint

    returnDesc-->On sucessful request, it returns:

        returnBody--> details of the currently logged in user
    """
    pass