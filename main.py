from rembg import remove
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(
    description='Programm, das einen Dateipfad entgegen nimmt und einen Output-Pfad anbietet.')
parser.add_argument('-f', '--file', type=str, help='Der Pfad zur Datei')
parser.add_argument('-o', '--output', type=str, help='Der Pfad, in dem die Ausgabe gespeichert wird')

args = parser.parse_args()

if args.file is None:
    file_path = input('Bitte geben Sie den Dateipfad ein: ')
else:
    file_path = args.file

if args.output is None:
    output_path = os.getcwd()
else:
    output_path = args.output

if not os.path.exists(file_path):
    print(f'Die Datei "{file_path}" existiert nicht.')
elif not os.path.isdir(output_path):
    print(f'Das Verzeichnis "{output_path}" existiert nicht.')
else:
    print(f'Der angegebene Dateipfad ist: {file_path}')
    print(f'Der Ausgabepfad ist: {output_path}')

input_image = Image.open(file_path)

output = remove(input_image)

output.save(output_path)