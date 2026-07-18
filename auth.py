from repository import UserRepository

from password import PasswordVerifier

from jwt_service import JwtService


class AuthService:

    def login(

        self,

        username,

        password

    ):

        user = UserRepository().find(

            username

        )

        if not user:

            return None

        if not PasswordVerifier().check(

            password,

            user.password

        ):

            return None

        return JwtService().create(

            username

        )
