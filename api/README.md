# 1. Crie e ative o ambiente virtual
```
cd api
python -m venv .venv
source .venv/Scripts/activate
```
# 2. Confirme que o Python é o do venv:
```
python -c "import sys; print(sys.executable)"
```
# 3. Instale as dependências
```
python -m pip install -U pip
python -m pip install -r requirements.txt
```
# 4. Configure o .env
```
BASE_URL=https://jsonplaceholder.typicode.com
TIMEOUT_SECONDS=4
```
# 5. Entra na pasta tests para executar os testes GET e POST
```
cd api/tests
pytest test_api_get.py  
pytest test_api_post.py  
```
# 6. Executar todos os testes
```
pytest -vv
```
## Nesse diretorio encontra o Relatório HTML e logs
- api/tests/reports/report.html

