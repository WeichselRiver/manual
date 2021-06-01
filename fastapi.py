# pip install fastapi, uvicorn

# start:
# uvicorn app:app --reload

# docs:
# localhost:8000/docs

# minimal ---------------------------

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_hdl():
  return {"message" : "Hallo"}


# templates -------------------------

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_hdl(request : Request):
    """
    Show entry page UploadHDL.html
    """
    return templates.TemplateResponse("UploadHDL.html", {"request": request})
  
  
# upload files (Excel) --------------------------------------
# pip install python-multipart
  
 ...

@app.post("/")
def create_upload_file(file: bytes = File(...)):
      
    snapshot_file = BytesIO(file).read() # read file and convert to pandas dataframe
    workbook = pd.ExcelFile(snapshot_file)
    
# upload files (text) --------------------------------------
# pip install python-multipart



...

from fastapi import FastAPI, UploadFile, File
import json

...

@app.post("/upload_snapshot")
async def create_upload_file(file: UploadFile = File(...)):
    txt = await file.read()
    MVP(json.loads(txt))
    return {"filename": file.filename}


