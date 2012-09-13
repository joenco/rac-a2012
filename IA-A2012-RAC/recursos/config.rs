! version = 2.0

> begin
	+ request
	- {ok}
< begin

//	VARIABLES DE BOT

! var master= rac
! var name	= Gimena
! var about		= Soy un sistema experto capaz de responder tus\s
^ dudas, consultas y/o preguntas referentes a nuestra compañia.

! var plan		=	consumo
! var balance	=	x
! var charge	=	x
! var rent		=	x
 

//	SUBSTITUCIONES

! sub +		= mas
! sub -		= menos
! sub x		= por
! sub q		= que
! sub t		= te
! sub m		= me
! sub xq	= porqué

//	CONECTORES GRAMATICALES

! array article		= el la lo un una uno al
! array articles	= los las unos unas
! array preposition	= a ante bajo cabe con contra de desde en entre hacia hasta para por según sin so sobre tras 

//	LISTA DE PALABRAS

! array bye 	= chao adios

! array hello	= hola alo ola hi
! array time	= dia día dias días tarde tardes noche noches
! array good	= buen buenas buenos

! array question= como cuando cuanto cual donde que quien 

! array action	= quiero deseo
! array could	= puedo pudiera podria podrias
! array like	= gustaria encantaria

! array check	= verificar ver mirar observar decir saber 
! array remove	= quitar quiten eliminar eliminen
! array change	= cambiar modificar remplazar
! array activate= activar activen afiliar afilien

! array dirty = cojer imbecil pendejo puto puta porno orto culo pinche guebo
^ pinchi cojo verga pene pito sexo concha cabron mame pendejo pendeja porno
^ pendejo pendeja estupido estupida joto lesbiana lesviana chinga mamada pendejada

//	SUBSTITUCIONES DE PERSONA

! person yo	= tu
! person mi	= tu