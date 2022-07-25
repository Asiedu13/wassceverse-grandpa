const { response } = require("express");

let lastUrl = location.href;
let num = 1;

window.onload = async () => {
  let res = await axios.get("/api/schools");
  schools = res.data
  console.log( res.data );

  schools.forEach((school) => {
    let html_to_be_added = ` <article class="school">
    <div class="sch_img">
    <img src="${school.logo}" alt="Image not found" onerror="this.onerror=null;this.src='./media/image_not_found.png';" />
    </div>
    <div class="sch_desc">
    <h4 class="sch_name">${school.school_name}</h4>
    <span>Location: </span><span>${school.location}</span>
    </div>
    </article>
    `;
  });
};

new MutationObserver(() => {
  const url = location.href;
  if (url !== lastUrl) {
    lastUrl = url;
    onUrlChange();
  }
}).observe(document, { subtree: true, childList: true });

function onUrlChange() {
  let confirmationElem = document.getElementById("confirmation_elems");
  confirmationElem.style.display = "none";

  var conversationalForm = window.cf.ConversationalForm.startTheConversation({
    formEl: document.querySelector("form"),
    context: document.getElementById("cf-context"),
    showProgressBar: true,
    //  flowStepCallback: function(dto, success, error){

    //     if(dto.tag.id == "firstname"){
    //         if(dto.tag.value.toLowerCase() === "sherlock"){
    //             return success();
    //         }else{
    //             return error();
    //         }
    //         //conversationalForm.stop("Stopping form, but added value");
    //     }else if(dto.tag.name == "gender"){
    //         if(dto.tag.value[0] === "male"){
    //             return success();
    //         }else{
    //             return error();
    //         }
    //     }

    //     return success();
    // }

    submitCallback: function () {
      conversationalForm.addRobotChatResponse(
        "Your data is being processed..."
      );

      // Display form data
      var formData = conversationalForm.getFormData();
      var formDataSerialized = conversationalForm.getFormData(true);
      console.log("Formdata:", formData);
      console.log("Formdata, serialized:", formDataSerialized);

      let det = {
        first_name: formDataSerialized.first_name,
        surname: formDataSerialized.surname,
        other_names: formDataSerialized.other_names,
        date_of_birth: formDataSerialized.date_of_birth,
        gender: formDataSerialized.gender,
        school: formDataSerialized.school,
        index_number: formDataSerialized.index_number,
        year_completed: formDataSerialized.year_completed,
        course: formDataSerialized.course,
        electives: formDataSerialized.electives,
        parent_contact: formDataSerialized.parent_contact,
      };

      conversationalForm.addRobotChatResponse(
        "Click 'verify details' to confirm your data"
      );

      localStorage.setItem("chatData", JSON.stringify(det));
      verifyBtn = document.querySelector(".verification");
      console.log(num);

      verifyBtn.addEventListener("click", () =>
        store(conversationalForm, confirmationElem)
      );

      onConfirmation(conversationalForm, confirmationElem);
    },
  });
}
