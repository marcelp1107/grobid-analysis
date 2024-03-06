from grobid_client.grobid_client import GrobidClient
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def extract_abstract_from_xml(xml_file):
    # Parsea el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Encuentra el elemento 'abstract' (esto puede variar dependiendo de la estructura de tu XML)
    abstract = root.find('.//abstract')

    if abstract is not None:
        return abstract.text
    else:
        return ''

def generate_wordcloud(text):
    if len(text.split()) > 0:
        # Genera el WordCloud
        wordcloud = WordCloud().generate(text)

        # Muestra el WordCloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
    else:
        print("El texto no contiene palabras. No se puede generar una nube de palabras.")

def process_directory_with_wordcloud(input_directory):
    # Verifica que el directorio de entrada exista
    if not os.path.exists(input_directory):
        print(f"El directorio de entrada {input_directory} no existe.")
        return

    # Procesa cada archivo en el directorio de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith(".xml"):
            input_file = os.path.join(input_directory, filename)

            # Extrae el texto del abstract del archivo XML
            abstract_text = extract_abstract_from_xml(input_file)

            # Genera un WordCloud a partir del texto del abstract
            generate_wordcloud(abstract_text)

if __name__ == "__main__":
    process_directory_with_wordcloud("../grobid/grobid_client_python/resources/test_out/")
