function calculateAverage() {
    const name = document.getElementById('studentName').value.trim();
    const g1 = parseFloat(document.getElementById('grade1').value);
    const g2 = parseFloat(document.getElementById('grade2').value);
    const g3 = parseFloat(document.getElementById('grade3').value);

    if (!name || isNaN(g1) || isNaN(g2) || isNaN(g3)) {
        alert("Fill in all the fields.");
        return;
    }

    if ([g1, g2, g3].some(g => g < 0 || g > 10)) {
        alert("Grades must be between 0 and 10.");
        return;
    }

    const avg = (g1 + g2 + g3) / 3;

    let status = "failed";
    let label = "Failed";

    if (avg >= 7) {
        status = "approved";
        label = "Approved";
    } else if (avg >= 5) {
        status = "remedial";
        label = "Remedial";
    }

    const card = document.getElementById('resultCard');
    const badge = document.getElementById('statusBadge');

    card.className = "result-card " + status + "-card";
    badge.className = "badge " + status + "-badge";
    badge.textContent = label;

    document.getElementById('resultName').textContent = name;
    document.getElementById('resultAverage').textContent = avg.toFixed(2);
}
