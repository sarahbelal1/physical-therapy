from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
import hashlib

def sendQuery(query, values):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='PTDB',
                                            user='root',
                                            password='HTML_Hackers_were_here')
        cursor = connection.cursor()
        cursor.execute(query, values)
        records = cursor.fetchone()
        return records
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


class Login(BaseModel):
    email: str
    password: str

class Search(BaseModel):
    patientName: str


app = FastAPI()

@app.post("/login/")
async def login(login: Login):
    email = login.email
    password = login.email.encode()
    hashedPass = hashlib.sha256(password).digest().hexdigest()
    try:
        # ? is used as a placeholder to prevent SQL injection
        query = "SELECT patientName, Therapist, authToken FROM users WHERE email = ? AND hashedPass = ?"
        vals = [email, hashedPass]
        name, therapist, authToken = sendQuery(query, vals)

        return {
            'patientName': name,
            'therapist': therapist,
            'token': authToken
        }
    except:
        return {
            'ERROR 400': 'Invalid email or password'
        }


@app.get("/search/")
async def get_info(searchData: Search):
    patientName = searchData.patientName
    try:
        query = "SELECT desc, Therapist, link FROM therapyTBL WHERE patientName = ?"
        desc, therapist, link = sendQuery(query, [patientName])
        return {
                'patientName': patientName,
                'therapist': therapist,
                'description': desc,
                'videoLink': link
            }
    except:
        return {
            'ERROR 404': 'No data was found!'
        }

uvicorn.run(app, host="127.0.0.1", port=8000)
