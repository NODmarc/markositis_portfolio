export class WebInputsPage {
  elements = {
    // Input fields
    numberField: () => cy.get('input[id*="input-number"]'),
    textField: () => cy.get('input[id*="input-text"]'),
    passwordField: () => cy.get('input[id*="input-password"]'),
    dateField: () => cy.get('input[id*="input-date"]'),

    // Output fields
    numberFieldOutput: () => cy.get('#output-number'),
    textFieldOutput: () => cy.get('[id*="output-text"]'),
    passwordFieldOutput: () => cy.get('[id*="output-password"]'),
    dateFieldOutput: () => cy.get('[id*="output-date"]'),

    // Buttons
    buttonDisplayInputs: () => cy.get('button[id*="btn-display-inputs"]'),
    buttonClearInputs: () => cy.get('button[id*="btn-clear-inputs"]'),
  };

  inputNumber(num: string) {
    this.elements.numberField().should('be.visible').type(num);
  }

  inputText(name: string) {
    this.elements.textField().should('be.visible').type(name);
  }

  inputPassword(name: string) {
    this.elements.passwordField().should('be.visible').type(name);
  }

  inputDate(name: string) {
    this.elements.dateField().should('be.visible').type(name);
  }

}
export const webInputsPage = new WebInputsPage();
