# Classificação de Polígonos

Este projeto realiza a leitura de um conjunto de polígonos e pontos, classifica os polígonos quanto à sua simplicidade e convexidade, e verifica em quais polígonos cada ponto está contido. Opcionalmente, também é possível visualizar os dados em um gráfico.

## 📦 Pré-requisitos

- Python 3 (recomendado: 3.8+)
- `virtualenv` (opcional, mas recomendado)
- `matplotlib` para visualização

## 🧪 Como configurar o ambiente (opcional)

```bash
# Navegue até a pasta do projeto
cd ~/pasta_projeto

# Crie o ambiente virtual
python3 -m venv poly_env

# Ative o ambiente virtual
source poly_env/bin/activate

# Instale as dependências
pip install matplotlib
```

## ▶️ Como rodar o programa

O programa espera um arquivo de entrada no seguinte formato via redirecionamento (`<`):

```bash
python3 poligonos.py < testes/t1.txt
```

### 🔍 Para exibir visualização gráfica

Use a flag `-p` após o nome do script:

```bash
python3 poligonos.py -p < testes/t1.txt
```

### 📝 Formato do arquivo de entrada (`testes/t1.txt`)

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

---

Desenvolvido por João Pedro Vicente Ramalho 🎓