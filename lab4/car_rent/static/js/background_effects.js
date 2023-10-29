document.body.addEventListener('mousemove', function(event) {
      const r = Math.round(255 * event.clientX / window.innerWidth);
      const g = Math.round(255 * event.clientY / window.innerHeight);
      const b = Math.round(255 * (r + g) / 510);
      document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
});