! array hello = hola|alo
^ buen dia|buenos dias|buenas tardes|buenas noches

+ (@hello)
* <get call> == undefined => <set call=1>{random}
^ Hola, dime en que te puedo ayudar.|
^ Buenas en que puedo servirle.{/random}
- Hola de nuevo, digame en que le puedo ayudar.
- Hola, estoy aquí!. \n ¿Díme en que te puedo ayudar?.