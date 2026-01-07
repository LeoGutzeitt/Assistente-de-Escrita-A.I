# ✍️ Assistente de Escrita A.I

Uma aplicação web inteligente que utiliza IA para corrigir erros, reescrever e melhorar textos em português.

## 🚀 Funcionalidades

- **Correção de Erros**: Corrige erros gramaticais, ortográficos e de pontuação
- **Reescrita de Texto**: Reescreve textos em diferentes estilos (formal, informal, técnico, criativo)
- **Melhoria de Texto**: Aprimora a qualidade geral do texto, tornando-o mais claro e impactante
- **Interface Responsiva**: Design moderno e intuitivo que funciona em qualquer dispositivo

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI (para obter API key)
- Navegador web moderno

## 🔧 Instalação

### Backend (Flask)

1. Navegue até a pasta backend:

```bash
cd backend
```

2. Crie e ative um ambiente virtual:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

   - Copie o arquivo `.env.example` para `.env`
   - Adicione sua chave da API OpenAI no arquivo `.env`:

   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```

5. Execute o servidor:

```bash
python app.py
```

O backend estará rodando em `http://localhost:5000`

### Frontend

1. Abra o arquivo `frontend/index.html` em seu navegador
   - Ou use um servidor local como Live Server (extensão do VS Code)

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
