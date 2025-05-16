document.addEventListener("DOMContentLoaded", () => {
  fetch("data.json")
    .then(res => {
      if (!res.ok) throw new Error(`HTTP ${res.status} - ${res.statusText}`);
      return res.json();
    })
    .then(data => {
      const container = document.getElementById("destaques-container");
      container.innerHTML = ""; // limpar se já houver algo

      data.forEach(peca => {
        const div = document.createElement("div");
        div.className = "highlight";
        div.innerHTML = `
          <img src="${peca.imagem}" alt="${peca.nome}">
          <p><strong>${peca.nome}</strong></p>
          <p>${peca.descricao}</p>
          <p><strong>Preço:</strong> ${peca.preco}</p>
          <a href="${peca.link}" target="_blank">Ver Anúncio</a>
        `;
        container.appendChild(div);
      });
    })
    .catch(err => {
      console.error("Erro ao carregar peças:", err.message);
      const container = document.getElementById("destaques-container");
      container.innerHTML = `<p style="color:red;">Erro ao carregar peças. Verifica o ficheiro data.json.</p>`;
    });
});
