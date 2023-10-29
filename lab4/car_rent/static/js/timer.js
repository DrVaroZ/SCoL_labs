// Функция для запуска отсчета
function startCountdown() {
    let currentTime = new Date().getTime();

    // Если время в локальном хранилище отсутствует, устанавливаем текущее время
    if (!localStorage.getItem('startTime')) {
        localStorage.setItem('startTime', currentTime);
    } else {
        // Получаем сохраненное время начала отсчета
        let storedTime = localStorage.getItem('startTime');
        let timeDifference = currentTime - storedTime;

        // Устанавливаем интервал для обновления отсчета каждую секунду
        let interval = setInterval(function () {
            let remainingTime = 3600000 - timeDifference; // 3600000 миллисекунд = 1 час

            let hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            let minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
            let seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

            // Отображаем отсчет на странице
            document.getElementById('countdown').innerHTML = `Remaining time: ${hours}h ${minutes}m ${seconds}s`;

            if (remainingTime <= 0) {
                clearInterval(interval);
                localStorage.removeItem('startTime'); // Удаляем сохраненное время после завершения отсчета
                document.getElementById('countdown').innerHTML = 'Time is up';
            } else {
                timeDifference += 1000; // Обновляем разницу времени каждую секунду
            }
        }, 1000);
    }
}

// Вызываем функцию при загрузке страницы
startCountdown();
