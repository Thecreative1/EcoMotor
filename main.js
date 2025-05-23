document.addEventListener("DOMContentLoaded", () => {
  fetch('data.json')
    .then(res => res.json())
    .then(data => carregarDestaques(data))
    .catch(err => {
      console.error("Erro ao carregar peças:", err);
      const container = document.getElementById("destaques-container");
      container.innerHTML = `<p style="color:red;">Erro ao carregar peças. Verifica se o ficheiro data.json está no local certo.</p>`;
    });
});

function carregarDestaques(pecas) {
  const container = document.getElementById("destaques-container");
  container.innerHTML = ""; // limpa se já houver conteúdo

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
}
