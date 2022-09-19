from fastapi import FastAPI

from mod.mod import simple_func

app = FastAPI()

@app.get("/")
def root():
    simple_func()
    return {"response": "finished"}
    



