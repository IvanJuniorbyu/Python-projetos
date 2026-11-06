# 🧮 Tabuada em Python - Evolução de Código

Projeto didático mostrando a evolução de um código simples para um código robusto e reutilizável. Feito para praticar fundamentos de Python.

### 📸 Previewython projetos

--- Tabuada do 7 até 10 ---
 1 x  7 =   7
 2 x  7 =  14
...
10 x  7 =  70


### 🚀 Evolução

**V1.0 - Básica**
- Input simples + for loop

**V2.0 - Validação**
- `try / except` para evitar crash com letras
- `while True` para pedir novamente

**V3.0 - Atual (Profissional)**
- Função `def mostrar_tabuada(numero, limite=10)`
- Parâmetro opcional com valor padrão
- Alinhamento com f-string `f'{i:2}'`
- UX: usuário escolhe o limite

### 💡 O que aprendi

1.  **Tratamento de erros:** `try/except ValueError` impede que o programa quebre.
2.  **Funções reutilizáveis:** Escrever uma vez e usar com `mostrar_tabuada(5)` ou `mostrar_tabuada(9, 20)`.
3.  **Experiência do usuário:** Valor padrão com Enter e saída alinhada.

### 🛠️ Como rodar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tabuada-python

# Entre na pasta
cd tabuada-python

# Rode
python tabuada.py

🔮 Próximos passos (Roadmap)

V4.0 - Salvar tabuada em arquivo .txt
V5.0 - Versão web com HTML/JS para portfólio WDD131
V6.0 - Tabuada completa de 1 a 10

👨‍💻 Autor

Feito por Ivan Junior - Estudante de Análise e Desenvolvimento de Sistemas na BYU Idaho
Em aprendizado constante de Python, HTML, CSS e JavaScript.

