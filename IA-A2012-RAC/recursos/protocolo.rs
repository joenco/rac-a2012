+ begin
* <bot time> == dia		=> Buenos días {@iam}
* <bot time> == tarde	=> Buenas tardes {@iam}
* <bot time> == noche	=> Buenas noches {@iam}

+ iam
- le habla <bot name>.\n{@help}

+ help
- ¿En qué puedo ayudarle?.

+ who
- ¿Con quién tengo el gusto de hablar?.

+ [@hello] [@good] [@time]
- {@salute}

+ salute
- Estoy aquí, {@help}

+ [*] (mi nombre [es]|me llamo) *
- <set name={formal}<star2>{/formal}>Es un placer <get name>, yo soy <bot name>.\n{@help}

+ [*] (me llaman|me dicen|me apodan|me conocen como) *
- Lo siento, no puedo llamarlo así.\nSolo se me permite llamarlo por su nombre.
//	- <set nick={formal}<star2>{/formal}>¿Desea que le llame por su nombre o le diga <get nick>.

+ (@bye)
- {@bye}

+ bye
- Gracias por preferirnos, que tenga {@byefinal}

+ byefinal
* <bot time> == dia		=> un buen día.
* <bot time> == tarde	=> una tarde agradable.
* <bot time> == noche	=> una feliz noche.