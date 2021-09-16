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

* RAPIDMINER

Este datset se encuentra con valores nulos en casi todos sus registros, para ello debemos buscar una solucion para descartar esos datos nulos y colocar datos a traves de un promedio. Usaremos la herramienta Rapidminer para realizar una limpieza de datos para rellenar los registros vacios.

![image](https://user-images.githubusercontent.com/58041699/133549763-dec21da4-05d8-41cf-8911-ae04366a28fa.png)

Entonces cargamos la dataset con uno de los componenetes que leen datos NOSQL

![image](https://user-images.githubusercontent.com/58041699/133549852-bffc84b8-ae93-4d5e-a89a-76b55ec5b54a.png)

Luego hacemos usa del componente map para elegir los campos que queremos priorizar ante un cambio, despues hacemos uso del componente de reemplazar los componentes faltantes donde debemos identificar las columnas que tengan valores nulos y tambien eligiremos la respuesta ante los cambios donde sera un promedio de todos los datos.

![image](https://user-images.githubusercontent.com/58041699/133551671-74b21cf7-1d87-417d-8a4b-60e35a2ac268.png)

![image](https://user-images.githubusercontent.com/58041699/133551359-822d3033-3b3e-4ec6-b7ea-364d65921b26.png)

Y luego haremos la ejecucion del modelo para luego poder observar como los datos vacios han sido cubiertos por valores promedios.

![image](https://user-images.githubusercontent.com/58041699/133551800-1fd222af-8f82-449e-8401-2cf1e6254ddd.png)

Entonces con nuestro nuevo dataset, vamos a exportarlo y luego subirlo a nuestro sql lite pero para obtener esos datos no se puede hacer de manera directa para ello contaremos con una BD NOSQL que sera receptor de los datos que posteriormente seran exportados y subidos a sql lite.

* MongoDB

MongoDB nos ayudara con la recepcion de esos datos, como primer paso creamos una BD con un nombre.

![image](https://user-images.githubusercontent.com/58041699/133552382-ddb3c827-48de-4798-9756-8178ed09cdf6.png)

Una vez creada nos dirigiremos a Rapidminer donde crearemos una conexion con nuestra BD.

![image](https://user-images.githubusercontent.com/58041699/133552587-c5a403f4-c840-4ad2-a95f-41fe284b9f83.png)

Una vez creada configuraremos la base de datos y el host para establecer la conexion directa a MongoDB

![image](https://user-images.githubusercontent.com/58041699/133552793-37dedd52-acd8-49da-a180-d3b46dfa9a65.png)

De esta manera ya podemos hacer uso de esta coneccion, para el siguiente paso la añadiremos a nuestro diseño

![image](https://user-images.githubusercontent.com/58041699/133553164-58b22c3e-c0ee-49ce-a863-8a8861eb06f4.png)

Una vez diseñada la arquitectura, verificaremos que en MongoDB se encuentren nuestros datos.

![image](https://user-images.githubusercontent.com/58041699/133553280-5e57e98c-5b17-4abb-8095-c9d1ac3a755a.png)

Para el siguiente paso es extraer estos nuevos datos como csv y los enviaremos SQL LITE

![image](https://user-images.githubusercontent.com/58041699/133553410-3b59526b-3c83-460f-99ed-2ab6fd64fa67.png)


Como ultimo paso cargaremos el nuevo dataset NOSQL a SQL lite convirtiendo asi los datos en SQL, de esta manera ya hemos conseguido una BD SQL donde podemos observar las dominios de cada columnas.
![image](https://user-images.githubusercontent.com/58041699/133553647-48c5d1c3-fb52-45a4-9143-e804c321e92e.png)

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

En power bi iniciamos el programa para poder utilizar los reportes visuales que se haran atraves de nuestra dataset generada. 
![image](https://user-images.githubusercontent.com/58041699/133537130-6cb1fbdf-f2c8-44c9-b98f-dc1a2e8ad225.png)

Para la conexion con SQL Lite no existe un acceso directo para hacer una conexion directa al gestor de base de datos. 

![image](https://user-images.githubusercontent.com/58041699/133546816-c7c90543-46bd-43aa-91a1-3deaf4094d5c.png)


De esta manera lo que si podemos hacer es llamar a la base de datos de manera indirecta con un estandar ODBS, cuyo proposito es hacer posible el acceso a cualquier dato desde cualquier aplicación, sin importar qué sistema de gestión de bases de datos almacene los datos.

Por ello es necesario descargar el gestor ODBS para posteriormente crear un servicio DNS que servira para la comunicacion con la herramienta Power BI

![image](https://user-images.githubusercontent.com/58041699/133547110-6ffb5a3c-99d1-4096-8aaf-a0c1de5b8fcc.png)

Una vez obtenido la herramienta lo que sigue es crear ese servicio DNS donde eligiremos el servicio que queremos usar, luego colocaremos un nombre para su identificacion y ademas añadiremos la ruta de donde se encuentra nuestra base de datos de SQL lite

![image](https://user-images.githubusercontent.com/58041699/133547294-ef90b509-e763-4a58-9f96-cba5e7e1284c.png)

![image](https://user-images.githubusercontent.com/58041699/133547525-9e8b9b78-9bd6-4bc4-84e2-786cb31b6e34.png)

![image](https://user-images.githubusercontent.com/58041699/133547305-67e53319-962a-4414-bbbe-02b59cbc0d77.png)

De esta manera ya podremos usar nuestra BD en Power BI, entonces nuevamente nos dirigiremos a la pestaña de obtencion de datos y eligiremos la herramiento ODBS 

![image](https://user-images.githubusercontent.com/58041699/133547754-c5a29b0f-ceb5-44b9-a913-60a4ba8224fe.png)

Una vez seleccionada rapidamente identificara el servicio de puertas de enlaces junto a varios de los servicios que ya habiamos visto en el gestor ODBS. Entonces seleccionaremos nuestra de puerta de enlace.

![Captura1](https://user-images.githubusercontent.com/58041699/133547811-8e1e39d6-5588-46bd-8f66-f5f9087e6f74.JPG)

Despues tendremos que ingresar algunas credenciales para identificar la BD.

![Captura](https://user-images.githubusercontent.com/58041699/133547947-d5b42644-4cbb-4c59-83a4-51071bd3a847.JPG)

Una vez completado el apartado anterior Power Bi indentificara la BD que hemos designado en el ODBS y se nos mostrara los datos de la tabla.

![Captura2](https://user-images.githubusercontent.com/58041699/133548120-b043c27d-b2c8-46d9-9bab-4bd77c83b218.JPG)

Y con ello abremos importado la data de nuestro SQL LITE a Power BI, y de esta manera ya podremos hacer uso de los reportes visuales.

![Captura3](https://user-images.githubusercontent.com/58041699/133548202-cc84f56e-c284-4cee-b4a9-1f65893e982e.JPG)








