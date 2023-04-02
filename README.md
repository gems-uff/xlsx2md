# xlsx2md

Creates Markdown schedule based on an Excel spreadsheet

## Installation

### Requirements

We assume that you have Python 3.11+ installed on your computer

We also assume that the input Excel file has a tab named _Cronograma_ with at least three columns, named _Data_, _Atividade_, and _Entrega_. Moreover, we assume that some special activities in the _Atividade_ column starts with: _Prova_, _Segunda chamada_, _Verificação suplementar_, _Apresentação de trabalho_, _Vista de prova_, and _Sem aula_.  

### Installation

1. Clone our repository:

`~$ git clone https://github.com/gems-uff/xlsx2md.git`

2. Access the project's directory:

`~$ cd xlsx2md`

3. Install pipenv (if you haven't installed it yet)

`~/xlsx2md$ python -m pip install pipenv`

4. Install the necessary libraries:

`~/xlsx2md$ pipenv sync`

## Running the script:

1. Access the project's directory:

`~$ cd xlsx2md`

2. Activate the environment you just created:

`~/xlsx2md$ pipenv shell`

3. Run the script (replace the Excel file to use yours)

`~/xlsx2md$ python xlsx2md.py example.xlsx`
