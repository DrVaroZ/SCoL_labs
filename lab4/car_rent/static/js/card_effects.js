let rotatingCards = {};

function startRotate(element) {
    rotatingCards[element.id] = true;
}

function stopRotate(element) {
    rotatingCards[element.id] = false;
    element.style.transform = 'rotate(0deg)';
}

function rotate(element, event) {
    if (rotatingCards[element.id]) {
        const boundingRect = element.getBoundingClientRect();
        const cardCenterX = boundingRect.left + boundingRect.width / 2;
        const cardCenterY = boundingRect.top + boundingRect.height / 2;
        const angleX = -(event.clientY - cardCenterY) * 0.1;
        const angleY = (event.clientX - cardCenterX) * 0.1;
        element.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg)`;
    }
}
