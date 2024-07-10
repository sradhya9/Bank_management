from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Bank(BaseModel):
    accno: int
    accname: str
    balance: float = 0.0

class Account(BaseModel):
    name: str
    accounts: dict = {}

class User(BaseModel):
    username: str
    password: str

users = {'Niranj':'1703','Sradhya':'1803','test':'0','0':'0'}  # Dictionary to store username-password pairs

@app.post("/sign_up")
async def sign_up(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already exists. Please choose a different one.")
    users[user.username] = user.password
    return {"message": "Sign up successful!"}

@app.post("/log_in")
async def log_in(user: User):
    if user.username in users and users[user.username] == user.password:
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password.")

@app.post("/create_account")
async def create_account(acc: Bank):
    if acc.accno in account.accounts:
        raise HTTPException(status_code=400, detail="Account already exists.")
    account.accounts[acc.accno] = acc
    return {"message": "Account created successfully"}

@app.post("/deposit")
async def deposit(accno: int, amount: float):
    if accno not in account.accounts:
        raise HTTPException(status_code=404, detail="Account not found.")
    account.accounts[accno].balance += amount
    return {"message": f"{amount} succesfully credited to the account."}

@app.post("/withdraw")
async def withdraw(accno: int, amount: float):
    if accno not in account.accounts:
        raise HTTPException(status_code=404, detail="Account not found.")
    if account.accounts[accno].balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance.")
    b_fees = account.accounts[accno].balance*0.025
    account.accounts[accno].balance -= (amount + b_fees)
    return {"message": f"{amount} withdrawn from account."}

@app.get("/check_balance/{accno}")
async def check_balance(accno: int):
    if accno not in account.accounts:
        raise HTTPException(status_code=404, detail="Account not found.")
    return {"balance": account.accounts[accno].balance}

account = Account(name="Bank")