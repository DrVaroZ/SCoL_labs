let packageData = [];

        function addPackage() {
            const senderName = document.getElementById("senderName").value;
            const receiverName = document.getElementById("receiverName").value;
            const weight = parseFloat(document.getElementById("weight").value);
            const day = parseInt(document.getElementById("day").value);
            const month = parseInt(document.getElementById("month").value);
            const year = parseInt(document.getElementById("year").value);

            packageData.push({
                sender: senderName,
                receiver: receiverName,
                weight: weight,
                day: day,
                month: month,
                year: year,
            });

            alert("Посылка добавлена!");
        }

        function findReceivingMultiplePackages() {
            const currentMonth = new Date().getMonth() + 1; // Текущий месяц

            const receivers = {};
            packageData.forEach((package) => {
                if (package.month === currentMonth && package.year === new Date().getFullYear()) {
                    if (!receivers[package.receiver]) {
                        receivers[package.receiver] = {
                            totalWeight: package.weight,
                            count: 1,
                        };
                    } else {
                        receivers[package.receiver].totalWeight += package.weight;
                        receivers[package.receiver].count++;
                    }
                }
            });

            const outputTable = document.getElementById("outputResult");
            outputTable.innerHTML = "";

            Object.keys(receivers).forEach((receiver) => {
                if (receivers[receiver].count > 1) {
                    const row = document.createElement("tr");
                    row.innerHTML = `<td>${receiver}</td><td>${receivers[receiver].totalWeight}</td>`;
                    outputTable.appendChild(row);
                }
            });
        }