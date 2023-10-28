function changeFontSize(select) {
    const content = document.querySelector('.privacy-policy');
    content.style.fontSize = select.value + 'px';
}

function changeTextColor(color) {
    const content = document.querySelector('.privacy-policy');
    content.style.color = color;
}

function changeBgColor(color) {
    document.body.style.backgroundColor = color;
}
