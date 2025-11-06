
        // Script para o carrossel
    document.addEventListener('DOMContentLoaded', function() {
            const slides = document.querySelectorAll('.slide');
    const indicators = document.querySelectorAll('.indicador');
    let currentSlide = 0;

    function showSlide(n) {
        slides.forEach(slide => slide.classList.remove('active'));
                indicators.forEach(indicator => indicator.classList.remove('active'));

    currentSlide = (n + slides.length) % slides.length;

    slides[currentSlide].classList.add('active');
    indicators[currentSlide].classList.add('active');
            }

    function nextSlide() {
        showSlide(currentSlide + 1);
            }

    // Auto-advance slides
    setInterval(nextSlide, 5000);

            // Event listeners para os indicadores
            indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => showSlide(index));
            });
        });
