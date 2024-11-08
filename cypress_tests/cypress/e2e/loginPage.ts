export class LoginPage {
  elements = {
    usernameInput: () => cy.get("#username"),
    passwordInput: () => cy.get("#password"),
    usernameLabel: () => cy.get('label[for="username"]'),
    passwordLabel: () => cy.get('label[for="password"]'),
    submitButton: () => cy.get('button[type="submit"]'),
    successMessage:() => cy.get('#flash'),
    logOutButton: () => cy.get('.btn-danger'),
    errorMessage:() => cy.get('#flash')
  };

  typeInUsername() {
    cy.fixture("creds.json").then((JSON) => {
      const username: string = JSON.userName;
      if (username) {
        this.elements.usernameInput().type(username);
      }
    });
    return this;
  }

  typeInPassword() {
    cy.fixture("creds.json").then((JSON) => {
      const password: string = JSON.password;
      if (password) {
        this.elements.passwordInput().type(password);
      }
    });
    return this;
  }

  verifyLoginPage() {
    this.elements.usernameLabel().should("be.visible");
    this.elements.usernameInput().should("be.visible");
    this.elements.passwordLabel().should("be.visible");
    this.elements.passwordInput().should("be.visible");
    this.elements.submitButton().should("be.visible");
  }

  verifyPageUrl(url: string){
    cy.intercept(`https://practice.expandtesting.com/${url}`)
  }
}
export const loginPage = new LoginPage();
