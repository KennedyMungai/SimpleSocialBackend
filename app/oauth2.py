from jose import JWTError, jwt
from datetime import datetime, timedelta


# To generate a secret key use 'openssl rand -hex 32'
SECRET_KEY = "14c497b2746482189dc1b0c1859aa3e4ff9023ffa9c6ae07c2d620693bb5f15f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
