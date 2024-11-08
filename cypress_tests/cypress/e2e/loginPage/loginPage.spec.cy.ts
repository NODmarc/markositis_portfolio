import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";
import { loginPage } from "../loginPage";

Given("user open Test Login Page", () => {
  cy.visit("/");
  cy.fixture("selectors.json").then((JSON) => {
    cy.get(JSON.loginPage).click();
  });
});

When("user input username and password in login form and submit form", () => {
  loginPage.verifyLoginPage();
  loginPage.typeInUsername();
  loginPage.typeInPassword();
  loginPage.elements.submitButton().click();
});

Then("user sees success message and secure area page link", () => {
  loginPage.elements.successMessage().should("be.visible");
  loginPage.verifyPageUrl("secure");
});

When(/^user press Logout$/, () => {
  loginPage.elements.logOutButton().should("be.visible").click();
});

Then(/^sees Login page form$/, () => {
  loginPage.verifyLoginPage();
});

When(
  "user input invalid {string} and {string} and submit form",
  (username: string, password: string) => {
    loginPage.elements.usernameInput().type(username);
    loginPage.elements.passwordInput().type(password);
    loginPage.elements.submitButton().click();
  }
);

Then(/^user error message$/, () => {
  loginPage.elements.errorMessage().should("be.visible");
});
