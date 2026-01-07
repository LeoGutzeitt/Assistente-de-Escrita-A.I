from flask import Flask, request, jsonify, send_from_directory
from flask.cli import load_dotenv
from flask_cors import CORS
import os
#from dotenv import load_dotenv
import requests
import json

load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Configuração do Ollama (roda localmente)
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.2')  

def chamar_ollama(prompt, system_prompt, temperature=0.5):
    
    try:
        print(f"[DEBUG] Chamando Ollama em {OLLAMA_URL}")
        print(f"[DEBUG] Modelo: {OLLAMA_MODEL}")
        print(f"[DEBUG] Tamanho do prompt: {len(prompt)} caracteres")
        
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": f"{system_prompt}\n\n{prompt}",
                "temperature": temperature,
                "stream": False
            },
            timeout=120
        )
        
        print(f"[DEBUG] Status da resposta: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            resposta = result.get('response', '').strip()
            print(f"[DEBUG] Resposta recebida: {len(resposta)} caracteres")
            
            if not resposta:
                raise Exception("Ollama retornou resposta vazia")
                
            return resposta
        else:
            raise Exception(f"Ollama retornou erro {response.status_code}: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("[ERRO] Não foi possível conectar ao Ollama")
        raise Exception("Ollama não está rodando. Abra um terminal e execute: ollama serve")
    except requests.exceptions.Timeout:
        print("[ERRO] Timeout ao chamar Ollama")
        raise Exception("Ollama demorou muito para responder. Tente um texto menor.")
    except Exception as e:
        print(f"[ERRO] Erro inesperado: {str(e)}")
        raise Exception(f"Erro ao chamar Ollama: {str(e)}")

# ==================== ROTAS PARA SERVIR O FRONTEND ====================

@app.route('/')
def index():
    """Servir a página inicial"""
    return send_from_directory(app.static_folder, 'index_novo.html')

@app.route('/<path:path>')
def serve_static(path):
    """Servir arquivos estáticos (CSS, JS, etc)"""
    return send_from_directory(app.static_folder, path)

# ==================== ROTAS DA API ====================

@app.route('/api/health', methods=['GET'])
def health():
    """Verificar se a API está funcionando"""
    return jsonify({'status': 'ok', 'message': 'API está funcionando'})

@app.route('/api/corrigir', methods=['POST'])
def corrigir_texto():
    """Corrigir erros gramaticais e ortográficos no texto"""
    try:
        print("\n[INFO] === Requisição de Correção Recebida ===")
        data = request.get_json()
        texto = data.get('texto', '')
        
        if not texto:
            print("[ERRO] Texto vazio recebido")
            return jsonify({'error': 'Escreva algum texto para ser corrigido'}), 400
        
        print(f"[INFO] Texto recebido: {len(texto)} caracteres")
        
        system_prompt = "Você é um assistente de escrita especializado em correção de texto em português. Corrija erros gramaticais, ortográficos e de pontuação, mantendo o estilo original do autor. Retorne APENAS o texto corrigido, sem explicações adicionais."
        
        texto_corrigido = chamar_ollama(texto, system_prompt, temperature=0.3)
        
        if not texto_corrigido:
            raise Exception("Ollama não retornou nenhum texto corrigido")
        
        print(f"[SUCESSO] Texto corrigido: {len(texto_corrigido)} caracteres\n")
        
        return jsonify({
            'texto_original': texto,
            'texto_corrigido': texto_corrigido,
            'success': True
        })
    
    except Exception as e:
        print(f"[ERRO] Falha na correção: {str(e)}\n")
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/api/reescrever', methods=['POST'])
def reescrever_texto():
    """Reescrever o texto de forma mais clara e profissional"""
    try:
        data = request.get_json()
        texto = data.get('texto', '')
        estilo = data.get('estilo', 'formal')  # formal, informal, técnico, criativo
        
        if not texto:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        estilos_prompts = {
            'formal': 'Reescreva o texto de forma mais formal e profissional.',
            'informal': 'Reescreva o texto de forma mais informal e casual.',
            'técnico': 'Reescreva o texto de forma mais técnica e detalhada.',
            'criativo': 'Reescreva o texto de forma mais criativa e envolvente.'
        }
        
        system_prompt = f"Você é um assistente de escrita especializado em reescrita de texto em português. {estilos_prompts.get(estilo, estilos_prompts['formal'])} Retorne apenas o texto reescrito, sem explicações."
        
        texto_reescrito = chamar_ollama(texto, system_prompt, temperature=0.7)
        
        return jsonify({
            'texto_original': texto,
            'texto_reescrito': texto_reescrito,
            'estilo': estilo,
            'success': True
        })
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/api/melhorar', methods=['POST'])
def melhorar_texto():
    """Melhorar a qualidade geral do texto"""
    try:
        data = request.get_json()
        texto = data.get('texto', '')
        
        if not texto:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        system_prompt = "Você é um assistente de escrita. Melhore o texto tornando-o mais claro, coeso e impactante, mantendo a mensagem original. Retorne apenas o texto melhorado, sem explicações."
        
        texto_melhorado = chamar_ollama(texto, system_prompt, temperature=0.5)
        
        return jsonify({
            'texto_original': texto,
            'texto_melhorado': texto_melhorado,
            'success': True
        })
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/api/resumir', methods=['POST'])
def resumir_texto():
    try:
        data = request.get_json()
        texto = data.get('texto', '')
        tamanho = data.get('tamanho', 'medio')  # curto, medio, longo

        if not texto:
            return jsonify({'error': 'Não tem o que resumir'}), 400
        
        prompts_tamanho = {
            'curto': 'em 2-3 frases', 
            'medio': 'em 1 parágrafo',
            'longo': 'em 2-3 parágrafos'
        }
        
        system_prompt = "Você é um assistente especializado em resumir textos em português. " + \
                       f"Resuma o texto a seguir {prompts_tamanho.get(tamanho, prompts_tamanho['medio'])}, " + \
                       "mantendo apenas as informações mais importantes. Retorne apenas o resumo."
        
        resumo = chamar_ollama(texto, system_prompt, temperature=0.4)
        
        return jsonify({
            'texto_original': texto,
            'resumo': resumo,
            'tamanho': tamanho,
            'success': True
        })
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/api/sugestoes', methods=['POST'])
def sugerir_melhorias():
    """
    Analisar o texto e dar sugestões de melhoria sem alterar o texto
    
    TODO: Implemente esta funcionalidade
    
    DICAS:
    1. Esta rota NÃO deve reescrever o texto, apenas sugerir melhorias
    2. Peça para a IA retornar uma lista de sugestões
    3. Pode incluir: erros encontrados, sugestões de vocabulário, estrutura, etc.
    4. Use temperature mais alta (0.6-0.8) para sugestões mais criativas
    5. Retorne as sugestões em formato de lista ou texto estruturado
    
    ESTRUTURA DE RESPOSTA:
    {
        'texto_original': texto,
        'sugestoes': [
            'Sugestão 1: ...',
            'Sugestão 2: ...',
        ],
        'pontos_fortes': [...],  # OPCIONAL: adicione isso
        'pontos_fracos': [...],   # OPCIONAL: adicione isso
        'success': True
    }
    """
    try:
        data = request.get_json()
        texto = data.get('texto', '')
        
        if not texto:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        # TODO: Crie um prompt que peça análise e sugestões, não reescrita
        # DICA: Instrua a IA a listar problemas e sugestões numeradas
        system_prompt = """Você é um revisor de textos especializado. 
Analise o texto e forneça sugestões de melhoria organizadas em tópicos.
NÃO reescreva o texto, apenas analise e sugira melhorias.

Formate sua resposta assim:
SUGESTÕES DE MELHORIA:
1. [sua sugestão]
2. [sua sugestão]

PONTOS FORTES:
- [ponto forte]

PONTOS FRACOS:
- [ponto fraco]"""
        
        # TODO: Chame a IA
        analise = chamar_ollama(texto, system_prompt, temperature=0.6)
        
        # TODO AVANÇADO: Parse a resposta e separe em categorias
        # DICA: Use split() ou regex para extrair as seções
        # Por enquanto, retorne a análise completa como string
        
        return jsonify({
            'texto_original': texto,
            'analise': analise,  # TODO: Você pode melhorar isso separando em listas
            'success': True
        })
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/api/verificar-plagio', methods=['POST'])
def verificar_plagio():
    """
    Verificar possível plágio no texto
    
    TODO: Implemente esta funcionalidade
    
    CONCEITOS IMPORTANTES:
    - Plágio real requer comparação com uma base de dados de textos
    - A IA sozinha NÃO pode detectar plágio de fontes externas
    - Mas pode analisar padrões suspeitos e dar indicações
    
    OPÇÕES DE IMPLEMENTAÇÃO:
    
    OPÇÃO 1 - Análise por IA (Limitada):
    - Pedir para IA analisar se o texto parece original
    - Detectar trechos muito formais ou técnicos que parecem copiados
    - Analisar inconsistências de estilo
    
    OPÇÃO 2 - API Externa (Recomendado):
    - Copyscape API (pago): https://www.copyscape.com/apidocumentation.php
    - Plagiarism Checker API (tem planos grátis)
    - Google Search API (buscar trechos do texto)
    
    OPÇÃO 3 - Banco de Dados Local:
    - Salvar textos anteriores em um banco
    - Comparar novo texto com textos salvos
    - Calcular similaridade (use bibliotecas como difflib ou fuzzywuzzy)
    
    EXEMPLO DE IMPLEMENTAÇÃO SIMPLES:
    """
    try:
        data = request.get_json()
        texto = data.get('texto', '')
        
        if not texto:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        # TODO OPÇÃO 1: Análise simples por IA (não detecta plágio real)
        # system_prompt = """Analise o texto e identifique:
        # 1. Trechos que parecem copiados de fontes acadêmicas
        # 2. Mudanças bruscas de estilo
        # 3. Inconsistências que sugerem cópia
        # Seja direto e objetivo."""
        
        # analise_ia = chamar_ollama(texto, system_prompt, temperature=0.3)
        
        # TODO OPÇÃO 2: Usar API externa
        # DICA: Use requests.get() ou requests.post() para chamar a API
        # Exemplo:
        # response = requests.post('https://api-de-plagio.com/check', 
        #                          json={'text': texto})
        
        # TODO OPÇÃO 3: Comparar com banco local
        # DICA: 
        # 1. Instale: pip install fuzzywuzzy python-Levenshtein
        # 2. from fuzzywuzzy import fuzz
        # 3. similaridade = fuzz.ratio(texto, texto_do_banco)
        # 4. Se > 80%, pode ser plágio
        
        # POR ENQUANTO: Retorne uma mensagem explicativa
        return jsonify({
            'error': 'Funcionalidade em desenvolvimento',
            'mensagem': 'Para implementar detecção de plágio, você precisa: \n' +
                       '1. Usar uma API externa (Copyscape, etc.) OU\n' +
                       '2. Criar um banco de dados de textos para comparar OU\n' +
                       '3. Integrar com Google Custom Search API',
            'sugestao': 'Comece pesquisando APIs de detecção de plágio gratuitas',
            'success': False
        }), 501  # 501 = Not Implemented
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


# ==================== DICAS EXTRAS ====================
"""
MELHORIAS ADICIONAIS QUE VOCÊ PODE FAZER:

1. SISTEMA DE HISTÓRICO:
   - Salvar textos processados em um banco SQLite
   - Permitir o usuário ver textos anteriores
   
2. EXPORTAR RESULTADOS:
   - Adicionar rota para exportar em PDF ou DOCX
   - Use bibliotecas: reportlab (PDF), python-docx (Word)

3. ANÁLISE DE MÉTRICAS:
   - Contar palavras, frases, parágrafos
   - Calcular nível de legibilidade (Índice Flesch)
   - Detectar palavras repetidas

4. TRADUÇÃO:
   - Adicionar rota /api/traduzir
   - Traduzir texto para outros idiomas

5. LIMITES E VALIDAÇÃO:
   - Limitar tamanho máximo do texto
   - Validar caracteres especiais
   - Rate limiting para evitar spam

6. AUTENTICAÇÃO:
   - Adicionar sistema de login (Flask-Login)
   - Salvar preferências do usuário

7. CACHE:
   - Usar Redis ou cache simples para respostas repetidas
   - Economizar tempo de processamento
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)