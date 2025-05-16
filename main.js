document.addEventListener("DOMContentLoaded", () => {
  fetch('pecas.json')
    .then(res => res.json())
    .then(data => carregarDestaques(data))
    .catch(err => console.error("Erro ao carregar peças:", err));
});

function carregarDestaques(pecas) {
  const secao = document.querySelector(".highlights");
  const container = document.createElement("div");

  pecas.forEach(peca => {
    const div = document.createElement("div");
    div.className = "highlight card";
    div.innerHTML = `
      <img src="${peca.imagem}" alt="${peca.nome}">
      <p><strong>${peca.nome}</strong></p>
      <p>${peca.descricao}</p>
      <p><strong>Preço:</strong> ${peca.preco}</p>
      <a href="${peca.link}" target="_blank">Ver Anúncio</a>
    `;
    container.appendChild(div);
  });

  secao.innerHTML = "<h3>Destaques</h3>";
  secao.appendChild(container);
}
