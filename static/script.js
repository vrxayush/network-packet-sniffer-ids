async function fetchPackets() {
    try {
        const res = await fetch('/packets');
        const data = await res.json();

        let table = document.getElementById("data");
        table.innerHTML = "";

        data.forEach(p => {
            let row = `<tr style="color:${p[5] ? 'red' : 'black'}">
                <td>${p[1]}</td>
                <td>${p[2]}</td>
                <td>${p[3]}</td>
                <td>${p[4]}</td>
                <td>${p[5] ? p[5] : ""}</td>
            </tr>`;
            table.innerHTML += row;
        });

    } catch (err) {
        console.error("Error fetching packets:", err);
    }
}

setInterval(fetchPackets, 2000);
