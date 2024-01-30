from datetime import utcnow, timedelta
from decouple import config

def create_access_token(data:dict):
    """
    Take a dictionary of user details, encode it
    returns string
    """

    token_expiry_minutes = config("ACCESS_TOKEN_EXPIRE_MINUTES")
    algorithm = config("ALGORITHM")
    secret_key = config("SECRET_KEY")

    #extract the data
    to_encode = data.copy()

    #set the expiry date
    expire = utcnow() + timedelta(minutes=token_expiry_minutes)
    to_encode.update({"exp": expire})

    #encode the data
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str, credentials_exception, db: orm.Session):
    try:
        if not token:
            raise fastapi.HTTPException(
                    status_code = 401, detail="expired or invalid token")
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        #user = db.query(user_models.User).filter(user_models.User.id == id).first()

        #if user is None:
        #    raise fastapi.HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        #email = user.email

        if id is None:
            raise credentials_exception
        token_data = auth_schemas.TokenData(email=email, id=id)
    except JWTError:
        raise credentials_exception

    return token_data
