🌟 TP MONGODB

📌 Requisitos previos

Instalar:

- Git
- Python
- Mongo
- MySQL Server & MySQL Workbench
- IntelliJ IDEA o cualquier IDE compatible con Spring Boot

---

🔹 **Clonar el repositorio**

Ejecuta el siguiente comando en la terminal:
```bash
git clone https://github.com/cachi001/MongoTP.git
```

---

🔹 **Configurar y ejecutar el Backend**

1. Abre la carpeta del **backend** en IntelliJ IDEA.
2. Asegúrate de tener **MySQL Workbench** y **MySQL Server** instalados y en ejecución.
3. Configura la conexión a la base de datos en el archivo `application.properties`:

```properties
spring.application.name=mongo-tp

spring.jpa.hibernate.ddl-auto=update
spring.datasource.url=jdbc:mysql://localhost:3306/paises_db  # Nombre de la BD
spring.datasource.username=root  # Usuario
spring.datasource.password=1122  # Contraseña
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.show-sql=true
```

4. Ejecuten la aplicación desde IntelliJ IDEA.

🔹 ** Descargar e instalar MONGODB **
1. Añadir el path a LAS VARIABLES DE ENTORNO CON LA DIRECCION DONDE SE INSTALO MONGO. ** (mongod) **
  **  LUEGO DE INSTALAR AGREGAR LAS VARIABLES DE ENTORNO ** ![image](https://github.com/user-attachments/assets/6afa0543-5d25-499a-a441-60a944e403ae)

3. Ir a disco local y crear una carpeta con el nombre ** data ** y dentro una carpeta con nombre ** db **
  ** CREAR CARPETA DATA ** ![image](https://github.com/user-attachments/assets/d0d021e8-df1a-4c89-a751-1c2d137c3199)
  **  DENTRO CREAR CARPETA DB ** ![image](https://github.com/user-attachments/assets/8fc33a04-7dd5-4a0f-8712-fc9542501806)

4. DESCARGAR ** MONGODB SHELL **, guardar la carpeta dentro de MongoDb junto a la Carpeta Server
  ** DESCARGAR ** ![image](https://github.com/user-attachments/assets/64fc8ea8-07f0-4c6f-8e2c-1357e717b8f0)
  **  MOVER A ** ![image](https://github.com/user-attachments/assets/86d6c0cb-0c26-48fa-b2ab-013a9f97cdba)

5. PARA QUE SE CREE LA BASE DE DATOS EN MONGODB HAY Q EJECUTAR  ** mongod  ** en la consola
 
