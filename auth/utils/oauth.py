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




