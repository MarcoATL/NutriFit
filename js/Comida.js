const Platillos = [
    { name: "Pollo rostizado", image: "./img/comida-1.jpg" },
    { name: "Pozole", image: "./img/comida-2.jpg" },
    { name: "Pollo empanizado", image: "./img/comida-3.png" },
    { name: "Ensalada griega", image: "./img/comida-4.jpg" },
    { name: "Tacos al pastor", image: "./img/comida-5.jpg" },
    { name: "Tostadas de tinga", image: "./img/comida-6.jpg" },
    { name: "Enchiladas rojas", image: "./img/comida-7.jpg" },
    { name: "Sopes", image: "./img/comida-8.jpg" },
    { name: "Pambazo de chorizo con papa", image: "./img/comida-9.jpg" },
  ];  

//Platillos dinamicos
const cardContainer = document.querySelector(".comida:last-child");

Platillos.forEach((card) => {
  const cardHTML = `
    <div class="col-md-4 col-sm-4">
        <div class="card dish-card" data-name="${card.name}">
            <img src="${card.image}" alt="Imgane Comida" class="card-img-top img-platillo">
            <div class="card-body">
            <h5 class="card-title">${card.name}</h5>
            <a href="#" class="btn ver-receta">Ver receta</a>
            </div>
        </div>
    </div>
  `;
  cardContainer.insertAdjacentHTML("beforeend", cardHTML);
});

//Buscador
const searchInput = document.getElementById('searchInput');
const dishCards = document.querySelectorAll('.dish-card');

searchInput.addEventListener('input', function() {
    const searchTerm = searchInput.value.toLowerCase();

    dishCards.forEach(function(card) {
        const dishName = card.dataset.name.toLowerCase();

        if (dishName.includes(searchTerm)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
});