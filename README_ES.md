# DolarBot

DolarBot es un bot de Telegram simple que brinda información cada hora sobre precios de divisas, centrándose específicamente en la cotización del "dólar blue" en Argentina. Además, obtiene el precio de 1 USDT en pesos argentinos (ARS) en la plataforma P2P de binance.

## Funcionalidades

- Obtiene los valores de compra y venta del "dólar blue" en Argentina a través de la API de dolarsi.
- Recupera el precio de 1 USDT en ARS desde la plataforma P2P de Binance utilizando la API de criptoya.com.
- Envía a los usuarios un mensaje corto con los últimos valores de las divisas.
- Compara el precio actual con el anterior mediante un emoji en cada mensaje.

## APIs

DolarBot utiliza las siguientes APIs:

- [API de dolarsi](https://www.dolarsi.com/): Devuelve los valores de compra y venta del "dólar blue" en Argentina.
- [API de criptoya.com](https://criptoya.com/): Obtiene el precio de 1 USDT en ARS desde la plataforma P2P de Binance.

## Packages

DolarBot depende de las siguientes librerías de Python:

- [requests](https://docs.python-requests.org/en/latest/): Una biblioteca de Python para realizar solicitudes HTTP a APIs externas.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): El SDK de AWS para Python, utilizado para interactuar con varios servicios de AWS.
- [json](https://docs.python.org/3/library/json.html): Un paquete integrado de Python para trabajar con datos JSON.
- [datetime](https://docs.python.org/3/library/datetime.html): Un paquete integrado de Python para trabajar con fechas y horas.
- [dateutil](https://dateutil.readthedocs.io/): Una biblioteca de Python para trabajar con fechas, horas y zonas horarias.

## Uso

Para recibir los últimos precios de las divisas y actualizaciones, puedes unirte al canal de DolarBot en Telegram siguiendo este enlace: [Canal de DolarBot](https://t.me/PrecioDolarBlue).

## Implementación

El bot se puede implementar de varias formas. Una opción es ejecutar el script `main.py` periódicamente como un cronjob. Para hacer esto, se debería modificar el código para manejar adecuadamente las consultas a la base de datos.

Como alternativa, puedes implementarlo como una función AWS Lambda para ejecutarlo periódicamente. Esta es la implementación que elegí debido a su facilidad de uso.

El usuario es libre de explorar y ampliar la funcionalidad del bot agregando más valores de divisas, como la cotización oficial, "Dólar Bolsa", "Dólar MEP", etc., según las necesidades específicas.

## Aclaraciones
DolarBot obtiene el precio de 1 USDT en ARS desde la plataforma P2P de Binance utilizando la API de criptoya.com. Es importante tener en cuenta que el bot no simplemente obtiene el precio más barato disponible. El método exacto para seleccionar el precio de USDT es el siguiente:

1) El bot consulta la API de criptoya.com para obtener los precios disponibles de USDT desde la plataforma P2P de Binance.
2) El bot selecciona los primeros 5 vendedores que cumplen con los siguientes requisitos:
    - Ofrecen MercadoPago como método de pago.
    - Tienen al menos 50 USDT disponibles.
    - El mínimo por transacción es menor o igual a 30,000 AR$.
3) Se recopilan los precios de los vendedores seleccionados.
4) El bot calcula el promedio de los precios seleccionados.
5) El precio promedio calculado se devuelve como el precio de USDT.
6) Si no hay vendedores que cumplan con los requisitos, se repite el precio anterior.

Este enfoque asegura que el precio de USDT obtenido por DolarBot represente un valor razonable basado en los criterios especificados. Al promediar los precios de varios vendedores que cumplen con los requisitos, el bot proporciona un precio más confiable y competitivo para los usuarios.

## Contribuciones

Se aceptan contribuciones al proyecto DolarBot. Si tienes alguna sugerencia, informe de errores o deseas contribuir con nuevas características, no dudes en abrir un problema o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).