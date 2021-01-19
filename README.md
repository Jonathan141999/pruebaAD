# pruebaAD
Nombre: Jonathan Alquinga

Analisis de Datos

Twitter  a couchDB

En este script lo que hacemos es recolectar datos de twitter a una base de datos nsql como es CouchDB, vamos a extraer datos sobre: CNE','elecciones','votaciones para poder analizar esos datos sin necesidad de estar buscando , con estas palabras claves sera mas facil la recoleccion de datos. Todos los datos lo guardamos en la Base de Datos:  prueba0

Web Scrapping a MongoDB

En este script vamos a extrer datos de una pagina web con la ayuda de las etiquetas html que son las que nos van ayudar a realizar la extraccion de datos y poder guardar en Mongo DB todo los datos, la pagina que realizamos este trabajo es: https://www.elsevier.com/es-es/connect un detalle mas es que vamos a escoger una etiqueta padre para poder extraer los datos de las etiquetas hijos. 
El nombre de la Base de Datos es: prueba y la coleccion es my_post 

Es importante crear la Base de Datos manualmente

Facebook a MongoDB

En este escript vamos a recolectar datos de un tema especifico y lo guardaremos en MongoDB. El tema que escogimo para poder realizar la consulta es: Fifa y vamos a darle un limite para que pueda recolectar los datos, el limite es: 10000. Ahora todo esto lo guardaremos en la misma base de datos que tenemos que es: prueba pero en una diferente coleccion que es: post

SQLite a MongoDB


CouchDB a MongoDB

En este script lo que hacemos es realizar una coneccion de CouchDB a MongoDB. En lo que consiste es lo datos que tenemos en CouchDb pasarlo a MongoDB. Aqui vamos a usar la base de datos prueba0 que recolecto datos de CNE','elecciones','votaciones y la exporto a Mongo db en la misma base de datos de web Scrapping y Facebook que es prueba pero con una diferente coleccion que es: prueba5, asi tendremos una sincronizacion de datos en las Bases de Datos nsql

MongoDB a CouchDB

En este script es pasar todos los datos que tenemos en la Base de datos: prueba con sus tres colecciones que son: my_post,post,prueba5 todos los datos que tenemos en estas collecciones las exportamos a mongoDB. La Base de datos de Mongo DB es prueba0.

CouchDB a MongoDB atlas

En este script es poder exportar todos los datos de la Base de datos: prueba a la Base de datos de MongoDB atlas que es: prueba7 y su coleccion es: couchmongo. (aqui es necesario crear la base de datos en la nube), es importante usar la credencial que nos da mongoDB atlas para poder realizar la coneccion y poder exportar los daros con exito.

MongoDB a MongoDB atlas

En este script lo que hicimos es exportar todos los datos que tenemos en MongoDB que es de forma local a MongoDB atlas que es en la nube. Usamos la misma base de Datos prueba7 pero creamos otra colleccion que es: mongoatlas y asi podremos exportar todos los datos de manera local a remota.

MongoDB a Archivos CSV

En este apartado lo podemos hacer de dos formar una es concetar con MongoDBCompass que nos ayuda con una interfaz grafica poder acceder a los datos y poder descargarlos.
