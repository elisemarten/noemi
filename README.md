# JWT Auth Demo

A simple console application demonstrating JSON Web Token authentication.

The project authenticates users from an in-memory repository, creates JWT tokens and validates them.

---

## Workflow

```
Login
   │
   ▼
Password Check
   │
   ▼
JWT Token
   │
   ▼
Validation
```

---

## Example

```
Login successful

Generated token:

eyJhbGciOiJIUzI1Ni...

Token valid

User: admin
```

---

## Modules

- auth.py — authentication flow
- jwt_service.py — JWT generation
- repository.py — user repository
- password.py — password verification
- token_info.py — decoded token
- sample_users.py — demo users

Run

```
python app.py
```
