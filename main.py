from fastapi import FastAPI


app=FastAPI()



@app.get("/")
def hello_world():

    return "Hola estudiantes de skills campus"