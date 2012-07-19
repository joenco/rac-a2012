! version = 2.0

> begin
	+ request
	- {ok}
< begin

//	VARIABLES DE BOT

! var master= user
! var name	= Gimena
! var about	= Soy un sistema experto capaz de responder cualquier\s
^ duda, consulta o pregunta que puedas referente a nuestra compañia

//	SUBSTITUCIONES

! sub +		= mas
! sub -		= menos
! sub x		= por
! sub q		= que
! sub t		= te
! sub m		= me
! sub xq	= porqué

//	CONECTORES GRAMATICALES

! array article		= el la lo un una uno
! array articles	= los las unos unas

! array preposition	= a|ante|bajo|cabe|con|contra|de|desde|
^ en|entre|hacia|hasta|para|por|según|sin|so|sobre|tras 

//	LISTA DE PALABRAS

! array bye 	= adios chao

! array hello	= hola alo ola
! array time	= dia día dias días tarde tardes noche noches
! array good	= buen buenas

! array question= como cuando cuanto cual donde que quien 

! array action	= quiero deseo
! array could	= puedo pudiera podria podrias

! array check	= verificar ver mirar observar decir saber 
! array remove	= quitar quitarme quiten eliminar eliminarme eliminen
! array change	= cambiar modificar remplazar
! array activate= activar activarme activen afiliar afiliarme afilien

! array dirty = estupido|cojer|imbecil|pendejo|puto|puta|porno|orto|culo|pinche|pinchi|
^ cojo|verga|pene|pito|sexo|concha|cabron|putos|putas|mames|pendejos|pendejas|pendeja|
^ estupidos|estupida|joto|lesbiana|lesviana|chinga|porno|mamadas|pendejadas

//	SUBSTITUCIONES DE PERSONA

! person yo	= tu
! person mi	= tu