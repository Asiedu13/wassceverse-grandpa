let lastUrl = location.href;
let num = 1;
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
        firstName: formDataSerialized.firstName,
        lastName: formDataSerialized.lastName,
        otherNames: formDataSerialized.otherNames,
        DOB: formDataSerialized.DOB,
        gender: formDataSerialized.gender,
        school: formDataSerialized.school,
        beceIndex: formDataSerialized.beceIndex,
        yearCompleted: formDataSerialized.yearCompleted,
        course: formDataSerialized.course,
        electives: formDataSerialized.electives,
        parentContact: formDataSerialized.parentContact,




      };

      conversationalForm.addRobotChatResponse(
        "Click 'verify details' to confirm your data"
      );

      localStorage.setItem("chatData", JSON.stringify(det));
      verifyBtn = document.querySelector(".verification");
      console.log( num )
      
      verifyBtn.addEventListener( 'click', (num=1) => num <= 1 ? onConfirmation( conversationalForm, confirmationElem ) : store() )
      
      
      
    },
  });
}
