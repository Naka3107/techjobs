import sqlite3
from database import inicializar_db, resetear_db, guardar_oferta
from bolsa import Oferta
from auth import registrar_usuario

def seed():
    conn = sqlite3.connect("buscador.db")
    
    resetear_db(conn)
    inicializar_db(conn)
    
    cursor = conn.cursor()
    
    # --- EMPRESAS ---
    empresas = [
        {"email": "raona@test.com", "contraseña": "123456", "nombre": "Raona", "ciudad": "Barcelona", "pais": "Spain", "pagina_web": "raona.com"},
        {"email": "sopra@test.com", "contraseña": "123456", "nombre": "Sopra Steria", "ciudad": "Barcelona", "pais": "Spain", "pagina_web": "soprasteria.com"},
        {"email": "ubisoft@test.com", "contraseña": "123456", "nombre": "Ubisoft", "ciudad": "Paris", "pais": "France", "pagina_web": "ubisoft.com"},
        {"email": "nextret@test.com", "contraseña": "123456", "nombre": "NexTReT", "ciudad": "Barcelona", "pais": "Spain", "pagina_web": "nextret.com"},
        {"email": "thoughtworks@test.com", "contraseña": "123456", "nombre": "ThoughtWorks", "ciudad": "Berlin", "pais": "Germany", "pagina_web": "thoughtworks.com"},
    ]
    
    empresa_ids = {}
    for e in empresas:
        usuario_id = registrar_usuario(e["email"], e["contraseña"], "empresa", conn)
        cursor.execute(
            "INSERT INTO empresas (usuario_id, nombre, ciudad, pais, pagina_web) VALUES (?, ?, ?, ?, ?)",
            (usuario_id, e["nombre"], e["ciudad"], e["pais"], e["pagina_web"])
        )
        empresa_ids[e["nombre"]] = cursor.lastrowid
    
    # --- OFERTAS ---
    ofertas = [
        # Raona
        {"empresa": "Raona", "puesto": "Python Developer", "salario": 26000, "experiencia_minima": 1, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Python", "SQL", "Git"]},
        {"empresa": "Raona", "puesto": "Backend Junior", "salario": 22000, "experiencia_minima": 0, "pais": "Spain", "ciudad": "Madrid", "tecnologias": ["Java", "Spring Boot", "SQL"]},
        {"empresa": "Raona", "puesto": "Data Analyst", "salario": 28000, "experiencia_minima": 2, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Python", "SQL", "Tableau"]},
        {"empresa": "Raona", "puesto": "DevOps Junior", "salario": 24000, "experiencia_minima": 1, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Docker", "AWS", "Git"]},
        {"empresa": "Raona", "puesto": "Frontend Developer", "salario": 25000, "experiencia_minima": 1, "pais": "Spain", "ciudad": "Valencia", "tecnologias": ["JavaScript", "React", "CSS"]},
        # Sopra Steria
        {"empresa": "Sopra Steria", "puesto": "Java Developer", "salario": 30000, "experiencia_minima": 2, "pais": "Germany", "ciudad": "Berlin", "tecnologias": ["Java", "Spring Boot", "SQL"]},
        {"empresa": "Sopra Steria", "puesto": "Fullstack Developer", "salario": 32000, "experiencia_minima": 3, "pais": "Germany", "ciudad": "Munich", "tecnologias": ["JavaScript", "React", "Node"]},
        {"empresa": "Sopra Steria", "puesto": "Cloud Engineer", "salario": 35000, "experiencia_minima": 3, "pais": "France", "ciudad": "Paris", "tecnologias": ["AWS", "Docker", "Python"]},
        {"empresa": "Sopra Steria", "puesto": "QA Engineer", "salario": 24000, "experiencia_minima": 1, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Java", "Selenium", "Git"]},
        {"empresa": "Sopra Steria", "puesto": "Data Engineer", "salario": 33000, "experiencia_minima": 3, "pais": "Germany", "ciudad": "Berlin", "tecnologias": ["Python", "SQL", "Spark"]},
        # Ubisoft
        {"empresa": "Ubisoft", "puesto": "Game Developer", "salario": 38000, "experiencia_minima": 3, "pais": "France", "ciudad": "Paris", "tecnologias": ["C++", "Python", "Git"]},
        {"empresa": "Ubisoft", "puesto": "Backend Engineer", "salario": 35000, "experiencia_minima": 2, "pais": "France", "ciudad": "Lyon", "tecnologias": ["Python", "Docker", "AWS"]},
        {"empresa": "Ubisoft", "puesto": "ML Engineer", "salario": 40000, "experiencia_minima": 4, "pais": "France", "ciudad": "Paris", "tecnologias": ["Python", "TensorFlow", "SQL"]},
        {"empresa": "Ubisoft", "puesto": "Frontend Senior", "salario": 36000, "experiencia_minima": 4, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["React", "TypeScript", "CSS"]},
        {"empresa": "Ubisoft", "puesto": "Mobile Developer", "salario": 32000, "experiencia_minima": 2, "pais": "France", "ciudad": "Paris", "tecnologias": ["Swift", "Kotlin", "Git"]},
        # NexTReT
        {"empresa": "NexTReT", "puesto": "Systems Administrator", "salario": 26000, "experiencia_minima": 1, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Linux", "Docker", "AWS"]},
        {"empresa": "NexTReT", "puesto": "Angular Developer", "salario": 28000, "experiencia_minima": 2, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Angular", "TypeScript", "CSS"]},
        {"empresa": "NexTReT", "puesto": "SQL Developer", "salario": 24000, "experiencia_minima": 1, "pais": "Spain", "ciudad": "Madrid", "tecnologias": ["SQL", "Python", "Git"]},
        {"empresa": "NexTReT", "puesto": "Node Developer", "salario": 27000, "experiencia_minima": 2, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Node", "JavaScript", "SQL"]},
        {"empresa": "NexTReT", "puesto": "Security Analyst", "salario": 31000, "experiencia_minima": 3, "pais": "Spain", "ciudad": "Barcelona", "tecnologias": ["Python", "Linux", "Git"]},
        # ThoughtWorks
        {"empresa": "ThoughtWorks", "puesto": "Software Consultant", "salario": 42000, "experiencia_minima": 4, "pais": "Germany", "ciudad": "Berlin", "tecnologias": ["Python", "Java", "SQL", "Docker"]},
        {"empresa": "ThoughtWorks", "puesto": "DevOps Engineer", "salario": 38000, "experiencia_minima": 3, "pais": "Germany", "ciudad": "Hamburg", "tecnologias": ["Docker", "AWS", "Git", "Linux"]},
        {"empresa": "ThoughtWorks", "puesto": "React Developer", "salario": 34000, "experiencia_minima": 2, "pais": "Germany", "ciudad": "Berlin", "tecnologias": ["React", "TypeScript", "JavaScript"]},
        {"empresa": "ThoughtWorks", "puesto": "Data Scientist", "salario": 44000, "experiencia_minima": 4, "pais": "Germany", "ciudad": "Berlin", "tecnologias": ["Python", "TensorFlow", "SQL"]},
        {"empresa": "ThoughtWorks", "puesto": "Backend Engineer", "salario": 36000, "experiencia_minima": 3, "pais": "Germany", "ciudad": "Munich", "tecnologias": ["Java", "Spring Boot", "Docker", "SQL"]},
    ]
    
    for o in ofertas:
        empresa_id = empresa_ids[o["empresa"]]
        guardar_oferta(Oferta(
            id=None,
            empresa_id=empresa_id,
            nombre_empresa=o["empresa"],
            puesto=o["puesto"],
            salario=o["salario"],
            experiencia_minima=o["experiencia_minima"],
            pais=o["pais"],
            ciudad=o["ciudad"],
            tecnologias=o["tecnologias"]
        ), conn)
    
    # --- PROGRAMADORES ---
    programadores = [
        {"email": "carlos@test.com", "contraseña": "123456", "nombre": "Carlos", "ciudad": "Barcelona", "pais": "Spain", "experiencia": 0, "tecnologias": ["Python", "SQL", "Git"]},
        {"email": "ana@test.com", "contraseña": "123456", "nombre": "Ana", "ciudad": "Madrid", "pais": "Spain", "experiencia": 3, "tecnologias": ["Java", "Spring Boot", "SQL"]},
        {"email": "mikel@test.com", "contraseña": "123456", "nombre": "Mikel", "ciudad": "Bilbao", "pais": "Spain", "experiencia": 2, "tecnologias": ["JavaScript", "React", "Docker"]},
        {"email": "laura@test.com", "contraseña": "123456", "nombre": "Laura", "ciudad": "Barcelona", "pais": "Spain", "experiencia": 5, "tecnologias": ["Python", "TensorFlow", "SQL", "AWS"]},
        {"email": "pierre@test.com", "contraseña": "123456", "nombre": "Pierre", "ciudad": "Paris", "pais": "France", "experiencia": 4, "tecnologias": ["Python", "Docker", "AWS", "Git"]},
        {"email": "marie@test.com", "contraseña": "123456", "nombre": "Marie", "ciudad": "Lyon", "pais": "France", "experiencia": 2, "tecnologias": ["React", "TypeScript", "CSS", "JavaScript"]},
        {"email": "hans@test.com", "contraseña": "123456", "nombre": "Hans", "ciudad": "Berlin", "pais": "Germany", "experiencia": 5, "tecnologias": ["Java", "Spring Boot", "Docker", "SQL"]},
        {"email": "lena@test.com", "contraseña": "123456", "nombre": "Lena", "ciudad": "Munich", "pais": "Germany", "experiencia": 3, "tecnologias": ["Python", "SQL", "TensorFlow"]},
        {"email": "sofia@test.com", "contraseña": "123456", "nombre": "Sofia", "ciudad": "Barcelona", "pais": "Spain", "experiencia": 1, "tecnologias": ["Angular", "TypeScript", "CSS"]},
        {"email": "marco@test.com", "contraseña": "123456", "nombre": "Marco", "ciudad": "Madrid", "pais": "Spain", "experiencia": 4, "tecnologias": ["Python", "Linux", "Docker", "AWS"]},
        {"email": "emma@test.com", "contraseña": "123456", "nombre": "Emma", "ciudad": "Paris", "pais": "France", "experiencia": 6, "tecnologias": ["C++", "Python", "Git", "Linux"]},
        {"email": "jorge@test.com", "contraseña": "123456", "nombre": "Jorge", "ciudad": "Valencia", "pais": "Spain", "experiencia": 2, "tecnologias": ["JavaScript", "Node", "SQL", "Git"]},
        {"email": "nina@test.com", "contraseña": "123456", "nombre": "Nina", "ciudad": "Berlin", "pais": "Germany", "experiencia": 1, "tecnologias": ["Python", "SQL", "Git"]},
        {"email": "alex@test.com", "contraseña": "123456", "nombre": "Alex", "ciudad": "Barcelona", "pais": "Spain", "experiencia": 3, "tecnologias": ["React", "JavaScript", "Python", "SQL"]},
        {"email": "julia@test.com", "contraseña": "123456", "nombre": "Julia", "ciudad": "Hamburg", "pais": "Germany", "experiencia": 4, "tecnologias": ["Docker", "AWS", "Git", "Linux", "Python"]},
    ]
    
    for p in programadores:
        usuario_id = registrar_usuario(p["email"], p["contraseña"], "programador", conn)
        cursor.execute(
            "INSERT INTO programadores (usuario_id, nombre, ciudad, pais, experiencia) VALUES (?, ?, ?, ?, ?)",
            (usuario_id, p["nombre"], p["ciudad"], p["pais"], p["experiencia"])
        )
        programador_id = cursor.lastrowid
        for tec in p["tecnologias"]:
            cursor.execute(
                "INSERT INTO tecnologias_programador (programador_id, tecnologia) VALUES (?, ?)",
                (programador_id, tec)
            )
    
    conn.commit()
    conn.close()
    print("✅ Base de datos poblada correctamente")
    print(f"   5 empresas")
    print(f"   25 ofertas")
    print(f"   15 programadores")

seed()