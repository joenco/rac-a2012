! version = 2.0

> begin
	+ request
	- {ok}
< begin

! var master= RAC
! var name	= Gimena
! var about	= Soy un sistema experto capaz de responder cualquier\s
^ duda, consulta o pregunta que puedas referente a nuestra compañia

+ *
* <input> == undefined => <set error=0>no entiendo
* <input> == <input2> => <add error=2>{@ adios}
* <input> == <input1> => <add error=1>verifique el texto
- no entiendo