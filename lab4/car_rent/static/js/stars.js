function createStars() {
    const reviews = document.querySelectorAll('.review'); // Selects all elements with the class 'review'

    reviews.forEach(review => {
        const mark = parseInt(review.querySelector('#mark').textContent.trim()); // Extracts the mark from the review
        const starsContainer = review.querySelector('#stars'); // Selects the stars container within the review

        starsContainer.innerHTML = ''; // Clears the stars container to prevent duplicating stars on multiple calls

        // Loop to create the stars based on the mark
        for (let i = 0; i < mark; i++) {
            const star = document.createElement('span'); // Create a span element for a star
            star.innerHTML = '★'; // Adds the star icon to the span
            starsContainer.appendChild(star); // Appends the star to the stars container
        }
    });
}
