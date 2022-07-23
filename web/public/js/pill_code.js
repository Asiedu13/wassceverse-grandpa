/* globals pill */
/* eslint-disable no-console */
const indicator = document.getElementById("loader");

let timeout = 10;
pill("main", {
  onLoading() {
    if (timeout) {
      clearTimeout(timeout);
      timeout = 0;
    }
    indicator.style.display = "block";
  },
  onUnmounting(page, url, element) {
    preserveFormPlugin(element);
  },
   onReady() {
    indicator.style.display = 'none'
  },
  // onReady(page, element) {
  //   // Delay to simulate long content loading
  //   timeout = setTimeout(() => {
  //     indicator.style.visibility = "hidden";
  //   }, 1000);
  //   populateFormPlugin(element);
  // },
  onMounting() {
    console.log("updating content");
  },
  listenClickEventOn: "#main",
});

function populateFormPlugin(element) {
  const key = location.pathname;
}

function preserveFormPlugin(element) {
  const key = location.pathname;
  const fields = Array.from(
    element.querySelectorAll("input, textarea, select", "header")
  );
  if (fields.length > 0) {
    const values = fields.map((val) => {
      return {
        fieldName: val.name,
        value:
          val.type === "checkbox" || val.type === "radio"
            ? val.checked
            : val.value,
      };
    });
    localStorage.setItem(key, JSON.stringify(values));
  }
}

document.addEventListener("pill:ready", appendEventReady);
document.addEventListener("pill:mounting", appendEvent);
document.addEventListener("pill:unmounting", appendEvent);
document.addEventListener("pill:loading", appendEvent);
document.addEventListener("pill:error", appendEvent);
function appendEvent(event) {}

function appendEventReady(event) {
  console.info(event);

  // var conversationalForm = window.cf.ConversationalForm.startTheConversation( {
  //   formEl: document.querySelector(".question_time"),
  //   context: document.getElementById("cf-context"),
  //   submitCallback: function () {
  //     conversationalForm.addRobotChatResponse("Alright, you are done.");
  //   },
  // });
}
