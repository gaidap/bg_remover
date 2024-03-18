from rembg import remove
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(
    description='Programm, das ein Bild entgegen nimmt und ein neues Bild speicher ohne Hintergrund.')
parser.add_argument('-f', '--file', type=str, help='Der Pfad zur Datei')
parser.add_argument('-o', '--output', type=str, help='Der Pfad, in dem die Ausgabe gespeichert wird')
parser.add_argument('-e', '--extension', type=str, default='png', help='Die Dateierweiterung für die Ausgabedatei')
parser.add_argument('-F', '--format', type=str, default='PNG', help='Die Formatangabe für die Ausgabedatei')

args = parser.parse_args()

if args.file is None:
    file_path = input('Bitte geben Sie den vollständigen Dateipfad ein: ')
else:
    file_path = args.file

if args.output is None:
    output_path = os.getcwd()
else:
    output_path = args.output

if not os.path.isfile(file_path):
    print(f'Die Datei "{file_path}" existiert nicht.')
elif not os.path.isdir(output_path):
    print(f'Das Verzeichnis "{output_path}" existiert nicht.')
else:
    print(f'Der angegebene Dateipfad ist: {file_path}')
    print(f'Der Ausgabepfad ist: {output_path}')

input_image = Image.open(file_path)

output = remove(input_image)
output_filename, _ = os.path.splitext(os.path.basename(file_path))

output.save(output_path + os.sep + output_filename + "_bg_removed" + "." + args.extension, args.format)
