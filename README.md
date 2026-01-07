# Assistente de Escrita A.I 🤖

Um assistente de escrita inteligente desenvolvido com Python e Flask que utiliza IA para melhorar seus textos.

## 📋 Descrição

Este projeto é uma aplicação web que ajuda usuários a melhorar seus textos utilizando inteligência artificial. O assistente oferece várias funcionalidades:

- ✅ Correção gramatical
- 🎨 Melhoria de estilo
- 📝 Expansão de texto
- 📊 Resumo de texto
- 🌐 Tradução
- ✨ Escrita criativa

## 🚀 Tecnologias

- **Python 3.8+**
- **Flask** - Framework web
- **OpenAI API** - Para funcionalidades avançadas de IA (opcional)
- **HTML/CSS/JavaScript** - Interface do usuário

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/LeoGutzeitt/Assistente-de-Escrita-A.I.git
cd Assistente-de-Escrita-A.I
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. (Opcional) Configure a API do OpenAI:
```bash
cp .env.example .env
# Edite o arquivo .env e adicione sua chave da API OpenAI
```

## 🎯 Como Usar

1. Inicie o servidor:
```bash
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

3. Digite ou cole seu texto na área de texto

4. Selecione o tipo de assistência desejada

5. (Opcional) Marque a opção "Usar API de IA" se você configurou a chave da API

6. Clique em "Melhorar Texto"

## 🔑 Configuração da API OpenAI (Opcional)

Para usar funcionalidades avançadas de IA:

1. Crie uma conta em [OpenAI](https://platform.openai.com/)
2. Gere uma chave de API
3. Copie o arquivo `.env.example` para `.env`
4. Adicione sua chave no arquivo `.env`

**Nota:** O aplicativo funciona mesmo sem a API do OpenAI, usando melhorias de texto básicas.

## 📂 Estrutura do Projeto

```
Assistente-de-Escrita-A.I/
├── app.py                  # Aplicação Flask principal
├── requirements.txt        # Dependências Python
├── .env.example           # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Este arquivo
├── templates/
│   └── index.html        # Interface do usuário
└── static/
    └── css/
        └── style.css     # Estilos CSS
```

## 🛠️ Funcionalidades

### Modo Básico (Sem API)
- Demonstração das capacidades do sistema
- Funciona sem necessidade de chave de API

### Modo Avançado (Com API OpenAI)
- Correções gramaticais precisas
- Melhorias de estilo profissionais
- Expansão contextual de texto
- Resumos inteligentes
- Tradução entre idiomas
- Aprimoramento criativo

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença GPL-2.0 - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

LeoGutzeitt

## 🙏 Agradecimentos

- OpenAI pela API de IA
- Comunidade Flask
- Todos os contribuidores do projeto