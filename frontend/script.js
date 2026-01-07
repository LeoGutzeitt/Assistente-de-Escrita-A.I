// Configuração da API
const API_URL = "http://localhost:5000/api";

// Elementos do DOM
const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const charCount = document.getElementById("charCount");
const loading = document.getElementById("loading");
const toast = document.getElementById("toast");
const copyBtn = document.getElementById("copyBtn");
const estiloSelect = document.getElementById("estiloSelect");

// Atualizar contador de caracteres
inputText.addEventListener("input", () => {
  const count = inputText.value.length;
  charCount.textContent = `${count} caracteres`;
});

// Mostrar/esconder loading
function showLoading() {
  loading.style.display = "flex";
  disableButtons(true);
}

function hideLoading() {
  loading.style.display = "none";
  disableButtons(false);
}

// Desabilitar/habilitar botões
function disableButtons(disable) {
  const buttons = document.querySelectorAll(".btn");
  buttons.forEach((btn) => (btn.disabled = disable));
}

// Mostrar toast notification
function showToast(message, type = "success") {
  toast.textContent = message;
  toast.className = `toast ${type} show`;

  setTimeout(() => {
    toast.classList.remove("show");
  }, 3000);
}

// Fazer requisição à API
async function fazerRequisicao(endpoint, dados) {
  try {
    const response = await fetch(`${API_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dados),
    });

    if (!response.ok) {
      throw new Error(`Erro HTTP: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Erro na requisição:", error);
    throw error;
  }
}

// Corrigir texto
async function corrigirTexto() {
  const texto = inputText.value.trim();

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading();

  try {
    const resultado = await fazerRequisicao("/corrigir", { texto });

    if (resultado.success) {
      outputText.value = resultado.texto_corrigido;
      copyBtn.style.display = "inline-flex";
      showToast("Texto corrigido com sucesso!");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("Erro ao corrigir texto: " + error.message, "error");
  } finally {
    hideLoading();
  }
}

// Reescrever texto
async function reescreverTexto() {
  const texto = inputText.value.trim();
  const estilo = estiloSelect.value;

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading();

  try {
    const resultado = await fazerRequisicao("/reescrever", { texto, estilo });

    if (resultado.success) {
      outputText.value = resultado.texto_reescrito;
      copyBtn.style.display = "inline-flex";
      showToast(`Texto reescrito no estilo ${estilo}!`);
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("Erro ao reescrever texto: " + error.message, "error");
  } finally {
    hideLoading();
  }
}

// Melhorar texto
async function melhorarTexto() {
  const texto = inputText.value.trim();

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading();

  try {
    const resultado = await fazerRequisicao("/melhorar", { texto });

    if (resultado.success) {
      outputText.value = resultado.texto_melhorado;
      copyBtn.style.display = "inline-flex";
      showToast("Texto melhorado com sucesso!");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("Erro ao melhorar texto: " + error.message, "error");
  } finally {
    hideLoading();
  }
}

// Copiar resultado
function copiarResultado() {
  outputText.select();
  document.execCommand("copy");
  showToast("Texto copiado para a área de transferência!");
}

// Limpar textos
function limparTextos() {
  inputText.value = "";
  outputText.value = "";
  charCount.textContent = "0 caracteres";
  copyBtn.style.display = "none";
  showToast("Textos limpos!");
}

// Verificar saúde da API ao carregar
window.addEventListener("load", async () => {
  try {
    const response = await fetch(`${API_URL}/health`);
    const data = await response.json();
    console.log("Status da API:", data.message);
  } catch (error) {
    console.warn(
      "API não está respondendo. Certifique-se de que o backend está rodando."
    );
  }
});
