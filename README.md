# 📙 BLACKLIST SERVICE PY

Este es un proyecto REST API, el mismo esta realizado con python 3.
Como framework Base se utiliza Flask.

## ℹ️ Para que sirve la Blacklist?

Una blacklist o lista negra es un componente que nos permite administrar el ingreso o egreso de entidades freuduletas.
Una ejemplo seria el detectar un intento de fraude dentro de un flujo de negocio determinado e intentar guardar a esa persona o entidad
para no permitirle que pueda seguir operando en los flujo de negocio por un tiempo determinado.


## Componentes a instalar

### Flask

Flask es un microframework de Python que permite crear aplicaciones web con unas pocas líneas de código, lo que lo hace muy ligero y flexible. Es una alternativa popular a Django, ofreciendo simplicidad y versatilidad en el desarrollo web. Flask es ideal para crear páginas web dinámicas, APIs y aplicaciones web pequeñas y medianas

> pip install Flask



### Entidades Basicas de la blacklist

La blacklist cuenta con estas entidades basicas para poder administrar los ingresos,
los egresos, las causas entre otros topicos.

## Causes

Las causas reflejan el motivo por el cual un registro ingreso a blacklist


| Tipo        | Nombre | Descripción            | 
|-------------|--------|------------------------|
| id          | String | Id                     |
| code        | long   | Código de causa        |
| description | String | Descripcion de causa   |
| created_at  | Date   | Fecha de creación      |
| update_at   | Date   | Fecha de actualización |
| state       | State  | Estado del registro    |


## Domain

Esta tabla representa el domino al cual pertenece un registro de Blacklist


| Tipo        | Nombre | Descripción            | 
|-------------|--------|------------------------|
| id          | String | Id                     |
| code        | String | Código de dominio      |
| description | String | Descripcion de dominio |
| created_at  | Date   | Fecha de creación      |
| update_at   | Date   | Fecha de actualización |
| state       | State  | Estado del registro    |


## Field

Un field es un registro de entrada a la blacklist,  este registro identifica un dato representativo de una persona, por ejemplo su cuil.


| Tipo       | Nombre | Descripción            | 
|------------|--------|------------------------|
| id         | String | Id                     |
| key        | String | Código de dominio      |
| value      | String | Descripcion de dominio |
| created_at | Date   | Fecha de creación      |
| update_at  | Date   | Fecha de actualización |
| state      | State  | Estado del registro    |
| domain     | Long   | Código de dominio      |


## FieldEvent


FieldEvent  se usa para marcar un field con una causa. Al mismo tiempo se le da un tiempo de espiración dentro de la blacklist,  si este tiempo es null
La duración dentro de la la blacklist es indifido.


| Tipo        | Nombre | Descripción             | 
|-------------|--------|-------------------------|
| id          | String | Id                      |
| fieldId     | String | id de field             |
| causeCode   | String | Código de causa         |
| created_at  | Date   | Fecha de creación       |
| update_at   | Date   | Fecha de actualización  |
| expiration  | Date   | Fecha de expiracion     |
| domain      | Long   | Código de dominio       |
| event       | Event  | Evento                  |
| descripcion | String | Descripcion de la causa |
| domain      | Long   | Código de dominio       |



## Colaboradores

- [Kevin Hidalgo](https://github.com/usuario-colaborador-1)
- [Mateo Calcagno](https://github.com/usuario-colaborador-2)
- [Yoel Enrriquez](https://github.com/usuario-colaborador-3)
- [Soria Maximiliano](https://github.com/MaximilianoRodrigoSoria)