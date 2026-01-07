# 🚀 Guia de Instalação - Ollama (IA Gratuita e Local)

## O que é Ollama?

Ollama permite rodar modelos de IA **localmente** no seu computador, **sem custo** e **sem precisar de API keys**. É 100% gratuito e open source!

## 📥 Passo 1: Instalar o Ollama

### Windows

1. Baixe o instalador: https://ollama.com/download/windows
2. Execute o arquivo `.exe` baixado
3. Siga o assistente de instalação

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### macOS

1. Baixe o aplicativo: https://ollama.com/download/mac
2. Arraste para a pasta Aplicativos
3. Execute o Ollama

## 🤖 Passo 2: Baixar um Modelo de IA

Após instalar, abra o terminal/PowerShell e execute:

```bash
# Modelo recomendado (rápido e eficiente - ~2GB)
ollama pull llama3.2

# Alternativas:
ollama pull mistral        # Ótimo para português
ollama pull gemma          # Desenvolvido pelo Google
ollama pull phi3           # Pequeno e rápido
```

## ▶️ Passo 3: Iniciar o Ollama

```bash
ollama serve
```

Deixe este terminal aberto enquanto usar a aplicação.

## 🧪 Passo 4: Testar

Em outro terminal:

```bash
ollama run llama3.2
```

Digite uma mensagem para testar. Para sair: `/bye`

## 🔧 Configuração no Projeto

1. No seu arquivo `.env` (copie de `.env.example`):

```
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

2. Pronto! Agora execute o backend:

```bash
cd backend
python app.py
```

## 📊 Modelos Disponíveis

| Modelo   | Tamanho | Velocidade | Qualidade | Recomendado para |
| -------- | ------- | ---------- | --------- | ---------------- |
| llama3.2 | ~2GB    | ⚡⚡⚡     | ⭐⭐⭐    | Uso geral        |
| mistral  | ~4GB    | ⚡⚡       | ⭐⭐⭐⭐  | Português        |
| llama3   | ~5GB    | ⚡⚡       | ⭐⭐⭐⭐  | Alta qualidade   |
| gemma    | ~5GB    | ⚡⚡       | ⭐⭐⭐⭐  | Balanceado       |
| phi3     | ~2GB    | ⚡⚡⚡     | ⭐⭐⭐    | PC mais fracos   |

## 💡 Dicas

- **Primeira execução**: O modelo demora um pouco para carregar (normal)
- **Performance**: Quanto mais RAM, melhor
- **GPU**: Se tiver GPU NVIDIA, Ollama usa automaticamente
- **Sem internet**: Funciona 100% offline depois de baixar o modelo

## 🆘 Resolução de Problemas

### "Ollama não está rodando"

```bash
ollama serve
```

### Trocar de modelo

No `.env`, mude:

```
OLLAMA_MODEL=mistral
```

### Ver modelos instalados

```bash
ollama list
```

### Remover modelo

```bash
ollama rm nome-do-modelo
```

## 🌐 Recursos

- Site oficial: https://ollama.com
- Modelos disponíveis: https://ollama.com/library
- Documentação: https://github.com/ollama/ollama

---

✨ **Vantagens do Ollama:**

- ✅ 100% Gratuito
- ✅ Sem limites de uso
- ✅ Privacidade total (seus dados não saem do PC)
- ✅ Funciona offline
- ✅ Sem API keys necessárias
