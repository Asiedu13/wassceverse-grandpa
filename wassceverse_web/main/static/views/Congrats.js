import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
    this.setTitle("Congratulations!!!");
  }

  async getHTML() {
    return `
        <main id="success-main">
     
      <img src="/static/media/happy_feeling.svg" />
      <section>
        <h1>You have been registered!</h1>
        <a href="/" data-link><img src="/static/media/arrow-small-left.svg" /> Home</a>
      </section>
      
    </main>
        `;
  }
}
