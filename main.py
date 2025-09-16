from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/nombre/David_Cano")
async def DavidCano(name: str):
    return {"message": f"Soy David Cano :D"}

@app.get("/nombre/Duvan_Guerrero")
async def DuvanGuerrero(name: str):
    return { "message": "hola soy Duvan ;)"}

@app.get("/nombre/Karen_Cordoba")
async def KarenC(name: str):
    return {"message": f"Soy Karen Cordoba"}



@app.get("/nombre/Juan_Vega")
async def juanVega():
        return {"message": f"Hola soy Juan Vega :p"}

@app.get("/nombre/Felipe_Garzon")
async def FelipeGarzon(name: str):
    return{"message": "Soy Felipe Garzon"}

@app.get("/nombre/Nicolas_Lozano")
async def Nicolaslozano (name: str):
    return {"message": "Soy Nicolas"}

@app.get("/nombre/Rafael_Cordero")
async def get_nombre(name: str):
    return{"message": f"Buenos dias, soy {name}"}


app.get("/nombre/Valentina_Ovalle")
async def ValentinaOvalle(name: str):
    return{"message": f"HOLA!!, soy Valentina Ovalle, dispuesta a aprender!!"}



@app.get("/pablo_rincon")
async def nombre(name:str):
    return {"nombre": name }


@app.get("/nombre/Christian_Solano")
async def Christian(name:str):
    return{"mensaje":"Hola profe soy Christian Solano"}

    

@app.get("/nombre/Daniel_Segura")
async def danielSegura():
    return {"mensaje": f"Hola, Soy Daniel Segura"}


@app.get("/nombre/Daniel_Vaquiro")
async def DanielVaquiro(name: str):
    return {"mensage":"Hola, soy Daniel Vaquiro"}


@app.get("/nombre/Ivan_Vanegas")
async def ivanVanegas():
    return{}