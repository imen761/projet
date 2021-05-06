from typing import Optional
from fastapi import FastAPI , Request
import mysql.connector
import json
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
insc=FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware ,
    allow_origins = ['*'] , 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
@app.get("/contact")
def gets():
    mydb = mysql.connector.connect ( host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * from contact,inscdoct")
    rv = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv :
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@app.post("/add")
async def add(request:Request):
    mydb = mysql.connector.connect ( host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    body = json.loads(await request.body())
    try : 
        mycursor.execute(f"insert into `contact` (nom,prenom,mail,telephone,commentaire) VALUES ('{body['nom']}' , '{body['prenom']}' , '{body['mail']}' , {body['téléphone']} , '{body['commentaire']}' );")
        mydb.commit()
        return {"ok"}
    except : 
        mydb.rollback()
        return {"non"}


    

@app.post("/ajouter")
async def ajouter(request:Request):
    mydb =mysql.connector.connect(host="localhost", user="root",password="",database="gestion-rdv-patient-docteur")
    mycursor=mydb.cursor()
    body=json.loads(await request.body())
    query = (f"insert into `inscdoct` (faculte,specialite,lieu,cnss,etatique,visite,frais,experiences,nom,telephone,mail,mdp,age,dnaiss,img)  values ('{body['faculte']}','{body['specialite']}','{body['lieu']}','{body['cnss']}','{body['etatique']}','{body['visite']}','{body['frais']}','{body['experiences']}','{body['nom']}','{body['telephone']}','{body['mail']}','{body['mdp']}','{body['age']}','{body['dnaiss']}','{body['img']}');")

    try:
       
       # mycursor.execute(f"INSERT INTO client (username, phone, email, password) VALUES( '{client.username}' ,'{client.phone}' ,'{client.email}' ,'{body.password}' ")
        mycursor.execute(query)
        mydb.commit()
        return("ok")
    except:
        mydb.rollback()
        return("no")

@app.post("/envoyer")
async def envoyer(request:Request):
    mydb =mysql.connector.connect(host="localhost", user="root",password="",database="gestion-rdv-patient-docteur")
    mycursor=mydb.cursor()
    body=json.loads(await request.body())
    query = (f"insert into `inscpatient` (habitation,cnss,maladie,visite,salaire,maladies,nom,tel,mail,mdp,age,dnais,img)  values ('{body['habitation']}','{body['cnss']}','{body['maladie']}','{body['visite']}','{body['salaire']}','{body['maladies']}','{body['nom']}','{body['tel']}','{body['mail']}','{body['mdp']}','{body['age']}','{body['dnais']}','{body['img']}');")

    try:
       
       # mycursor.execute(f"INSERT INTO client (username, phone, email, password) VALUES( '{client.username}' ,'{client.phone}' ,'{client.email}' ,'{body.password}' ")
        mycursor.execute(query)
        mydb.commit()
        return("ok")
    except:
        mydb.rollback()
        return("no")



@app.get("/connectiondocteur")
def gets():
    mydb = mysql.connector.connect ( host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT mail,mdp from inscdoct ")
    rv = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv :
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@app.get("/listepatient")
def gets():
    mydb = mysql.connector.connect ( host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * from inscpatient ")
    rv = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv :
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@app.get("/doct")
def gets():#ken nheb naadi query param juste fi west el () nekteb b syntax hedha {esm_el_var}:{type} [EX : gets(id:int) ======> donc fel requete ki naamel get l http://127.0.0.1:8000/gets?id=4 el variable id mte3i fi west el code bech tkoun el valeur mte3ha 4]
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT nom,specialite,img FROM inscdoct")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@app.get("/patient")
def gets():#ken nheb naadi query param juste fi west el () nekteb b syntax hedha {esm_el_var}:{type} [EX : gets(id:int) ======> donc fel requete ki naamel get l http://127.0.0.1:8000/gets?id=4 el variable id mte3i fi west el code bech tkoun el valeur mte3ha 4]
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT nom,maladies,img FROM inscpatient")
    #ena fel resultat eli bech yraja7ouli el api nhebou yrajaali json w assemi el attributs mte3ou houma assemi les attributs mte3i eli f table mtaa el SQL
    row_headers=[x[0] for x in mycursor.description] #EL CODE hedha dima yetaawed donc copy paste w mataabech rouhek
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data


@app.get("/connectionpatient")
def gets():
    mydb = mysql.connector.connect ( host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT mail,mdp from inscpatient ")
    rv = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv :
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@app.post("/login")
async def db_test(request : Request):

    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    body = json.loads(await request.body())
    print (body)
    mycursor.execute(f"select mail, mdp from inscdoct  where (mail = '{body['user']}' ) and (mdp = '{body['pwd']}')")
    row_headers=[x[0] for x in mycursor.description] 
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    return json_data


@app.post("/loginpatient")
async def db_test(request : Request):

    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "gestion-rdv-patient-docteur")
    mycursor = mydb.cursor()
    body = json.loads(await request.body())
    print (body)
    mycursor.execute(f"select mail, mdp from inscpatient  where (mail = '{body['user']}' ) and (mdp = '{body['pwd']}')")
    row_headers=[x[0] for x in mycursor.description] 
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    return json_data
    

