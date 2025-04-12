.PHONY: setup run clean help

ENV_DIR = poly_env

setup:
	@echo ""
	@echo "Este trabalho foi implementado em python3."
	@echo "O Makefile criará o ambiente Python com todas as dependências necessárias..."
	@echo "Ao final, basta usar o comando 'make clean' para removê-lo."
	@echo ""
	@echo "Criando ambiente virtual em '$(ENV_DIR)'..."
	@python3 -m venv $(ENV_DIR)
	@echo "Ambiente virtual criado."

	@echo "Instalando dependências do requirements.txt... isso levará alguns instantes..."
	@$(ENV_DIR)/bin/pip install --upgrade pip > /dev/null
	@$(ENV_DIR)/bin/pip install -r requirements.txt > /dev/null || (echo "Erro ao instalar dependências." && exit 1)
	@echo "Bibliotecas instaladas com sucesso."

	@echo ""
	@echo "Setup finalizado!"
	@echo "Para ativar o ambiente manualmente, use:"
	@echo "    source $(ENV_DIR)/bin/activate"
	@echo ""
	@echo "Para desativá-lo: deactivate"
	@echo ""
	@echo "Para removê-lo: make clean"
	@echo ""
	@echo "Para rodar o programa, use:"
	@echo "    python3 poligonos.py < nome_do_arquivo_de_entrada"
	@echo ""

run:
	@echo "Executando o programa com o arquivo 'entrada.txt'..."
	@$(ENV_DIR)/bin/python3 poligonos.py < entrada.txt

clean:
	@echo "Removendo ambiente virtual '$(ENV_DIR)'..."
	@rm -rf $(ENV_DIR)
	@echo "Ambiente removido."

help:
	@echo "Comandos disponíveis:"
	@echo "  make setup   - Cria ambiente virtual e instala dependências"
	@echo "  make run     - Executa o programa com entrada.txt"
	@echo "  make clean   - Remove o ambiente virtual"

