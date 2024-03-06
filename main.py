from grobid_client.grobid_client import GrobidClient
import os

def process_directory_with_grobid(input_directory, output_directory):
    # Inicializa el cliente de Grobid
    client = GrobidClient(config_path="../grobid/grobid_client_python/config.json")

    # Verifica que el directorio de entrada exista
    if not os.path.exists(input_directory):
        print(f"El directorio de entrada {input_directory} no existe.")
        return

    # Crea el directorio de salida si no existe
    os.makedirs(output_directory, exist_ok=True)

    # Procesa cada archivo en el directorio de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith(".pdf"):
        	print(filename)
        	input_file = os.path.join(input_directory, filename)
        	output_file = os.path.join(output_directory, filename.replace(".pdf", ".xml"))
        	client.process("processFulltextDocument", input_directory, output=output_directory, consolidate_citations=True, tei_coordinates=True, force=True)

if __name__ == "__main__":
    process_directory_with_grobid("../pipeline", "../grobid/grobid_client_python/resources/test_out/")
