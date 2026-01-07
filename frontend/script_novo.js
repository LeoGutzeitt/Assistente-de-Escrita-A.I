// Configuração da API
const API_URL = "/api"; // Agora usa URL relativa pois o Flask serve o frontend

// Elementos do DOM
const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const charCount = document.getElementById("charCount");
const loading = document.getElementById("loading");
const toast = document.getElementById("toast");
const copyBtn = document.getElementById("copyBtn");
const sidebar = document.getElementById("sidebar");

// Estilo selecionado (para reescrever)
let estiloSelecionado = "formal";

// ================ NAVEGAÇÃO ================

function mostrarSecao(secaoId) {
  // Remover classe active de todas as seções
  document.querySelectorAll(".content-section").forEach((secao) => {
    secao.classList.remove("active");
  });

  // Remover classe active de todos os nav-items
  document.querySelectorAll(".nav-item").forEach((item) => {
    item.classList.remove("active");
  });

  // Adicionar classe active na seção correspondente
  const secao = document.getElementById(`secao-${secaoId}`);
  if (secao) {
    secao.classList.add("active");
  }

  // Adicionar classe active no nav-item correspondente
  // Encontrar o botão que chamou esta função
  document.querySelectorAll(".nav-item").forEach((item) => {
    const onclickAttr = item.getAttribute("onclick");
    if (onclickAttr && onclickAttr.includes(`'${secaoId}'`)) {
      item.classList.add("active");
    }
  });

  // Fechar sidebar no mobile
  if (window.innerWidth <= 768) {
    sidebar.classList.remove("open");
  }
}

function toggleSidebar() {
  sidebar.classList.toggle("open");
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
}

function toggleTheme() {
  // TODO: Implementar tema claro
  showToast("TEMA CLARO EM DESENVOLVIMENTO!", "info");
}

// ================ EDITOR FUNCTIONS ================

// Atualizar contador de caracteres
inputText?.addEventListener("input", () => {
  const count = inputText.value.length;
  charCount.textContent = `${count} CARACTERES`;
});

function limparTexto(tipo) {
  if (tipo === "input") {
    inputText.value = "";
    charCount.textContent = "0 CARACTERES";
  } else {
    outputText.value = "";
    copyBtn.style.display = "none";
  }
  showToast("TEXTO LIMPO!");
}

async function colarTexto() {
  try {
    const texto = await navigator.clipboard.readText();
    inputText.value = texto;
    inputText.dispatchEvent(new Event("input"));
    showToast("TEXTO COLADO COM SUCESSO!");
  } catch (err) {
    showToast("ERRO AO COLAR TEXTO. USE CTRL+V", "error");
  }
}

function substituirTexto() {
  if (outputText.value) {
    inputText.value = outputText.value;
    inputText.dispatchEvent(new Event("input"));
    outputText.value = "";
    copyBtn.style.display = "none";
    showToast("TEXTO SUBSTITUÍDO!");
  }
}

function copiarResultado() {
  outputText.select();
  document.execCommand("copy");
  showToast("TEXTO COPIADO!");
}

// ================ LOADING & TOAST ================

function showLoading(show = true) {
  if (show) {
    loading.classList.add("active");
  } else {
    loading.classList.remove("active");
  }
}

function showToast(message, type = "success") {
  toast.textContent = message;
  toast.className = `toast ${type} show`;

  setTimeout(() => {
    toast.classList.remove("show");
  }, 3000);
}

// ================ API CALLS ================

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

// ================ FUNCIONALIDADES PRINCIPAIS ================

async function corrigirTexto() {
  const texto = inputText.value.trim();

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading(true);

  try {
    const resultado = await fazerRequisicao("/corrigir", { texto });

    if (resultado.success) {
      outputText.value = resultado.texto_corrigido;
      copyBtn.style.display = "flex";
      showToast("TEXTO CORRIGIDO COM SUCESSO!");

      // Voltar para o editor
      mostrarSecaoById("editor");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("ERRO AO CORRIGIR TEXTO: " + error.message, "error");
  } finally {
    showLoading(false);
  }
}

function selecionarEstilo(estilo) {
  estiloSelecionado = estilo;

  // Remover seleção de todos os cards
  document.querySelectorAll(".style-card").forEach((card) => {
    card.classList.remove("selected");
  });

  // Adicionar seleção ao card clicado
  event.target.closest(".style-card").classList.add("selected");
}

async function reescreverTexto() {
  const texto = inputText.value.trim();

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading(true);

  try {
    const resultado = await fazerRequisicao("/reescrever", {
      texto,
      estilo: estiloSelecionado,
    });

    if (resultado.success) {
      outputText.value = resultado.texto_reescrito;
      copyBtn.style.display = "flex";
      showToast(
        `TEXTO REESCRITO NO ESTILO ${estiloSelecionado.toUpperCase()}!`
      );

      // Voltar para o editor
      mostrarSecaoById("editor");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("ERRO AO REESCREVER TEXTO: " + error.message, "error");
  } finally {
    showLoading(false);
  }
}

async function melhorarTexto() {
  const texto = inputText.value.trim();

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading(true);

  try {
    const resultado = await fazerRequisicao("/melhorar", { texto });

    if (resultado.success) {
      outputText.value = resultado.texto_melhorado;
      copyBtn.style.display = "flex";
      showToast("TEXTO MELHORADO COM SUCESSO!");

      // Voltar para o editor
      mostrarSecaoById("editor");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("ERRO AO MELHORAR TEXTO: " + error.message, "error");
  } finally {
    showLoading(false);
  }
}

async function resumirTexto() {
  const texto = inputText.value.trim();
  const tamanho =
    document.querySelector('input[name="tamanho"]:checked')?.value || "medio";

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading(true);

  try {
    const resultado = await fazerRequisicao("/resumir", { texto, tamanho });

    if (resultado.success) {
      outputText.value = resultado.resumo;
      copyBtn.style.display = "flex";
      showToast(`RESUMO ${tamanho.toUpperCase()} GERADO COM SUCESSO!`);

      // Voltar para o editor
      mostrarSecaoById("editor");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("ERRO AO RESUMIR TEXTO: " + error.message, "error");
  } finally {
    showLoading(false);
  }
}

async function obterSugestoes() {
  const texto = inputText.value.trim();

  if (!texto) {
    showToast("Por favor, digite um texto primeiro", "error");
    return;
  }

  showLoading(true);

  try {
    const resultado = await fazerRequisicao("/sugestoes", { texto });

    if (resultado.success) {
      const sugestoesBox = document.getElementById("sugestoesResult");
      const sugestoesContent = document.getElementById("sugestoesContent");

      sugestoesContent.textContent = resultado.analise;
      sugestoesBox.style.display = "block";

      showToast("ANÁLISE CONCLUÍDA!");
    } else {
      throw new Error(resultado.error);
    }
  } catch (error) {
    showToast("ERRO AO OBTER SUGESTÕES: " + error.message, "error");
  } finally {
    showLoading(false);
  }
}

// Helper para mostrar seção por ID
function mostrarSecaoById(secaoId) {
  document.querySelectorAll(".content-section").forEach((secao) => {
    secao.classList.remove("active");
  });

  document.querySelectorAll(".nav-item").forEach((item) => {
    item.classList.remove("active");
  });

  const secao = document.getElementById(`secao-${secaoId}`);
  if (secao) {
    secao.classList.add("active");
  }

  // Encontrar e ativar o nav-item correspondente
  document.querySelectorAll(".nav-item").forEach((item) => {
    const onclickAttr = item.getAttribute("onclick");
    if (onclickAttr && onclickAttr.includes(`'${secaoId}'`)) {
      item.classList.add("active");
    }
  });
}

// ================ INICIALIZAÇÃO ================

window.addEventListener("load", async () => {
  try {
    const response = await fetch(`${API_URL}/health`);
    const data = await response.json();
    console.log("✅ API Status:", data.message);
    showToast("CONECTADO À API!");
  } catch (error) {
    console.warn(
      "⚠️ API não está respondendo. Certifique-se de que o backend está rodando."
    );
    showToast("API OFFLINE. INICIE O BACKEND!", "error");
  }
});

// Fechar sidebar ao clicar fora (mobile)
document.addEventListener("click", (e) => {
  if (window.innerWidth <= 768) {
    if (!sidebar.contains(e.target) && !e.target.closest(".menu-btn")) {
      sidebar.classList.remove("open");
    }
  }
});
