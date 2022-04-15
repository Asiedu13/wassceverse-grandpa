lastUrl = location.href;

new MutationObserver(() => {
  const url = location.href;
  if (url !== lastUrl) {
    lastUrl = url;
  }
}).observe(document, { subtree: true, childList: true });

function onConfirmation(item, replacement) {
  console.log(verifyBtn);
  chatData = JSON.parse(localStorage.getItem("chatData"));
  console.log(chatData);

  setInputValuesToChatData(chatData);
  item.remove();
  replacement.style.display = "block";
}

function setInputValuesToChatData(chatData) {
  console.log(chatData);
  // Get elements
  confirmationInputs = document.querySelectorAll(".confirmationElem");
  console.log(confirmationInputs);

  for (let i = 0; i < confirmationInputs.length; i++) {
    console.log(confirmationInputs[i]);
    let name = confirmationInputs[i].getAttribute("name");

    console.log(name);
    if (name in chatData) {
      confirmationInputs[i].setAttribute("value", `${chatData[name]}`);
      console.log(confirmationInputs[i]);
      console.log("Name in chatData!");
    } else {
      console.log("Name not found");
    }
    console.log(num)
    // console.log(confirmationInputs)
  }
  num = num + 1;
}

function store(item, replacement) {
  chatData = JSON.parse(localStorage.getItem("chatData"));
  console.log(chatData);

  setInputValuesToChatData(chatData);
  item.remove();

  replacement.style.display = "block";
  console.log( "Store function..." )
  chatData = JSON.parse(localStorage.getItem("chatData"));

  axios
    .post("/post", chatData)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
}
