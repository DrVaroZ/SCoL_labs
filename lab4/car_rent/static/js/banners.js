// JavaScript
const banners = document.querySelectorAll('.banner');
let bannerIndex = 0;
let rotationInterval;

// Function to rotate through banners and display one while hiding the rest
function rotateBanners() {
  // Hide all banners
  banners.forEach(banner => banner.style.display = 'none');
  // Get the next banner to display
  bannerIndex = (bannerIndex + 1) % banners.length;
  // Show the next banner
  banners[bannerIndex].style.display = 'block';
}

function startRotation() {
  // Get the rotation interval value entered by the user and convert it to milliseconds
  const rotationIntervalInput = document.getElementById('rotationInterval');
  const interval = parseInt(rotationIntervalInput.value) * 1000;

  // Start rotation only if it's not already running
  if (!rotationInterval) {
    rotationInterval = setInterval(rotateBanners, interval);
  }
}

function stopRotation() {
  // Clear the rotation interval if it's running
  if (rotationInterval) {
    clearInterval(rotationInterval);
    rotationInterval = null;
  }
}

// Event listeners for 'start' and 'stop' rotation buttons
document.getElementById('startRotation').addEventListener('click', startRotation);
document.getElementById('stopRotation').addEventListener('click', stopRotation);

// Event listener for page visibility change
document.addEventListener('visibilitychange', function () {
  if (document.hidden) {
    stopRotation();
  } else {
    startRotation();
  }
});

// Initially start the rotation
startRotation();
