// Learn stuff about our users.

+ mi nombre es *
- <set name=<formal>>Es un gusto conocerte, <get name>.
- <set name=<formal>><get name>, Encantado.

+ mi nombre es <bot master>
- <set name=<bot master>>Ese es mi nombre tambien.

+ mi nombre es <bot name>
- <set name=<bot name>>Que coincidencia ese tambien es mi nombre!
- <set name=<bot name>>Ese tambien es mi nombre!

+ llamame *
- <set name=<formal>><get name>, Te llamare de ahora en adelante.

+ yo tengo * anios
- <set age=<star>>Mucha gente tiene <get age>, no estas soloe.
- <set age=<star>>Cool, yo tengo <bot age>.{weight=49}

+ yo soy (@malenoun)
- <set sex=male>Bien, asi que eres <star>.

+ yo soy (@femalenoun)
- <set sex=female>Ok, eres una ninia.

+ yo (soy de|vivo en) *
- <set location=<formal>>Yo he hablado con gente de <get location> en alguna ocacion.

+ mi * favorita es *
- <set fav<star1>=<star2>>Porque es tu favorita?

+ yo soy soltero
- <set status=single><set spouse=nobody>yo tambien lo soy.

+ yo tengo una novia
- <set status=girlfriend>Cual es su nombre?

+ yo tengo un novio
- <set status=boyfriend>Cual es su nombre?

+ *
% cual es su nombre
- <set spouse=<formal>>Que bonito nombre.

+ *
% cual es su nombre
- <set spouse=<formal>>Buen nombre.

+ mi (novia|novio)* se llama *
- <set spouse=<formal>>Que bonito nombre.

+ (ual es mi nombre|quien soy|sabes mi nombre|sabes quien soy){weight=20}
- Tu nombre es <get name>.
- Me dijiste que tu nombre era <get name>.
- No eras <get name>?

+ (que edad tengo|sabes que edad tengo|sabes mi edad){weight=20}
- Tu tienes <get age> anios.
- Tienes <get age>.

+ soy un (@malenoun) o una (@femalenoun){weight=10}
- Eres <get sex>.

+ soy (@malenoun) o (@femalenoun){weight=10}
- Tu eres <get sex>.

+ cual es mi * favorita{weight=10}
- Tu <star> Favorita es <get fav<star>>

+ quien es mi (novio|novia|esposo|esposa){weight=10}
- <get spouse>