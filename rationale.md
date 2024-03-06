El script fygure.py, define una función count_figures_in_xml(xml_file) que cuenta el número de elementos figure en los archivos XML proporcionados como entrada por la ruta que hemos asignado, lo lee y busca todos los elementos figure, devuelve el número de elementos figure encontrados.
Define una función process_directory(input_directory) que procesa todos los archivos XML en un directorio dado. Esta función toma como entrada la ruta a un directorio, verifica que el directorio existe y luego procesa cada archivo en el directorio que termine en “.xml”. Para cada archivo XML, llama a la función count_figures_in_xml(input_file) para contar el número de elementos ‘figure’ y luego imprime el resultado.
Finalmente, si este script se ejecuta como un programa (es decir, no se importa como un módulo), llama a la función process_directory(input_directory) con la ruta a un directorio específico como argumento.

El script my_wordcloud.py, define una función extract_abstract_from_xml(xml_file) que extrae el texto del elemento ‘abstract’ de un archivo XML dado. Esta función toma como entrada la ruta a un archivo XML, lo parsea y busca el elemento ‘abstract’. Devuelve el texto del elemento ‘abstract’ si existe, o una cadena vacía si no existe.
Define una función generate_wordcloud(text) que genera una nube de palabras a partir de un texto dado. Esta función toma como entrada una cadena de texto, verifica si el texto contiene al menos una palabra y, si es así, genera una nube de palabras y la muestra en una ventana de matplotlib. Si el texto no contiene palabras, imprime un mensaje indicando que no se puede generar una nube de palabras.
Define una función process_directory_with_wordcloud(input_directory) que procesa todos los archivos XML en un directorio dado y genera una nube de palabras a partir del texto del elemento ‘abstract’ de cada archivo. Esta función toma como entrada la ruta a un directorio, verifica que el directorio exista y luego procesa cada archivo en el directorio que termine en “.xml”. Para cada archivo XML, extrae el texto del elemento ‘abstract’ y genera una nube de palabras a partir de ese texto.
Finalmente, si este script se ejecuta como un programa (es decir, no se importa como un módulo), llama a la función process_directory_with_wordcloud(input_directory) con la ruta a un directorio específico como argumento.


primero lee el archivo coge la info y te saca el numero de figuras
coge la info abstracta y hace un wordcloud a partir de esa info
busca los urls y te los muestra el url de cada archivo
