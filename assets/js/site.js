/* E&E Contabilidade — comportamento do site
   Preencha CONFIG quando os dados reais forem fornecidos. Nada aqui é inventado. */

const CONFIG = {
  whatsapp: "",   // TODO: número com DDI+DDD, só dígitos. Ex.: "5535999999999"
  telefone: "",   // TODO: telefone para exibição
  email: "",      // TODO: e-mail
  instagram: "",  // TODO: URL completa do Instagram
  formEndpoint: "", // TODO: endpoint de envio do formulário (ex.: Formspree/backend)
  mensagemWhatsapp: "Olá! Vim pelo site da E&E Contabilidade e gostaria de falar com uma especialista.",
};

document.documentElement.classList.remove("no-js");

// Links de WhatsApp: se não houver número, levam ao formulário de contato.
document.querySelectorAll("[data-wa]").forEach((el) => {
  if (CONFIG.whatsapp) {
    el.href = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(CONFIG.mensagemWhatsapp)}`;
    el.target = "_blank";
    el.rel = "noopener";
  }
});

// Dados de contato reais substituem os [TODO] quando existirem.
const contatos = {
  whatsapp: CONFIG.whatsapp && `+${CONFIG.whatsapp}`,
  telefone: CONFIG.telefone,
  email: CONFIG.email,
  instagram: CONFIG.instagram && CONFIG.instagram.replace(/^https?:\/\/(www\.)?/, ""),
};
document.querySelectorAll("[data-contact]").forEach((el) => {
  const valor = contatos[el.dataset.contact];
  if (!valor) return;
  el.textContent = valor;
  el.classList.remove("todo");
  const link = el.closest("a");
  if (link) {
    const k = el.dataset.contact;
    link.href = k === "email" ? `mailto:${valor}` : k === "telefone" ? `tel:${valor.replace(/\D/g, "")}` : k === "instagram" ? CONFIG.instagram : link.href;
  }
});

// Menu mobile
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".main-nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const aberto = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", aberto);
    toggle.setAttribute("aria-label", aberto ? "Fechar menu" : "Abrir menu");
  });
  nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => {
    nav.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
  }));
}

// Link ativo conforme a seção visível (só na home)
const secoes = [...document.querySelectorAll("main section[id]")];
const links = [...document.querySelectorAll(".main-nav a[href*='#']")];
if (secoes.length && "IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      links.forEach((l) => l.classList.toggle("ativo", l.getAttribute("href").endsWith(`#${e.target.id}`)));
    });
  }, { rootMargin: "-40% 0px -55% 0px" });
  secoes.forEach((s) => io.observe(s));
}

// Animação de entrada
const reveals = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const ro = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("in"); ro.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  reveals.forEach((r) => ro.observe(r));
} else {
  reveals.forEach((r) => r.classList.add("in"));
}

// Formulário
const form = document.getElementById("form-contato");
if (form) {
  const status = form.querySelector(".form-status");
  const mostrar = (msg, ok) => {
    status.textContent = msg;
    status.className = `form-status show${ok ? " ok" : ""}`;
  };
  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    if (!form.reportValidity()) return;
    if (!CONFIG.formEndpoint) {
      mostrar("[TODO] O envio do formulário ainda não está configurado. Enquanto isso, fale conosco pelo WhatsApp.", false);
      return;
    }
    try {
      const res = await fetch(CONFIG.formEndpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      form.reset();
      mostrar("Mensagem enviada! Retornaremos em breve.", true);
    } catch {
      mostrar("Não foi possível enviar agora. Tente novamente ou fale pelo WhatsApp.", false);
    }
  });
}
