// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    let slides = document.querySelectorAll('.slide');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.transform = `translateX(${100 * (i - index)}%)`;
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }
    

    setInterval(nextSlide, 3000);
});

// Ejemplo de script personalizado
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página cargada y lista!');
});

