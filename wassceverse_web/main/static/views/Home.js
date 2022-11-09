import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
  constructor() {
    super();
    this.getTitle("MainPage");
  }

  async getHTML() {
      axios.get( "/api/schools" ).then( ( res ) => {
          // -------- Get schools data --------
          schools = res.data;
          console.log( res.data );
      } )
    return `
    <main id="main">
      <section id="content">
        <header class="content-header">
          <h2>Select your school</h2>
        </header>
        <section id="school_selector">
          <!-- The search bar goes here -->
          <div class="search-bar">
            <p>I am a</p>
            <input type="text" id="search" oninput="inputChange(this)" />
            <p>student</p>
          </div>
          <div class="results">
            <!-- Search result descriptions -->
            <div id="search_desc">
              <span>Schools found: </span>
              <span class="search_data_count">1</span>
            </div>

            <!-- Actual Search results -->
            <div id="search_results">
              <!-- The results appear here from main.js -->
            </div>
          </div>
        </section>
      </section>
    </main>
      `;
  }
}
