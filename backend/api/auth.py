@router.post("/register")
def register(data: AuthRequest):
    for u in users:
        if u["email"] == data.email:
            raise HTTPException(status_code=400, detail="User exists")

    users.append({
        "email": data.email,
        "password": pwd.hash(data.password)
    })
    return {"msg": "Registered"}

@router.post("/login")
def login(data: AuthRequest):
    for u in users:
        if u["email"] == data.email and pwd.verify(data.password, u["password"]):
            return {"token": create_token(data.email)}

    raise HTTPException(status_code=401, detail="Invalid credentials")
