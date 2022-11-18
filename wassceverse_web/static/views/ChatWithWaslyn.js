import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
  constructor() {
    super();
    this.setTitle("Chatting...");
  }

  async getHTML() {
    return `
        <div id='question-time'>
        <section id="might-interest-tips">
            <article>
              <h3>Tip!</h3>
              <p>
                To revert mistakes, click on the upward triangle icon next to
                your reply.
              </p>
            </article>
          </section>

        <form id="my-form-element">
             <datalist id="classes">
              <option
                value="3 SCIENCE 1"
              ></option>
              <option value="3 SCIENCE 2"></option>
              <option value="3 SCIENCE 3"></option>
              <option value="3 SCIENCE 4"></option>
              <option value="3 SCIENCE "></option>
              <option value="Wesley Girls Senior High School"></option>
            </datalist>

            <cf-robot-message cf-questions="Hello student!"></cf-robot-message>

           

            <fieldset cf-questions="Choose your gender">
              <input type="radio" name="gender" cf-label="Male" value="male" />

              <input
                type="radio"
                name="gender"
                ,
                cf-label="Female"
                value="female"
              />
            </fieldset>
            <input
              type="text"
              name="date_of_birth"
              title="Date of Birth"
              cf-input-placeholder="DD/MM/YYYY"
              cf-questions="Birth date? (DD/MM/YYYY)"
            />
            <!-- <input
              type="text"
              name="class"
              list="classes"
              cf-questions="Which class are you in?"
            /> -->
            <input
              type="number"
              name="index_number"
              minlength="8"
              pattern="^[0-9]*$"
              cf-questions="What is your BECE index number"
            />
            <input
              type="number"
              name="year_completed"
              minlength="4"
              pattern="^[0-9]{4}"
              cf-questions="Which year did you complete BECE?"
            />
            <fieldset cf-questions="Choose your programme or course">
              <input
                type="radio"
                name="course"
                cf-label="General Science"
                value="General Science"
              />

              <input
                type="radio"
                name="course"
                cf-label="General Arts"
                value="General Arts"
              />

              <input
                type="radio"
                name="course"
                cf-label="Business"
                value="Business"
              />

              <input
                type="radio"
                name="course"
                cf-label="Home Economics"
                value="Home Economics"
              />

              <input
                type="radio"
                name="course"
                cf-label="Visual Arts"
                value="Visual Arts"
              />

              <input
                type="radio"
                name="course"
                cf-label="Agriculture"
                value="Agriculture"
              />
            </fieldset>

            <fieldset cf-questions="Choose your elective subjects">
              <input
                type="checkbox"
                name="electives"
                cf-label="E-Math"
                value="E-Math"
              />

              <input
                type="checkbox"
                name="electives"
                cf-label="Physics"
                value="Physics"
              />

              <input
                type="checkbox"
                name="electives"
                cf-label="Chemistry"
                value="Chemistry"
              />

              <input
                type="checkbox"
                name="electives"
                cf-label="Biology"
                value="Biology"
              />

              <input
                type="checkbox"
                name="electives"
                cf-label="E-ICT"
                value="E-ICT"
              />

              <input
                type="checkbox"
                value="Business Management"
                name="electives"
                cf-label="Business Management"
              />

              <input
                type="checkbox"
                name="electives"
                cf-label="Financial Accounting"
                value="Financial Accounting"
              />

              <input
                type="checkbox"
                name="electives"
                cf-label="Government"
                value="Government"
              />
              <input type="checkbox" name="electives" cf-label="" />
            </fieldset>

            <input
              type="text"
              name="parent_contact"
              minlength="8"
              maxlength="14"
              pattern="[0-9]*$"
              cf-questions="Your parent's contact number?"
              cf-input-placeholder="+233"
            />

            <fieldset cf-questions="Do you wish to continue?">
              <input type="radio" name="continue" cf-label="Yes" value="Yes" />
            </fieldset>
          </form>

          <div id="cf-context" role="cf-context" cf-context></div>
        
        `;
  }
}

let some = `<fieldset>
            <label for="name">What's your name?</label>
            <input required cf-questions="Hi there! What's your name? 😊" type="text" class="form-control" name="name" id="name" />
          </fieldset>
        
          <fieldset>
            <label for="occupation">Occupation</label>
            <div class="radio">
              <label>
                      <input cf-questions="Great to meet you, {previous-answer}! I'm a web form, what do you do?|Awesome, {previous-answer}! And what do you do?" type="radio" name="occupation" id="occupation-1" value="developer">
                        Developer
                    </label>
            </div>
            <div class="radio">
              <label>
                      <input type="radio" name="occupation" id="occupation-2" value="designer">
                        Designer
                    </label>
            </div>
            <div class="radio">
              <label>
                <input type="radio" name="occupation" id="occupation-3" value="curious-mind">
                        Curious mind
                    </label>
            </div>
            <div class="radio">
              <label>
                        <input type="radio" name="occupation" id="occupation-2" value="lost">
                        Lost cause
                    </label>
            </div>
          </fieldset>
        
          <fieldset>
            <label for="company">Company</label>
            <input cf-questions="Which company are you with?" type="text" class="form-control" name="company" id="company">
          </fieldset>
        
          <fieldset>
            <label for="opinion">Will conversational interfaces be everywhere?</label>
            <select cf-questions="Do you think conversational forms will replace web forms in the future?" name="opinion" id="opinion" class="form-control">
              <option></option>
              <option>Definitely</option>
              <option>Maybe</option>
              <option>No</option>
            </select>
          </fieldset>
        
          <fieldset>
            <label for="email">Email</label>
            <input pattern=".+\@.+\..+" cf-error="E-mail not correct" cf-questions="If you want to stay updated on conversational interfaces from SPACE10, please give me your email." type="email" class="form-control" name="email" id="your-email">
          </fieldset>
        
          <fieldset style="display: none;">
            <label for="thats-all">Are you ready to submit the form?</label>
            <select cf-questions="Are you ready to submit the form?" name="submit-form" id="submit-form" class="form-control">
              <option></option>
              <option>Yup</option>
            </select>
          </fieldset>
        
          <fieldset style="display: none;">
            <label for="thats-all">Want to start over?</label>
            <select cf-questions="Want to start over?" name="repeat" id="repeat" class="form-control">
              <option></option>
              <option>Yes, let's go again</option>
            </select>
          </fieldset>

           <fieldset cf-questions="Do you wish to continue?">
              <input type="radio" name="continue" cf-label="Yes" value="Yes" />

            </fieldset>
          <button type="submit" class="btn btn-default">Submit</button>
        </form>
        
        <div id="cf-context" class="dark-theme" role="cf-context" cf-context></div>`;
