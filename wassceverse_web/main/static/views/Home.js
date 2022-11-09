import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
  constructor() {
    super();
    this.getTitle("MainPage");
  }

  async getHTML() {
    return `<header class="main-header">
        <section>
          <h1>WASSCEVERSE.COM</h1>
          <p> Home paragraph1</p>
        </section>
      </header>
      `;
  }
}
