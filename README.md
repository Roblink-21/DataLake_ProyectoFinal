# DataLake_ProyectoFinal

# Integrantes

* Miguel Cuenca
* Luis Jacome
* Kevin Morales
* Roberth Pincha
* Carlos Quel
* Sebastian Valencia
* Michael Valenzuela

# Proyecto Final Análisis de datos

Diseñar una arquitectura de Data Lake en la cual tenga el insumo de datos de al menos las siguientes fuentes:

3 bases de datos SQL

3 bases de datos NoSQL


Estas fuentes deben tener a su vez como insumo fuentes de Internet (facebook, twitter, webscrapping, tiktok, linkedin) y además archivos estáticos de kaggle, INEC, etc.

Como concentrador de datos debe utilizar elasticsearch y con datos actualizados, realizar un caso de estudio para cada una de las siguientes temáticas:


* Pulso político en 20 ciudades principales de Ecuador, listas y candidatos, presidenciales y diputados.

* Pulso político por provincias en Ecuador, listas y candidatos, presidenciales y diputados.

* Juegos en línea por países.

* Tema definido por el estudiante.

* Eventos o noticias mundiales.


La recopilación de información se puede realizar con geolocalización o con filtro de palabras. Si se utiliza geolocalización se recomienda subdividir la región. Si se utiliza filtro de palabras se recomienda usar varias palabras por script.
Se debe crear la indexación en al menos 2 nodos. (debe crear un clúster)

Para las visualizaciones en tiempo real se usará Kibana, para los dashboards estáticos se utilizará cualquier otra herramienta.
Cada caso de estudio debe tener su propio dashboard y de todo el proyecto al menos una visualización debe tener geolocalización.

# ARQUITECTURA

![arquitectura](https://user-images.githubusercontent.com/58127103/133541999-f4d61455-0772-4f3e-afe3-f5453c85397f.png)

# SCRIPTS -- BD SQL

* SQL LITE --- TIKTOK

![image](https://user-images.githubusercontent.com/58041699/133362509-725d8840-3013-4a63-9685-f35397f7c9bc.png)

* SQL LITE --- KAGGLE(CSV)

En la pagina de KAGGLE podemos contar con dataset's de una gran variedad de temas, para esta practica haremos uso de un dataset sobre las variantes del covid.

![image](https://user-images.githubusercontent.com/58041699/133369877-feda218e-6ad1-4a29-a8a2-a99693efabf7.png)

![image](https://user-images.githubusercontent.com/58041699/133370546-0acecbed-11a7-417e-860b-0d9d7809d17f.png)


Ese dataset que adquirimos podemos trasladarlo a un gestor base de datos como sql lite, de esta manera esos datos seran registros de una tabla relacional.

![image](https://user-images.githubusercontent.com/58041699/133370797-5cbec501-f64b-4007-96e5-fc4495ed9c21.png)

Una vez importada la data, ya hemos conseguido una BD SQL donde podemos observar las dominios de cada columnas.
![image](https://user-images.githubusercontent.com/58041699/133545801-62d33216-eb69-4600-8640-6f39979cdb3d.png)

* MYSQL-(PHPMYADMIN) --- INEC

Dentro de la pagina oficial del Instituto Nacional de Estadística y Censos, podemos encontrar informacion a nivel demografico, educacional, salud y bienestar, economia, agricultura, ambiental y entre otros acerca de estado de nuestro Pais.
![image](https://user-images.githubusercontent.com/58041699/133373411-6fd4e9fa-8cc9-485c-84e9-246b14631f83.png)

De esta manera usaremos datos del INCE para realizar la practica. El tema trata del Índice de Nivel de Actividad Registrada (INA-R) donde extreremos el desempeño económico-fiscal de los sectores productivos de la economía nacional entre el año 2016

![image](https://user-images.githubusercontent.com/58041699/133374678-c8d94add-8d02-4330-8312-3e8125817327.png)


En nuestro gesto de Base de datos MYSQL vamos a integrar este csv y realizamos las configuraciones pertinentes para su integracion.

![image](https://user-images.githubusercontent.com/58041699/133385694-981bf8ae-d6fc-4d83-89e1-7a1872e584c1.png)


![image](https://user-images.githubusercontent.com/58041699/133385759-1f73137f-a9b9-48a7-83d1-f0a06753403c.png)

Una vez establecida las configuraciones podemos dar un vistaso previo a la tabla con los datos del csv y la base de datos creada.

![image](https://user-images.githubusercontent.com/58041699/133385878-34dd6d52-6fd9-4e02-a4f4-34d87ed2557e.png)

![image](https://user-images.githubusercontent.com/58041699/133386150-4aad8803-c0b9-45ce-9cb6-8141c229fb08.png)











# SCRIPTS -- BD NOSQL

* WebScraping --- MONGODB

1. Se empieza estableciendo la conexión con mongodb mediante pymongo y se hace la importación de las respectivas herramientas

![image](https://user-images.githubusercontent.com/58041699/131235523-e4c89d15-25d0-4ed9-b0e3-48660fb10109.png)

2. Se generan las funciones para su posterior limpieza mediante un for

![image](https://user-images.githubusercontent.com/58041699/131235530-0c03d5df-9e9e-485c-9183-871fb0a690eb.png)

![image](https://user-images.githubusercontent.com/58041699/131235533-687e6239-243b-4465-9b3b-09f2697c9851.png)

3. Se trasladan los datos al dataframe

![image](https://user-images.githubusercontent.com/58041699/131235546-6c0d42b7-43f5-4d8d-97fc-5fd32f7d43b1.png)

![image](https://user-images.githubusercontent.com/58041699/131234850-c4574f9d-704a-4328-81b6-f0a91db4fab3.png)

4. Se establece la conexión con mongodb y se insertan los datos

![image](https://user-images.githubusercontent.com/58041699/131235200-1708c939-b9dc-4b2d-bcb8-0b9518ec2b6b.png)

5. Por ultimo la información que se envio es presentada en formato JSON

![image](https://user-images.githubusercontent.com/58041699/131235219-351a6b02-39e1-4977-9bd3-f2a4e95f3f92.png)

* Facebook --- COUCHDB

1. Se raliza la importación de las respectivas librerias

![librerias](https://user-images.githubusercontent.com/58050574/133524002-bf673cac-152d-482e-8d79-410d24edad7f.png)

2. Se crea la base de datos y establece la conexión

![conexion](https://user-images.githubusercontent.com/58050574/133524776-375ab18c-78db-4bb0-8faf-4c5517b28417.png)

3. Se procede a realizar la extracción de los datos los cuales seran guardados en la base de datos

![extraccionDatos](https://user-images.githubusercontent.com/58050574/133524971-a0bd8741-fbc1-4953-a481-7f454a02e41e.png)

4. Una vez recopilado los datos podemos verlos en couchdb tanto la base de datos steam como el numero de documentos los cuales se presentan en formato json

![couchdbSteam](https://user-images.githubusercontent.com/58050574/133525283-65087722-6544-4b6c-a03d-0dc9ac67bec6.png)

![BDSteam](https://user-images.githubusercontent.com/58050574/133525374-6df5663a-fa0d-447e-bc1d-920323bc4ef8.png)

![Steamjson](https://user-images.githubusercontent.com/58050574/133525549-5915d092-be2e-47df-ba3a-f49ab5800197.png)

5. Vistas

5.1 Para la primera vista imprimimos una clave designada “Steam”

![vista1indx1](https://user-images.githubusercontent.com/58050574/133539805-84c5d54a-59b0-4921-88e6-1a371fda7351.png)

![vista1indx1(2)](https://user-images.githubusercontent.com/58050574/133539821-3375138d-0cf6-4d9e-a80f-8ebaf75f00dd.png)

5.2 Para la segunda vista se busco entre los datos de texto los que contengan “PC” y “play”

![vista2indx1](https://user-images.githubusercontent.com/58050574/133539921-61f80d57-c79c-46e0-af75-1cc50ee6b7f8.png)

![vista2indx2(1)](https://user-images.githubusercontent.com/58050574/133539927-f52db92e-1768-464f-ba78-0bb9147e039e.png)

![vista2indx2(2)](https://user-images.githubusercontent.com/58050574/133539935-db751d52-484e-4989-8987-5a47e6faf511.png)

5.3 Para la tercera vista se aplico la función reduce para calcular el numero de ocurrencias de la palabra “buy” y “new” en el texto

![vista3indx1](https://user-images.githubusercontent.com/58050574/133540388-e0c7f8ce-d266-442b-8ad7-2265d0214e41.png)

![vista3indx1(1)](https://user-images.githubusercontent.com/58050574/133540207-c4228932-033c-4a84-977d-cd11e0260e1f.png)

![vista3indx1(2)](https://user-images.githubusercontent.com/58050574/133540266-228d94ed-41f8-421f-a6c7-a83c30a654e2.png)













# ELASTICSEARCH -- CONCENTRADOR DE DATOS


# VISUALIZACION - (POWER BI, KIBANA)

* Power BI

![image](https://user-images.githubusercontent.com/58041699/133537130-6cb1fbdf-f2c8-44c9-b98f-dc1a2e8ad225.png)

