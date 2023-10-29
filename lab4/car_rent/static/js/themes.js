function changeBackgroundColor() {
      const colors = ["#FF5733", "#33FF57", "#3366FF", "#FF33A8", "#E6FF33"];
      const randomColor = colors[Math.floor(Math.random() * colors.length)];
      document.body.style.backgroundColor = randomColor;
    }

    const colorButton = document.getElementById("colorButton");
    colorButton.addEventListener("click", changeBackgroundColor);