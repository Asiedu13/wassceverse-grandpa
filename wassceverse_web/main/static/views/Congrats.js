import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor() {
        super();
    this.setTitle("Congratulations!!!");
  }

  async getHTML() {
    return `
            <h1>AJEI!!! The boy has finished    
    
            </h1>
        `;
  }
}
