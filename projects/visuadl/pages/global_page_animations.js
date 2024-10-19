document.addEventListener('DOMContentLoaded', function () {
    const postIts = document.querySelectorAll('.sticky-container');  // Select all post-its

    // Scroll observer function
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.setAttribute('data-scroll', 'animate');
                entry.target.classList.add('is-visible');
            }
        });
    }, { threshold: 0.2 });

    // Scroll observer for post-it notes
    const postItObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const postIt = entry.target;
                stickPostIt(postIt); // Trigger sticking animation
            }
        });
    }, { threshold: 0.2 });

    // Attach observer to each post-it
    postIts.forEach(postIt => {
        postItObserver.observe(postIt);
    });

    // Post-It "sticking" animation with added effects
    const stickPostIt = (element) => {
        anime({
            targets: element,
            translateY: ['-200px', '0px'],
            rotate: ['-15deg', '0deg'],
            scale: [0.8, 1],
            opacity: [0, 1],
            easing: 'easeOutElastic(1, 0.5)',
            duration: 2000,
        });
    };
    
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
