let prevScrollPosition = 0;

window.addEventListener('scroll', () => {
    const images = document.querySelectorAll('.scroll-image');
    const bottomScrollPosition = document.body.scrollHeight - window.innerHeight;
    const scrollPosition = window.scrollY;
    const screenHeight = window.innerHeight;

    images.forEach(image => {
        const imagePosition = image.offsetTop;

        if (scrollPosition > imagePosition - screenHeight * 0.75 && scrollPosition < bottomScrollPosition) {
            image.style.transform = `translateX(${scrollPosition - imagePosition + screenHeight * 0.75}px)`;
        } else if (scrollPosition <= imagePosition - screenHeight * 0.75) {
            image.style.transform = 'translateX(0)';
        } else if (scrollPosition >= bottomScrollPosition) {
            image.style.transform = `translateX(${bottomScrollPosition - imagePosition + screenHeight * 0.75}px)`;
        }
    });

    // Detect scrolling direction
    if (scrollPosition > prevScrollPosition) {
        // Scrolling down
    } else {
        // Scrolling up
        if (scrollPosition === 0) {
            images.forEach(image => {
                image.style.transform = 'translateX(0)';
            });
        }
    }

    prevScrollPosition = scrollPosition;
});
