import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";
import { loginPage } from "../loginPage";

Given(/^user open Login Portal$/, () => {
  cy.visit("https://webdriveruniversity.com/Login-Portal/index.html?");
});

Then(`user sees success {string}`, (expectedAlertText: string) => {
  cy.on("window:alert", (txt) => {
    expect(txt).to.contains(expectedAlertText);
  });
});

Then(`user sees unsuccess message`, () => {
  cy.on("window:alert", (txt) => {
    expect(txt).to.contains("validation failed");
  });
});

When(
  `user input {string} and {string} in login form and submit form`,
  (username: string, password: string) => {
    cy.get('input[type="text"]')
      .invoke("attr", "placeholder")
      .should("be.a", "string");
    cy.get('input[type="text"]').type(username);
    cy.get('input[type="password"]')
      .invoke("attr", "placeholder")
      .should("be.a", "string");
    cy.get('input[type="password"]').type(password);
    cy.get('button[id="login-button"]').contains("Login").click();
  }
);
