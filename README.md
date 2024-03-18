# Background Remover Script

This Python script accepts an image file as input, removes the background from the image and creates a new image with a custom extension and in a custom format.

## Installation

You will need Python 3.x installed on your machine. You can download it from the official website: https://www.python.org/downloads/

Once Python is installed, you can clone this repository to your local machine.

## Usage

Run the script with the following command in your terminal:
```sh
sh python main.py -f [file_path] -o [output_directory] -e [extension] -F [format]
```

### Parameters:

- `-f`, `--file`: Path to the input image file. (required)

- `-o`, `--output`: Directory where the output file will be saved. If not specified, the current working directory will be used.

- `-e`, `--extension`: The output file's extension. Default is 'png'.

- `-F`, `--format`: The output file's format. This should be a format that the Python PIL library can handle. Default is 'PNG'.

In the absence of optional parameters, their default values will be used.

### Example:

```sh
sh python main.py -f /home/user/pictures/input.jpg -o /home/user/pictures/output -e jpg -F JPEG
```

This will create an output file named `input_bg_removed.jpg` in the `/home/user/pictures/output` directory.

## License

[MIT](https://choosealicense.com/licenses/mit/)