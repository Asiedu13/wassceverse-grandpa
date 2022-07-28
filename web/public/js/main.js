// import { specifiedUser } from "./globals";

let lastUrl = location.href;
let num = 1;
let schools;
let userData = {
  school: "",
  index_number: "",
  first_name: "",
  surname: "",
};

window.onload = async () => {
  axios.get("/api/schools").then((res) => {
    // -------- Get schools data --------
    schools = res.data;
    console.log(res.data);

    // -------- Get parent Element ----
    let parent = document.getElementById("search_results");
    let count_display = document.querySelector(".search_data_count");

    // ------ Get the number of elements in the array ---------
    count_display.innerHTML = schools.length;
    console.log(parent);

    upDateSchoolsList(schools, parent, count_display, "article", "school");
  });
  console.log(parent);

  // ---------- Add event listeners ------
};

let main_input = document.querySelector("#search");
main_input.addEventListener("input", (e) => inputChange(e, schools));
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
    // FIXME: Remove the comments when done and this is still not necessary.
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
        first_name: userData.first_name,
        surname: userData.surname,
        other_names: formDataSerialized.other_names,
        date_of_birth: formDataSerialized.date_of_birth,
        gender: formDataSerialized.gender,
        school: userData.school,
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

function upDateSchoolsList(
  schools_list,
  parent,
  count_display,
  parentElem,
  className
) {
  // --- Check if there are child elements in the parent
  if (parent.childElementCount > 0) {
    parent.innerHTML = "";
    // Get the number of elements in the array
    count_display.innerHTML = schools_list.length;
    // Do the same thing again for the else
    schools_list.forEach((school) => {
      if (school.school_name != "") {
        let html_to_be_added = `
        
           <div class="sch_img">
              <img src="${school.school_logo}" alt="Image not found" onerror="this.onerror=null;this.src='./media/image_not_found.png';" />
          </div>
          <div class="sch_desc">
          <h4 class="sch_name">${school.school_name}</h4>
          <span>Location: </span><span>${school.location}</span>
          </div>
      `;
        var div = document.createElement(`${parentElem}`);

        div.innerHTML = html_to_be_added;
        div.setAttribute("class", `${className}`);
        div.setAttribute("onClick", `schoolSelected(this)`);
        console.log(html_to_be_added);
        parent.appendChild(div);
      }
    });
  } else {
    schools_list.forEach((school) => {
      if (school.school_name != "") {
        let html_to_be_added = `
        
           <div class="sch_img">
              <img src="${school.school_logo}" alt="Image not found" onerror="this.onerror=null;this.src='./media/image_not_found.png';" />
          </div>
          <div class="sch_desc">
          <h4 class="sch_name">${school.school_name}</h4>
          <span>Location: </span><span>${school.location}</span>
          </div>
      `;
        var div = document.createElement(`${parentElem}`);

        div.innerHTML = html_to_be_added;
        div.setAttribute("class", `${className}`);
        div.setAttribute("onClick", `schoolSelected(this)`);
        console.log(html_to_be_added);
        parent.appendChild(div);
      }
    });
  }
}

// ----------- When the search input is edited ---

function inputChange(e, schools_list) {
  let search_value = e.target.value;
  let parent = document.getElementById("search_results");
  // let search_value;
  console.log(search_value);
  let count_display = document.querySelector(".search_data_count");

  newSchoolList = schools_list.filter((school) => {
    return school.school_name
      .toLowerCase()
      .includes(search_value.toLowerCase());
  });
  console.log(newSchoolList);

  upDateSchoolsList(newSchoolList, parent, count_display, "article", "school");
}

// --------- When the user taps on a school ------

function schoolSelected(e) {
  // -- School selection code goes here...
  console.log("A school has been clicked!");
  console.log(e);
  let selected_school = e;

  // ---------- Get school name ----------
  let selectedSchoolName = e.children[1].children[0].innerText;
  console.log(selectedSchoolName);
  // ------ Set input to school name ------
  main_input.value = selectedSchoolName;

  // ------ Save school name ------
  userData.school = selectedSchoolName;
  // ------ Disable input element ---------
  main_input.setAttribute("disabled", "disabled");

  // ------ Remove search results section ------

  let resultsParent = document.querySelector(".results");
  resultsParent.remove();

  // ------ Replace search results section with other elements

  let replacementHtml = `     
            <p>and my B.E.C.E index number was </p>
            <input type="text" minlength="10" maxlength="13 id="indexNumber" onInput="updateIndexNumber(this)" placeholder="eg. 0101050901619" />  
            <button id="continueC" onClick="continueToChat()">Save</button>
  `;
  let schoolSelector = document.querySelector("#school_selector");
  let parentReplacementHtml = document.createElement("div");
  parentReplacementHtml.setAttribute("class", "index_number_input");
  parentReplacementHtml.innerHTML = replacementHtml;
  schoolSelector.appendChild(parentReplacementHtml);
}

function updateIndexNumber(e) {
  userData.index_number = e.value;
  console.log(userData);
}

async function continueToChat() {
  let schoolSelector = document.querySelector("#school_selector");

  let result = await getStudentName(userData.school, userData.index_number);
  console.log("Async working");
  console.log(result);

  // Pass data to URL or local storage
  console.log(schoolSelector);
  let continueLink = document.createElement("div");
  let username = `${userData.first_name} ${userData.surname}`;

  specifiedUser = username;
  let theLink = `
      <a id="continues" href="/pages/student_registration.html?index_number=${userData.index_number}&username=${username}">Continue</a>`;
  continueLink.innerHTML = theLink;
  schoolSelector.appendChild(continueLink);
}

// Get student name from DB
function getStudentName(school, index_number) {
  return new Promise((resolve, reject) => {
    axios
      .get(
        `/api/student/getStudent?school=${school}&index_number=${index_number}`
      )
      .then((res) => {
        console.log(res.data);
        console.log("Saving in userData object");
        userData.first_name = res.data.first_name;
        userData.surname = res.data.surname;
        console.log(userData);
        resolve(true);
      })
      .catch((err) => {
        console.error(err.message);
        reject(false);
      });
  });
}
