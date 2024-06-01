Instructivo para probar el proyecto:

El proyecto cuenta con una pagina de inicio que es el Home, donde se renderiza un template de Bootstrap personalizado en algunas partes (css propio para stylo del boton home, luego se agregaran más estilos).
Ese template se encuentra en father.html, el cual se utiliza en todas las demás paginas del blog como base.
Haciendo click en los distintos botones del nav, podrás acceder a Categories, Users, Posts y Comments, y ver que utilizan el mismo tema pero con su contenido cambiante en el medio el cual consiste de un titulo y un párrafo antes del footer.
Esos 5 botones de los que hablo, se corresponden con los 5 modelos que cree para mi web en models.py (con sus correspondientes HTML a los cuales heredan) y funcionan ya que todas las urls fueron agregadas con su correspondiente path en el archivo url.py.
Además se encuentran creados 5 formularios, uno para cada modelo, los cuales se crean el forms.py y se renderizan también en el archivo de views.py.
Para poder acceder a esos modelos (no cree botones, lo hice tal cual lo visto en clase), se accede a los mismos tipeando en la consola seguido a la dirección que nos tira cuando le damos python manage.py run server se debe tipear /MyBlog/(aqui el nombre del form que corresponda): estos son, usersForm, CategoriesForm, postsForms y CommentsForms.
En cualquiera de estos forms, se deben rellenar los datos requeridos (cada form tiene su correspondiente HTML) y así se crean los distintos usuarios, categorias, comentarios y posteos. 
Cuando se apreta submit en cada formulario renderiza de nuevo la pagina de inicio pero se cargan los datos ingresados, en caso de que no se ingresaran de forma adecuada nos sale el cartel de error en rojo.
También tenemos la pagina de MyBlog/userSearch donde podemos buscar usuarios por su nombre, completamos dicho campo, le damos enviar y nos trae el resultado de acuerdo a si un usuario con ese nombre fue cargado anteriormente. Utilice filter y no get que nos filtra todo lo que incluya los caracteres ingresados.
Este userSearch renderiza el resultado de acuerdo al archivo HTML de resultSearch (con ese formato) y funciona gracias a la vista incluida en views.py llamada Search que es la que tiene el mencionado filter.

Hay 2 formas de chequear los datos cargados en los formularios, una es mediante SQLite que nos abre las bases de datos en nuestro proyecto y la otra es mediante un admin.
username: ariel_tutor
password: Souto123

con esos datos podras entrar a /admin y ver los datos cargados en los distintos modelos (de acuerdo a lo ingresado en los formularios).
Ese usuario lo cree con permisos de staff y solo de view de los distintos modelos.

