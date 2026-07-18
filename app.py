from auth import AuthService

from jwt_service import JwtService

from token_info import show

token = AuthService().login(

    "admin",

    "password123"

)

if token:

    print()

    print("Login successful")

    print()

    print("Generated token:\n")

    print(token)

    payload = JwtService().verify(

        token

    )

    show(payload)

else:

    print(

        "Authentication failed"

    )
