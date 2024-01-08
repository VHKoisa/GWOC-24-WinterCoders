import sqlite3
import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import Form, Request

class Students(BaseModel):
    fname : str
    lname : str
    state : str
    city :  str
    pin :  str
    mobile : str
    email : str

app = fastapi.FastAPI()
dbPath = 'fastapi_server/db/tarang.db'

templates = Jinja2Templates(directory="fastapi_server/admin") 

def get_db():
    db = sqlite3.connect(dbPath)
    yield db
    db.close()

# db = sqlite3.connect(dbPath)
@app.get('/admin', name='admin')
def admin_page(request: Request,db:  sqlite3.Connection = fastapi.Depends(get_db)):
    query = 'SELECT * FROM students'
    cur = db.cursor()
    cur.execute(query)
    students = cur.fetchall()
    print(students)
    columns = ['fname', 'lname', 'state', 'city', 'pin', 'mobile', 'email']
    return templates.TemplateResponse("admin.html", {"request": request, "students": students, 'columns':columns})

@app.post('/submit-form', name='submit')
def form_submit(fname:str = fastapi.Form(...), lname:str = Form(...), state:str = Form(...), city:str = Form(...), pin:str = Form(...), mobile:str = Form(...), email:str = Form(...), db:  sqlite3.Connection = fastapi.Depends(get_db)):
    # data = request.form()
    cur = db.cursor()
    
    
    
    cur.execute('''INSERT INTO students
                (fname, lname, state, city, pin, mobile, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',(fname, lname, state, city, pin, mobile, email))
    db.commit()
    return FileResponse('fastapi_server/pages/thankyou.html', media_type="text/html")

app.mount('/', StaticFiles(directory='fastapi_server/pages/', html=True), name='home')
# app.mount('/images', StaticFiles(directory='fastapi_server/images/'), name='images')
# app.mount('/videos', StaticFiles(directory='fastapi_server/videos/'), name='videos')
# app.mount('/notes', StaticFiles(directory='fastapi_server/notes/'), name='notes')
uvicorn.run(app=app, host='0.0.0.0', port=3000)

# fname=utsav&lname=baroliya&state=Meghalaya&city=Bhavnagar+District%2C+G...&pin=364002&mobile=9724716143&email=baroliyautsav003%40gmail.com