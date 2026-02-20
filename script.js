document.getElementById("fashionForm").addEventListener("submit", function(e) {
  e.preventDefault();

  document.getElementById("output").innerText =
    "AI Suggestion: Casual pastel top with jeans and white sneakers.";
});