const banners = document.querySelectorAll('.banner');
let bannerIndex = 0;
let rotationInterval;
let isPageFocused = true; // Предполагается, что страница загружена с фокусом

// Функция для отображения конкретного баннера
function showBanner(index) {
    banners.forEach(banner => banner.style.display = 'none');
    banners[index].style.display = 'block';
}

// Функция для автоматической смены баннеров
function startRotation() {
    rotationInterval = setInterval(() => {
        if (isPageFocused) {
            bannerIndex = (bannerIndex + 1) % banners.length;
            showBanner(bannerIndex);
        }
    }, 5000); // Интервал смены баннеров - 5000 миллисекунд (5 секунд)
}

// Остановка автоматической смены баннеров
function stopRotation() {
    clearInterval(rotationInterval);
}

// Проверка фокуса страницы
window.onblur = () => {
    isPageFocused = false;
    stopRotation();
};

window.onfocus = () => {
    isPageFocused = true;
    startRotation();
};

// Начало ротации баннеров при загрузке страницы
startRotation();
