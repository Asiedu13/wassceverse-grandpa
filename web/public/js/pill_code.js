/* globals pill */

// import { specifiedUser } from "./globals";

/* eslint-disable no-console */
let indicator = document.getElementById("loader");

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
    //  Get the chat element and attach username to it
    console.log(specifiedUser);

    let question =
      document.querySelector("cf-robot-message") || `<div></div>`;
    console.log(question.outerHTML);

    // Search URL for username query and set to it to question tag
    const urlParams = new URLSearchParams(location.search);
    let p_name = "";

    for (const [key, value] of urlParams) {
      console.log(key, value);
      if (key == "username") {
        p_name = value;
      } else {
        continue;
      }
    }

    //  This was the only way I could change the question being displayed since all cf elements are hiding the actual html (p) tags being displayed on the page for some reason
    question.outerHTML = `<cf-robot-message cf-questions=\"Hello ${p_name}!\" tabindex=\"-1\">Helo</cf-robot-message>`;
  },

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
