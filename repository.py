from sample_users import USERS


class UserRepository:

    def find(

        self,

        username

    ):

        for user in USERS:

            if user.username == username:

                return user

        return None
