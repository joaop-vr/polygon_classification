# Classificação de Polígonos

Este projeto realiza a leitura de um conjunto de polígonos e pontos, classifica os polígonos quanto à sua simplicidade e convexidade, e verifica em quais polígonos cada ponto está contido. Opcionalmente, também é possível visualizar os dados em um gráfico.

## 📦 Pré-requisitos

- Python 3 (recomendado: 3.8+)
- `make` (para utilizar os comandos automatizados)
- O programa cria automaticamente um ambiente virtual (`poly_env`) e instala as dependências necessárias.

## ⚙️ Como configurar e executar com Makefile

### 🔧 Configurar ambiente virtual e instalar dependências

```bash
make setup
```

Esse comando criará um ambiente virtual `poly_env`, instalará as dependências do `requirements.txt` e mostrará as instruções finais.

### ▶️ Rodar o programa com entrada padrão

```bash
make run
```

Este comando executa o programa com o arquivo `entrada.txt`. Você pode alterar o conteúdo do arquivo conforme necessário.

### 🧼 Remover ambiente virtual

```bash
make clean
```

Esse comando remove o ambiente `poly_env`.

### 🆘 Ver ajuda

```bash
make help
```

---

## 📜 Executar manualmente (sem Makefile)

```bash
# Criar e ativar ambiente virtual
python3 -m venv poly_env
source poly_env/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar programa com arquivo de entrada
python3 poligonos.py < testes/t1.txt
```

### 🔍 Para exibir visualização gráfica

Use a flag `-p` após o nome do script:

```bash
python3 poligonos.py -p < testes/t1.txt
```

## 📝 Formato do arquivo de entrada (`testes/t1.txt`)

- Primeira linha: dois inteiros `m n`, onde `m` é o número de polígonos e `n` é o número de pontos.
- Para cada polígono:
  - Uma linha com o número de vértices.
  - Seguem `ni` linhas com coordenadas `x y` dos vértices.
- Depois dos polígonos, `n` linhas com coordenadas dos pontos.

#### Exemplo:
```
4 4
4
0 0
4 0
4 4
0 4
4
5 5
8 5
8 8
5 8
4
1 1
2 1
2 2
1 2
5
10 10
12 10
11 11
12 12
10 12
2 2
6 6
1 1
12 11
```

## 🧩 Saída esperada

A saída consiste na classificação dos polígonos e a indicação de quais polígonos contêm cada ponto, numerados a partir de 1.

```
1 simples e convexo
2 simples e convexo
3 simples e nao convexo
4 nao simples
1:1 2
2:
3:1 3
4:2
```

## 🛠️ Observações

- Certifique-se de estar usando `python3`.
- O uso do `-p` ativa a visualização via `matplotlib`, abrindo uma janela com os polígonos e os pontos.
- O `Makefile` é recomendado para facilitar a configuração e execução.

---

Desenvolvido por João Pedro Vicente Ramalho 🎓
