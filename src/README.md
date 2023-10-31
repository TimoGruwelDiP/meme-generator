# Generate Memes 

In this project Python is used to open images and transform them to memes. The project includes a web interface where users can generate memes based on provided images, or they be creative and include image urls and own texts.

## Overview

This project consists of multiple modules:
- app.py ==> The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.
- ingestor.py ==> Includes logic to select the appropriate helper for a given file based on filetype.
- meme_engine.py ==> The Meme Engine Module is responsible for manipulating and drawing text onto images.
- meme.py ==> Create memes by interacting with the CLI
- quote_engine.py ==> The Quote Engine module is responsible for ingesting many types of files that contain quotes.
- quote_model.py ==> The QuoteModel is used to create object instances of quotes

### Instructions and Usage

#### Using the Command Prompt

As a user of this project, you can use the command prompt as interface to interact with the code. The utility can be run from the terminal by invoking: 

```
python3 meme.py 
```
The script must take three optional CLI arguments:

- --body _a string quote body_
- --author _a string quote author_
- --path _an image path_

The script returns a path to a generated image. If any argument is not defined, a random selection is used.

#### Using the app

You can also use the web interface by running the app.py file:
```
python3 app.py 
```

This returns a local IP adress that you can enter in the browser. You can then either create random memes by thanks to the local files provided. Or you can enter the "Creator" mode and provide an image url and quotes and authors yourself.

## Dependencies and sub-modules

Below you see a short overview of dependencies of modules:
|Module|Dependencies|
| --- | --- |
| app.py | meme_engine.py, quote_engine.py, ingestor.py |
| ingestor.py | quote_engine.py |
| quote_engine.py | quote_model.py |
| meme.py | ingestor.py, meme_engine.py, quote_model.py |