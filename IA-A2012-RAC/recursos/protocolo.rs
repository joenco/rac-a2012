+ begin
* <bot time> == dia		=> Buenos d�as {@iam}
* <bot time> == tarde	=> Buenas tardes {@iam}
* <bot time> == noche	=> Buenas noches {@iam}

+ iam
- le habla <bot name>.\n{@help}

+ help
- �En qu� puedo ayudarle?.

+ who
- �Con qui�n tengo el gusto de hablar?.

+ [@hello] [@good] [@time]
- {@salute}

+ salute
- Estoy aqu�, {@help}

+ [*] (mi nombre [es]|me llamo) *
- <set name={formal}<star2>{/formal}>Es un placer <get name>, yo soy <bot name>.\n{@help}

+ [*] (me llaman|me dicen|me apodan|me conocen como) *
- Lo siento, no puedo llamarlo as�.\nSolo se me permite llamarlo por su nombre.
//	- <set nick={formal}<star2>{/formal}>�Desea que le llame por su nombre o le diga <get nick>.

+ (@bye)
- {@bye}

+ bye
- Gracias por preferirnos, que tenga {@byefinal}

+ byefinal
* <bot time> == dia		=> un buen d�a.
* <bot time> == tarde	=> una tarde agradable.
* <bot time> == noche	=> una feliz noche.