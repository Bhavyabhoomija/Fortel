window.onload = function () {
    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="chat-bubble bot"><strong>Bot:</strong> Hello, I am a Weather Assistant. How can I help you?</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  
    // Add an event listener for the "Enter" key on the input field
    document.getElementById("user-input").addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        sendMessage();
      }
    });
  };
  
  function sendMessage() {
    let userInputElement = document.getElementById("user-input");
    let userInput = userInputElement.value.trim(); // Trim spaces
    let chatBox = document.getElementById("chat-box");
  
    if (userInput === "") return;
  
    // Display user message
    chatBox.innerHTML += `<div class="chat-bubble user"><strong>You:</strong> ${userInput}</div>`;
    userInputElement.value = ""; // Clear input field
    chatBox.scrollTop = chatBox.scrollHeight;
  
    // Send message to Django backend
    fetch("/chat/", {  // Ensure this URL matches your Django urlpatterns
        method: "POST",
        body: JSON.stringify({ "message": userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            chatBox.innerHTML += `<div class="chat-bubble bot"><strong>Bot:</strong> Error: ${data.error}</div>`;
        } else {
            // Display bot response first
            chatBox.innerHTML += `<div class="chat-bubble bot"><strong>Bot:</strong> ${data.response}</div>`;
            
            // Scroll to bottom
            chatBox.scrollTop = chatBox.scrollHeight;
  
            // Play the audio response (if available)
            if (data.audio) {
                let audio = new Audio(data.audio);
                audio.play();
            }
        }
    })
    .catch(error => {
        chatBox.innerHTML += `<div class="chat-bubble bot"><strong>Bot:</strong> Error: Failed to connect to server.</div>`;
    });
  }
  