# ✍️ ASSISTENTE DE ESCRITA A.I

Uma aplicação web inteligente que utiliza IA **100% GRATUITA** (Ollama) para corrigir erros, reescrever, melhorar e resumir textos em português.

## 🚀 FUNCIONALIDADES

- **✅ CORREÇÃO DE TEXTO**: Corrige erros gramaticais, ortográficos e de pontuação
- **🔄 REESCRITA DE TEXTO**: Reescreve em 4 estilos (formal, informal, técnico, criativo)
- **⬆️ MELHORIA DE TEXTO**: Aprimora qualidade, clareza e coesão
- **📝 RESUMO DE TEXTO**: Gera resumos em 3 tamanhos (curto, médio, longo)
- **💡 SUGESTÕES DE MELHORIA**: Analisa e sugere melhorias sem reescrever
- **🎨 INTERFACE YOUTUBE**: Design escuro moderno com navegação por sidebar
- **🆓 TOTALMENTE GRATUITO**: Sem API keys, sem custos, 100% local

## 📋 PRÉ-REQUISITOS

- **Python 3.8+**
- **Ollama** (IA local e gratuita)
- **Navegador web moderno**

## 🔧 INSTALAÇÃO

### 1️⃣ INSTALAR OLLAMA (IA Gratuita)

**Windows:**

1. Baixe: https://ollama.com/download/windows
2. Execute o instalador `.exe`
3. Reinicie o terminal após instalação

**Linux:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**macOS:**

1. Baixe: https://ollama.com/download/mac
2. Arraste para Aplicativos

### 2️⃣ BAIXAR MODELO DE IA

Abra um terminal e execute:

```bash
ollama pull llama3.2
```

Aguarde o download (~2GB). Modelos alternativos: `mistral`, `gemma`, `phi3`

### 3️⃣ CONFIGURAR BACKEND (Flask)

1. Clone o repositório e navegue até a pasta backend:

```bash
cd backend
```

2. Crie e ative ambiente virtual:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale dependências:

```bash
pip install -r requirements.txt
```

4. **(OPCIONAL)** Configure variáveis de ambiente `.env`:

```env
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### 4️⃣ EXECUTAR APLICAÇÃO

**Terminal 1 - Iniciar Ollama:**

```bash
ollama serve
```

**Terminal 2 - Iniciar Flask:**

```bash
cd backend
python app.py
```

Acesse: **http://localhost:5000**

## 🎯 Como Usar

1. Digite ou cole seu texto na área "Seu Texto"
2. Escolha uma das opções:
   - **Corrigir Erros**: Para corrigir erros gramaticais e ortográficos
   - **Melhorar Texto**: Para aprimorar a qualidade geral
   - **Reescrever**: Escolha um estilo e reescreva o texto
3. O resultado aparecerá na área "Resultado"
4. Clique em "Copiar" para copiar o texto processado

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask, OpenAI API, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **IA**: GPT-3.5-turbo (OpenAI)

## 📁 Estrutura do Projeto

```
Assistente-de-Escrita-A.I/
├── backend/
│   ├── app.py              # Aplicação Flask principal
│   ├── requirements.txt    # Dependências Python
│   ├── .env.example        # Exemplo de variáveis de ambiente
│   └── .gitignore
├── frontend/
│   ├── index.html          # Página principal
│   ├── style.css           # Estilos
│   └── script.js           # Lógica do frontend
├── LICENSE
└── README.md
```

## 🔐 Segurança

- **Nunca compartilhe sua API key**
- O arquivo `.env` está no `.gitignore` para evitar commits acidentais
- Use variáveis de ambiente para configurações sensíveis

## 📝 Notas

- A qualidade dos resultados depende do modelo de IA utilizado
- Você pode ajustar os parâmetros de temperatura nos prompts para resultados diferentes
- É possível adaptar o código para usar outras APIs de IA (Azure OpenAI, Anthropic, etc.)

## 🤝 Contribuindo

Sinta-se à vontade para abrir issues e pull requests!

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
