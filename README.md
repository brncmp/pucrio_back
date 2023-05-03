Este pequeno projeto corresponde ao backend MVP da Sprint 1 da Disciplina Desenvolvimento Full Stack Basico - PUCRIO

ORIENTAÇOES PARA RODAR O PROJETO BACKEND

Python 3.10.0

Criar e ativar o ambiente virtual: (https://virtualenv.pypa.io/en/latest/installation.html)

Instalar todas a dependencias do projeto na venv criada executando o seguinte comando:
    pip install -r requirements.txt

Criar e executar as migrations: (tenha certeza de estar dentro da pasta 'back' onde se encontra o arquivo manage.py)
    python manage.py makemigrations
    python manage.py migrate

Rodar o projeto: (por padrão rodará em 127.0.0.1:8000, porém a porta pode ser escolhida digitando a porta desejada na frente do seguinte comando)
    python manage.py runserver

Acesse:
    http://127.0.0.1:8000/api

Swagger em:
    http://127.0.0.1:8000/swagger
    http://127.0.0.1:8000/swagger.json
    http://127.0.0.1:8000/swagger.yaml
    http://127.0.0.1:8000/redoc