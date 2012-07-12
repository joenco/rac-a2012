+ (@hello)
- <set hello="simple">{@salute}

+ (@hello)[*] me llamo *
- <set hello="nombre">{@salute} <set name={formal}<star2>{/formal}>

+ [*](@good) [@time]
- <set hello="formal">{@salute}

+ salute
* <get hello> == "simple" => Hola, {@help}
* <get hello> == "nombre" => {random}Encantada {weight=5}|Es un placer{/random} <get name>, {@help}
* <get hello> == "formal" => Buenas, {@help} 

//* <get hello> == "simple" => {random}hola de nuevo, |hola, estoy aquí! {/random}{@help}

+ help
- ¿En que puedo servir?{weight=5}
- ¿Puedo ayudarle en algo?