document.getElementById("feedbackForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let course = document.getElementById("course").value;
    let feedback = document.getElementById("feedback").value;

    document.getElementById("result").innerHTML = `
        <h3>Submitted Feedback</h3>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Course:</strong> ${course}</p>
        <p><strong>Feedback:</strong> ${feedback}</p>
    `;
});