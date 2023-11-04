let packageData = []; // Array to store package information

// Function to add a package to the packageData array
function addPackage() {
    // Get data from form inputs
    const senderName = document.getElementById("senderName").value;
    const receiverName = document.getElementById("receiverName").value;
    const weight = parseFloat(document.getElementById("weight").value);
    const day = parseInt(document.getElementById("day").value);
    const month = parseInt(document.getElementById("month").value);
    const year = parseInt(document.getElementById("year").value);

    // Add package data to the packageData array
    packageData.push({
        sender: senderName,
        receiver: receiverName,
        weight: weight,
        day: day,
        month: month,
        year: year,
    });

    alert("Посылка добавлена!"); // Alert to confirm package addition
}

// Function to find receivers who received multiple packages in the current month and year
function findReceivingMultiplePackages() {
    const currentMonth = new Date().getMonth() + 1; // Current month
    const receivers = {};

    // Iterate through packageData to count packages received by each receiver in the current month and year
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

    // Display receivers who received more than one package in the current month and year in a table
    Object.keys(receivers).forEach((receiver) => {
        if (receivers[receiver].count > 1) {
            const row = document.createElement("tr");
            row.innerHTML = `<td>${receiver}</td><td>${receivers[receiver].totalWeight}</td>`;
            outputTable.appendChild(row);
        }
    });
}
