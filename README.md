# VERSIÓN 12.0 DE ODOO
# Concesionario

## Módulo ##
Este módulo es una ayuda más específica para controlar las ventas y clientes que tiene un concesionario dedicado a la venta de coches.

## Modelos ##
He usado un único modelo, llamado ventas_coches, en el cual declaro las diferentes clases, en este caso 3 (Ventas, Stock y Clientes).

## Funcionalidad principal ##
En el apartado Ventas se pueden ver los coches vendidos por el concesionario. 
<br>Columnas (izquierda a derecha)

1. Marca: marca del automóvil.
2. Modelo: nombre del modelo.
3. Estado: este campo es de tipo "Selection", se puede elegir entre Disponible, Vendido, Reparación y No disponible.
4. Información extra: como por ejemplo el color de la carrocería.
5. Fecha venta: Fecha en que se realizó la venta del vehículo.
6. Fecha registro: Fecha en que se registró la venta del vehículo en el sistema (campo calculado).
7. Precio: precio del aumóvil.
8. IVA: Fijado en *default* como 21%.
9. Total: Precio multiplicado por 1,21 del IVA.
10. Comprador: Nombre del comprador (cliente), es un campo relacional.
<br>
-Hay dos campos calculados, el primero es el cálculo del precio total con IVA y el segundo es la comparación entra la fecha de venta y de registro (la fecha de venta debe ser menor a la fecha de registro).

En Coches en stock vemos los automóviles que tiene el concesionario para venta directa al público. Este apartado tiene tres tipos de vistas, Form, Tree y Kanban.<br>
Tiene información diversa como cilindrada, tipo decombustible, año... y también cuenta con un apartado específico para subir una foto del coche.
En la vista kanban los coches están ordenados por marca.

El último apartado llamado Clientes, es una lista de los compradores de coches.
<br>Columnas (izquierda a derecha)
1. Ficha cliente: Abre una lista con los clientes de la compañía, también podemos crear nuevos(hereda de res.partner).
<br>*Los siguientes apartados son de información rápida para no tener que abrir la ficha de los clientes.*<br>
2. Domicilio: Domicilio del cliente.
3. Teléfono: Teléfono móvil del cliente.
4. Edad: Edad del comprador del coche. (O de los coches).
5. Descuento: Casilla que verifica que el cliente tuvo un descuento por el concesionario, por la marca o por VIP.

## Explicación de vistas ##
En este módulo hay tres vistas (clientes.xml, stock.xml, y ventas.xml), cada uno de ellos se refiere a su apartado correspondiente. Lo más destacable de las vistas es el apartado stock ya tiene vista kanban y una imagen.


