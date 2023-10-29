// JavaScript
const banners = document.querySelectorAll('.banner');
let bannerIndex = 0;
let rotationInterval;

function rotateBanners() {
  banners.forEach(banner => banner.style.display = 'none');
  bannerIndex = (bannerIndex + 1) % banners.length;
  banners[bannerIndex].style.display = 'block';
}

function startRotation() {
  const rotationIntervalInput = document.getElementById('rotationInterval');
  const interval = parseInt(rotationIntervalInput.value) * 1000;

  if (!rotationInterval) {
    rotationInterval = setInterval(rotateBanners, interval);
  }
}

function stopRotation() {
  if (rotationInterval) {
    clearInterval(rotationInterval);
    rotationInterval = null;
  }
}

document.getElementById('startRotation').addEventListener('click', startRotation);
document.getElementById('stopRotation').addEventListener('click', stopRotation);

document.addEventListener('visibilitychange', function () {
  if (document.hidden) {
    stopRotation();
  } else {
    startRotation();
  }
});

startRotation();
