perfil_autor = {
    "nombre": "Patrick Jane",
    "bio": "Consultor experto en observar personas y resolver crimenes.",
    "especialidad": "Investigacion y lectura del comportamiento",
    "redes_sociales": ["@patrick_jane", "@consultor_cbi"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {
    "Python",
    "Investigacion",
    "Psicologia",
    "Observacion",
    "Datos"
}

posts = [
    {
        "id": 1,
        "titulo": "El misterio de la mansion",
        "contenido": "Analisis de las pistas encontradas dentro de una antigua mansion.",
        "autor": perfil_autor,
        "tags": ["Investigacion", "Observacion"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Las pistas de Red John",
        "contenido": "Una recopilacion de indicios relacionados con el caso Red John.",
        "autor": perfil_autor,
        "tags": ["Investigacion", "Psicologia"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "El arte de observar",
        "contenido": "Como prestar atencion a los detalles del comportamiento.",
        "autor": perfil_autor,
        "tags": ["Observacion", "Psicologia"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "Caso sin resolver",
        "autor": perfil_autor,
        "tags": ["Investigacion"],
        "estado": "publicado"
    }
]


def listar_posts(lista):
    if not lista:
        print("No hay posts disponibles.")
        return

    print("\n--- POSTS DISPONIBLES ---")

    for post in lista:
        if not isinstance(post, dict):
            print("- Dato incorrecto")
            continue

        titulo = post.get("titulo", "Sin titulo")
        autor = post.get("autor", {})

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor desconocido"

        print(f"- {titulo} | Autor: {nombre_autor}")


def buscar_por_titulo(lista, termino):
    termino_limpio = termino.strip().lower()

    if termino_limpio == "":
        print("La busqueda no puede estar vacia.")
        return []

    resultados = []

    for post in lista:
        if not isinstance(post, dict):
            continue

        titulo = post.get("titulo", "")

        if isinstance(titulo, str) and termino_limpio in titulo.lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    tag_limpio = tag.strip().lower()

    if tag_limpio == "":
        print("El tag no puede estar vacio.")
        return []

    resultados = []

    for post in lista:
        if not isinstance(post, dict):
            continue

        tags = post.get("tags", [])

        if not isinstance(tags, list):
            continue

        for tag_post in tags:
            if isinstance(tag_post, str) and tag_limpio == tag_post.lower():
                resultados.append(post)
                break

    return resultados


def validar_post(post):
    if not isinstance(post, dict):
        return False, "El post no es un diccionario."

    claves_obligatorias = (
        "id",
        "titulo",
        "contenido",
        "autor",
        "tags",
        "estado"
    )

    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'Falta el dato obligatorio: "{clave}".'

    titulo = post.get("titulo")

    if not isinstance(titulo, str) or titulo.strip() == "":
        return False, "El titulo no es valido."

    contenido = post.get("contenido")

    if not isinstance(contenido, str) or contenido.strip() == "":
        return False, "El contenido no es valido."

    autor = post.get("autor")

    if not isinstance(autor, dict):
        return False, "El autor debe ser un diccionario."

    nombre_autor = autor.get("nombre")

    if not isinstance(nombre_autor, str) or nombre_autor.strip() == "":
        return False, "El autor debe tener un nombre."

    if not isinstance(post.get("tags"), list):
        return False, "Los tags deben estar dentro de una lista."

    if post.get("estado") not in estados_post:
        return False, "El estado no esta permitido."

    return True, "El post es valido."


def validar_posts(lista):
    print("\n--- VALIDACION DE POSTS ---")

    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)

        if isinstance(post, dict):
            titulo = post.get("titulo", "Sin titulo")
        else:
            titulo = "Dato incorrecto"

        if es_valido:
            print(f'Post {numero} - "{titulo}": VALIDO')
        else:
            print(f'Post {numero} - "{titulo}": INVALIDO')
            print(f"Motivo: {mensaje}")


def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        return int(input("Elegi una opcion: "))

    except ValueError:
        print("Error: debes ingresar un numero.")
        return None


def ejecutar_sistema():
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Ingresa el titulo que deseas buscar: ")
            resultados = buscar_por_titulo(posts, termino)

            if termino.strip() == "":
                continue

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts.")

        elif opcion == 3:
            tag = input("Ingresa el tag que deseas buscar: ")
            resultados = filtrar_por_tag(posts, tag)

            if tag.strip() == "":
                continue

            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts con ese tag.")

        elif opcion == 4:
            validar_posts(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog.")
            break

        else:
            print("Opcion invalida. Debes elegir un numero del 1 al 5.")


if __name__ == "__main__":
    ejecutar_sistema()