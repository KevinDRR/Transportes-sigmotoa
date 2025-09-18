from fastapi import APIRouter

router = APIRouter()

@router.get("/nombre/David_Cano")
async def DavidCano(name: str):
    return {"message": f"Soy David Cano :D"}

@router.get("/nombre/Duvan_Guerrero")
async def DuvanGuerrero(name: str):
    return { "message": "hola soy Duvan ;)"}

@router.get("/nombre/Karen_Cordoba")
async def KarenC(name: str):
    return {"message": f"Soy Karen Cordoba"}



@router.get("/nombre/Juan_Vega")
async def juanVega():
    return {"message": f"Hola soy Juan Vega :p"}

@router.get("/nombre/Felipe_Garzon")
async def FelipeGarzon(name: str):
    return{"message": "Soy Felipe Garzon"}

@router.get("/nombre/Nicolas_Lozano")
async def Nicolaslozano (name: str):
    return {"message": "Soy Nicolas"}

@router.get("/nombre/Rafael_Cordero")
async def get_nombre(name: str):
    return{"message": f"Buenos dias, soy {name}"}


@router.get("/nombre/Valentina_Ovalle")
async def ValentinaOvalle(name: str):
    return{"message": f"HOLA!!, soy Valentina Ovalle, dispuesta a aprender!!"}



@router.get("/pablo_rincon")
async def nombre(name :str):
    return {"nombre": name }


@router.get("/nombre/Christian_Solano")
async def Christian(name :str):
    return{"mensaje" :"Hola profe soy Christian Solano"}



@router.get("/nombre/Daniel_Segura")
async def danielSegura():
    return {"mensaje": f"Hola, Soy Daniel Segura"}


@router.get("/nombre/Daniel_Vaquiro")
async def DanielVaquiro(name: str):
    return {"mensage" :"Hola, soy Daniel Vaquiro"}


@router.get("/nombre/Ivan_Vanegas")
async def ivanVanegas():
    return{}