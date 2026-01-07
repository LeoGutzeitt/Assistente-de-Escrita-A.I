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

## 🎯 COMO USAR

1. Acesse **http://localhost:5000** no navegador
2. Digite ou cole seu texto no editor
3. Use a **BARRA LATERAL** para navegar entre funcionalidades:
   - **📝 EDITOR**: Área de edição principal
   - **✅ CORRIGIR**: Corrige erros gramaticais
   - **🔄 REESCREVER**: Escolha estilo (formal/informal/técnico/criativo)
   - **⬆️ MELHORAR**: Aprimora qualidade geral
   - **📝 RESUMIR**: Gera resumo (curto/médio/longo)
   - **💡 SUGESTÕES**: Recebe análise e sugestões
4. O resultado aparece no painel direito
5. Use botões **COPIAR** ou **SUBSTITUIR** para gerenciar resultados

## 🛠️ TECNOLOGIAS UTILIZADAS

- **Backend**: Flask 3.0.0, Python 3.x
- **IA**: Ollama (llama3.2 - 100% gratuito e local)
- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Design**: Material Icons, Dark Theme (YouTube-inspired)
- **API**: RESTful com JSON

## 📁 ESTRUTURA DO PROJETO

```
Assistente-de-Escrita-A.I/
├── backend/
│   ├── app.py                 # Flask API + servidor estático
│   ├── requirements.txt       # Dependências Python
│   ├── .env.example          # Template de configuração
│   └── .gitignore
├── frontend/
│   ├── index_novo.html       # Interface YouTube-style
│   ├── style_novo.css        # Dark theme (preto/azul)
│   └── script_novo.js        # Lógica e API calls
├── INSTALL_OLLAMA.md         # Guia detalhado de instalação
├── LICENSE
└── README.md
```

## 🐛 SOLUÇÃO DE PROBLEMAS

### Erro HTTP 500

✅ Verifique se o Ollama está rodando: `ollama serve`
✅ Verifique se o modelo está instalado: `ollama list`
✅ Baixe o modelo se necessário: `ollama pull llama3.2`

### "Ollama não está rodando"

✅ Abra terminal separado e execute: `ollama serve`
✅ Mantenha este terminal aberto durante o uso

### Página não carrega

✅ Verifique se Flask está rodando: `python app.py`
✅ Acesse: http://localhost:5000 (não http://127.0.0.1:5000)

### Resposta muito lenta

✅ Use modelo menor: `ollama pull phi3`
✅ Altere no `.env`: `OLLAMA_MODEL=phi3`
✅ Reinicie o Flask

## 📝 ENDPOINTS DA API

- `GET /api/health` - Status da API
- `POST /api/corrigir` - Corrige texto
- `POST /api/reescrever` - Reescreve em estilo específico
- `POST /api/melhorar` - Melhora qualidade
- `POST /api/resumir` - Gera resumo
- `POST /api/sugestoes` - Analisa e sugere
- `POST /api/verificar-plagio` - (Em desenvolvimento)

## 🚀 PRÓXIMAS MELHORIAS

- [ ] Sistema de histórico com banco de dados
- [ ] Exportação em PDF/DOCX
- [ ] Análise de métricas (palavras, frases, legibilidade)
- [ ] Detecção de plágio (API externa)
- [ ] Tema claro/escuro
- [ ] Autenticação de usuários
- [ ] Cache de respostas (Redis)

## 📄 LICENÇA

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 AUTOR

**Project BitBloom**

---

⭐ **Dica**: Para melhor desempenho, use SSD e pelo menos 8GB de RAM. O modelo `llama3.2` requer ~2GB de espaço em disco.

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
