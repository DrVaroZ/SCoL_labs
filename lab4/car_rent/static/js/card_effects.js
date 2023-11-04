// Object to store the state of rotating cards
let rotatingCards = {};

function startRotate(element) {
    rotatingCards[element.id] = true;
}

function stopRotate(element) {
    rotatingCards[element.id] = false;
    element.style.transform = 'rotate(0deg)';
}

// Function to rotate a card based on cursor movement
function rotate(element, event) {
    // Check if the card is in a rotating state
    if (rotatingCards[element.id]) {
        // Get the center coordinates of the card
        const boundingRect = element.getBoundingClientRect();
        const cardCenterX = boundingRect.left + boundingRect.width / 2;
        const cardCenterY = boundingRect.top + boundingRect.height / 2;

        // Calculate the angle based on cursor position relative to the card center
        const angleX = -(event.clientY - cardCenterY) * 0.1;
        const angleY = (event.clientX - cardCenterX) * 0.1;

        // Apply the rotation transformation to the card
        element.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg)`;
    }
}
