# Fundamentos de Internet

## 1. Del Cliente al Servidor

Cuando escribimos `www.youtube.com` en un navegador y presionamos Enter, ocurren varios procesos antes de que el video aparezca en pantalla.

Primero, el navegador actúa como **cliente**. El cliente es el dispositivo o programa que solicita información a otro equipo conectado a Internet.

Cuando escribimos:

```text
www.youtube.com

el navegador necesita saber a qué servidor debe conectarse.

DNS

El navegador consulta el sistema DNS (Domain Name System).

El DNS funciona como una especie de agenda de Internet, ya que convierte un nombre de dominio como:

www.youtube.com

en una dirección IP.

Por ejemplo:

www.youtube.com
        ↓
       DNS
        ↓
Dirección IP

La dirección IP permite identificar el servidor al que debe enviarse la solicitud.

Dirección IP

Después de obtener la dirección IP, el navegador puede conectarse con el servidor correspondiente.

La dirección IP funciona como una dirección que permite localizar dispositivos dentro de una red.

HTTP y HTTPS

El navegador se comunica con el servidor mediante el protocolo HTTP o HTTPS.

En el caso de YouTube se utiliza HTTPS.

HTTPS permite que la información viaje cifrada entre el navegador y el servidor.

El navegador realiza una solicitud HTTP, por ejemplo:

GET / HTTP/1.1
Host: www.youtube.com

El método GET indica que el cliente quiere obtener información.

Servidor

El servidor recibe la solicitud y procesa la información necesaria.

Puede consultar:

Videos.
Títulos.
Miniaturas.
Comentarios.
Usuarios.
Recomendaciones.

Después, el servidor genera una respuesta y la devuelve al navegador.

Una respuesta HTTP puede incluir:

HTTP/1.1 200 OK
Content-Type: text/html

El código 200 OK significa que la solicitud se procesó correctamente.

Visualización en el navegador

El navegador recibe archivos como:

HTML.
CSS.
JavaScript.
Imágenes.
Datos.

Después interpreta esa información y muestra la página en pantalla.

Cuando seleccionamos un video, el navegador realiza nuevas solicitudes al servidor para obtener la información y los datos necesarios para reproducirlo.

Diagrama del proceso
┌──────────────┐
│   Usuario    │
└──────┬───────┘
       │
       │ www.youtube.com
       ▼
┌──────────────┐
│  Navegador   │
│   Cliente    │
└──────┬───────┘
       │
       │ Consulta DNS
       ▼
┌──────────────┐
│     DNS      │
└──────┬───────┘
       │
       │ Dirección IP
       ▼
┌──────────────┐
│  Navegador   │
└──────┬───────┘
       │
       │ Request HTTPS
       ▼
┌──────────────┐
│   Servidor   │
│   YouTube    │
└──────┬───────┘
       │
       │ Response HTTPS
       ▼
┌──────────────┐
│  Navegador   │
│ muestra web  │
└──────────────┘
2. Frontend y Backend en acción

Supongamos que estamos construyendo una aplicación web para agendar citas médicas.

Frontend

El frontend corresponde a la parte de la aplicación con la que interactúa directamente el usuario.

En una aplicación de citas médicas incluiría:

Inicio de sesión.
Lista de médicos.
Calendario.
Selección de fecha y hora.
Formulario de reserva.
Botón para cancelar citas.
Confirmación de citas.

Tres tecnologías que podrían utilizarse son:

HTML.
CSS.
JavaScript.

También podrían utilizarse herramientas como React, Angular o Vue.

Backend

El backend corresponde a la parte del sistema que funciona en el servidor.

Se encarga de la lógica del sistema y de comunicarse con la base de datos.

Por ejemplo:

Registrar usuarios.
Consultar médicos.
Consultar horarios disponibles.
Crear citas.
Modificar citas.
Cancelar citas.
Validar datos.
Guardar información en una base de datos.

Tres tecnologías que podrían utilizarse son:

Node.js.
Java con Spring Boot.
Python con Django o FastAPI.
Comunicación entre frontend y backend

El frontend puede comunicarse con el backend mediante una API.

La API permite enviar solicitudes utilizando HTTP.

Por ejemplo:

GET /api/citas

podría utilizarse para consultar citas.

Mientras que:

POST /api/citas

podría utilizarse para crear una nueva cita.

El proceso sería:

Frontend
   │
   │ HTTP Request
   ▼
API del Backend
   │
   │ Procesa información
   ▼
Base de datos
   │
   ▼
Backend
   │
   │ HTTP Response
   ▼
Frontend

Por ejemplo, el frontend podría enviar:

{
  "medicoId": 15,
  "fecha": "2026-10-20",
  "hora": "10:00"
}

El backend recibe esa información, verifica si el horario está disponible y registra la cita.

Después puede responder:

{
  "id": 500,
  "estado": "confirmada",
  "mensaje": "Cita creada correctamente"
}

De esta manera se produce una comunicación de tipo:

Request → procesamiento → Response
3. REST vs SOAP vs GraphQL
Tipo de API	Formato de datos usado	Nivel de flexibilidad	Dificultad de implementación	Uso actual
REST	JSON / XML	Alta	Baja / Media	Alta
SOAP	XML	Baja / Media	Alta	Media
GraphQL	JSON	Muy alta	Media / Alta	Alta
REST

REST utiliza recursos y métodos HTTP como:

GET.
POST.
PUT.
PATCH.
DELETE.

Es relativamente fácil de implementar y se utiliza ampliamente en aplicaciones modernas.

SOAP

SOAP utiliza principalmente XML.

Tiene una estructura más estricta y normalmente utiliza contratos definidos.

Puede resultar útil en sistemas empresariales donde se requiere una estructura de comunicación muy controlada.

Su implementación suele ser más compleja que REST.

GraphQL

GraphQL permite que el cliente indique exactamente qué información necesita.

Por ejemplo, el cliente puede solicitar únicamente:

nombre
correo

en lugar de recibir toda la información de un usuario.

Esto ofrece mucha flexibilidad, aunque también aumenta la complejidad del sistema.

¿Cuál es más apropiada para una startup moderna? ¿Por qué?

Para una startup moderna que desarrolla un sistema de reservas en línea, utilizaría REST.

REST es relativamente sencillo de desarrollar, mantener y probar.

Además, utiliza métodos HTTP conocidos y normalmente trabaja con JSON, lo que facilita la comunicación entre aplicaciones web, móviles y servidores.

Un sistema de reservas podría utilizar endpoints como:

GET /reservas
GET /reservas/15
POST /reservas
PATCH /reservas/15
DELETE /reservas/15

GraphQL también puede ser útil cuando se necesita mucha flexibilidad en las consultas.

SOAP puede resultar más complejo para este tipo de proyecto debido a su estructura más estricta.

4. Explorando APIs con Postman
4.1 Selección de la API

Nombre de la API:

JSONPlaceholder

Descripción:

JSONPlaceholder es una API REST pública y gratuita que permite realizar pruebas.

Ofrece información ficticia relacionada con:

Usuarios.
Publicaciones.
Comentarios.
Fotografías.
Álbumes.
Tareas.

Para este ejercicio se utilizó principalmente el recurso:

/posts

La dirección base utilizada fue:

https://jsonplaceholder.typicode.com
4.2 Configuración en Postman

Nombre de la colección:

JSONPlaceholder

Dentro de la colección se crearon cuatro solicitudes:

GET     Obtener publicación
POST    Crear publicación
PUT     Actualizar publicación
DELETE  Eliminar publicación

También se creó un Environment llamado:

JSONPlaceholder Environment

con la siguiente variable:

base_url = https://jsonplaceholder.typicode.com

Esto permitió utilizar URLs como:

{{base_url}}/posts/1
4.3 Ejecución y análisis

Las solicitudes realizadas y sus resultados fueron los siguientes:

Solicitud	Método	Endpoint	Código de estado	Notas
Obtener publicación	GET	/posts/1	200 OK	Retornó la publicación con ID 1
Crear publicación	POST	/posts	201 Created	Simuló la creación de una nueva publicación
Actualizar publicación	PUT	/posts/1	200 OK	Simuló la actualización de la publicación
Eliminar publicación	DELETE	/posts/1	200 OK	Simuló la eliminación de la publicación

Uno de los headers importantes observados fue:

Content-Type: application/json

Esto indica que la respuesta del servidor se encuentra en formato JSON.

4.4 Explicación técnica
Obtener publicación

Método HTTP:

GET

Endpoint:

{{base_url}}/posts/1

Parámetros / body:

No se utilizó body.

El número 1 representa el ID de la publicación consultada.

Código de respuesta:

200 OK

Descripción de la respuesta:

La API devolvió la información de la publicación con ID 1.

Ejemplo de respuesta:

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit..."
}
Crear publicación

Método HTTP:

POST

Endpoint:

{{base_url}}/posts

Body enviado:

{
  "title": "Aprendiendo APIs",
  "body": "Esta publicación fue enviada desde Postman",
  "userId": 1
}

Código de respuesta:

201 Created

Respuesta obtenida:

{
  "title": "Aprendiendo APIs",
  "body": "Esta publicación fue enviada desde Postman",
  "userId": 1,
  "id": 101
}

El código 201 Created indica que el servidor aceptó correctamente la solicitud de creación.

JSONPlaceholder simula la creación del registro, por lo que el cambio no queda guardado permanentemente.

Actualizar publicación

Método HTTP:

PUT

Endpoint:

{{base_url}}/posts/1

Body enviado:

{
  "id": 1,
  "title": "Publicación actualizada",
  "body": "El contenido fue actualizado utilizando PUT",
  "userId": 1
}

Código de respuesta:

200 OK

Respuesta obtenida:

{
  "id": 1,
  "title": "Publicación actualizada",
  "body": "El contenido fue actualizado utilizando PUT",
  "userId": 1
}

La respuesta indica que la API aceptó correctamente la actualización.

El cambio es simulado y no se almacena permanentemente.

Eliminar publicación

Método HTTP:

DELETE

Endpoint:

{{base_url}}/posts/1

Parámetros / body:

No fue necesario utilizar body.

Código de respuesta:

200 OK

Respuesta obtenida:

{}

La respuesta vacía indica que la API aceptó la solicitud de eliminación.

La eliminación es simulada.

¿Qué aprendiste del proceso?

Durante este ejercicio aprendí que una API permite que diferentes aplicaciones se comuniquen entre sí.

También comprendí que los métodos HTTP representan diferentes acciones.

Por ejemplo:

GET     → consultar información
POST    → crear información
PUT     → actualizar información
DELETE  → eliminar información

También aprendí que una solicitud puede incluir:

Método HTTP.
URL o endpoint.
Headers.
Parámetros.
Body.

Mientras que una respuesta puede incluir:

Código de estado.
Headers.
Cuerpo de respuesta.

Postman permitió observar de forma directa cómo una solicitud enviada desde un cliente recibe una respuesta por parte de un servidor.

4.5 Reflexión final

Esta actividad me permitió entender mejor cómo funcionan las APIs y cómo se produce la comunicación entre un cliente y un servidor. Mediante diferentes solicitudes HTTP pude observar cómo se puede consultar, crear, actualizar y eliminar información utilizando métodos como GET, POST, PUT y DELETE.

Postman facilitó mucho la comprensión del proceso porque permite construir las solicitudes y observar directamente la respuesta del servidor. Gracias a esto pude relacionar conceptos como endpoint, request, response, código de estado, headers y JSON de una forma práctica.
