let prevScrollPosition = 0; // Variable to store the previous scroll position

window.addEventListener('scroll', () => {
    const images = document.querySelectorAll('.scroll-image'); // Selects all elements with the class 'scroll-image'
    const bottomScrollPosition = document.body.scrollHeight - window.innerHeight; // Position of bottom scroll
    const scrollPosition = window.scrollY; // Current scroll position
    const screenHeight = window.innerHeight; // Height of the window

    // Loop through each image
    images.forEach(image => {
        const imagePosition = image.offsetTop; // Offset of the image from the top of the document

        // Adjust image position based on scroll
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
            // If scrolled to the top, reset the image positions
            images.forEach(image => {
                image.style.transform = 'translateX(0)';
            });
        }
    }

    prevScrollPosition = scrollPosition; // Store current scroll position for next comparison
});
