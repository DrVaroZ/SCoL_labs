function createStars() {
    const reviews = document.querySelectorAll('.review');
    reviews.forEach(review => {
        const mark = parseInt(review.querySelector('#mark').textContent.trim());
        const starsContainer = review.querySelector('#stars');

        starsContainer.innerHTML = ''; // Clear the stars container

        for (let i = 0; i < mark; i++) {
            const star = document.createElement('span');
            star.innerHTML = '★';
            starsContainer.appendChild(star);
        }
    });
}