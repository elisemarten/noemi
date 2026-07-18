import jwt
import time

from config import (
    SECRET_KEY,
    ALGORITHM,
    TOKEN_EXPIRE
)


class JwtService:

    def create(

        self,

        username

    ):

        payload = {

            "sub": username,

            "exp": int(

                time.time()

            ) + TOKEN_EXPIRE

        }

        return jwt.encode(

            payload,

            SECRET_KEY,

            algorithm=ALGORITHM

        )

    def verify(

        self,

        token

    ):

        return jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )
