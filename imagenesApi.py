import requests
#se importa la biblioteca request que permite hacer peticiones HTTP.
def get_duck_image_url():   
#se crea la funcion en la que sacara las imagenes 
    url = 'https://random-d.uk/api/random'
    #se crea la funcion con el enlace de la Api
    res = requests.get(url)
    #se crea una variable en la que se envía una solicitud GET a una URL específica y devuelve un objeto de respuesta.
    #en este caso una imagen
    data = res.json()
    #se crea otra variable que es igual a la anterior .json, que es formato de intercambio de datos que se puede usar en Python.
    #por lo tanto en este caso se utiliza para codificar y decodificar datos estructurados. 
    return data['url']
    #aca por ultimo tenemos un return que indica el final de una función y devuelve un valor, el cual en este caso son los valores que se almacenan en 
    #la variable url