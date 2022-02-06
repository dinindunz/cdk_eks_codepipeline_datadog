from fastapi import FastAPI

app = FastAPI(title="EKS App Alpha Docker")

@app.get("/")
def get_message():
    return {"message": "EKS App Alpha Demo!"}