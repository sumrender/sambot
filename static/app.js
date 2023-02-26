const openButton = document.querySelector(".chatbox__button");
const chatBox = document.querySelector(".chatbox__support");
const sendButton = document.querySelector(".send__button");

state = false;
messages = [];

function toggleState(chatbox) {
  state = !state;

  // show or hides the box
  if (state) chatbox.classList.add("chatbox--active");
  else chatbox.classList.remove("chatbox--active");
}

function onSendButton(chatbox) {
  var textField = chatBox.querySelector("input");
  let text1 = textField.value;

  if (text1 === "") return;

  let msg1 = { name: "User", message: text1 };
  messages.push(msg1);

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    body: JSON.stringify({ message: text1 }),
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((r) => r.json())
    .then((r) => {
      let msg2 = { name: "Sam", message: r.data };
      messages.push(msg2);
      updateChatText(chatbox);
      textField.value = "";
    })
    .catch((error) => {
      console.log(error);
      updateChatText(chatbox);
      textField.value = "";
    });
}

function updateChatText(chatbox) {
  var html = "";
  messages
    .slice()
    .reverse()
    .forEach((item, idx) => {
      if (item.name === "Sam") {
        html +=
          '<div class="messages__item messages__item--visitor">' +
          item.message +
          "</div>";
      } else {
        html +=
          '<div class="messages__item messages__item--operator">' +
          item.message +
          "</div>";
      }
    });

  const chatmessage = chatbox.querySelector(".chatbox__messages");
  chatmessage.innerHTML = html;
}

function display() {
  openButton.addEventListener("click", () => {
    toggleState(chatBox);
  });

  sendButton.addEventListener("click", () => {
    onSendButton(chatBox);
  });

  const node = chatBox.querySelector("input");
  node.addEventListener("keyup", ({ key }) => {
    if (key === "Enter") onSendButton(chatBox);
  });
}

display();
