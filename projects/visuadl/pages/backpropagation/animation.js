document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('.backpropagation-section');

    // Scroll observer function
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.setAttribute('data-scroll', 'animate');
                entry.target.classList.add('is-visible');
            }
        });
    }, { threshold: 0.2 });

    // Attach observer to each section
    sections.forEach(section => {
        observer.observe(section);
    });

    // Anime.js animations for placeholders
    const animatePlaceholders = () => {
        const placeholders = document.querySelectorAll('.animation-placeholder');
        placeholders.forEach((el, index) => {
            anime({
                targets: el,
                backgroundColor: ['#E0E0E0', '#FFC0D9'],
                duration: 2000,
                delay: index * 500,
                loop: true,
                direction: 'alternate',
                easing: 'easeInOutQuad'
            });
        });
    };

    animatePlaceholders();
});
