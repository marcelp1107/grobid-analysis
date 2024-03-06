import os
import xml.etree.ElementTree as ET

def count_figures_in_xml(xml_file):
    # Parsea el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Cuenta los elementos 'figure' (esto puede variar dependiendo de la estructura de tu XML)
    figure_count = len(root.findall('.//figure'))

    return figure_count

def process_directory(input_directory):
    # Verifica que el directorio de entrada exista
    if not os.path.exists(input_directory):
        print(f"El directorio de entrada {input_directory} no existe.")
        return

    # Procesa cada archivo en el directorio de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith(".xml"):
            input_file = os.path.join(input_directory, filename)

            # Cuenta las figuras en el archivo XML
            figure_count = count_figures_in_xml(input_file)

            print(f"El archivo {input_file} contiene {figure_count} figuras.")

if __name__ == "__main__":
    process_directory("../grobid/grobid_client_python/resources/test_out/") 
