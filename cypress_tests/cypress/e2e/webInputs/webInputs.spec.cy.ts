import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";
import { webInputs } from "../webInputs";

Given('user open Submit form page', () => {
  cy.visit("/");
  cy.get("[href*='inputs']").click();
});

Then('user fill in Number, Text, Password, Date fields', () => {
  cy.typeText('input[id*="input-number"]', "12345");
  webInputs.inputText("QWERTY");
  webInputs.inputPassword("0000");
  webInputs.inputDate("2024-11-06");
});

When('user press button Display Inputs', () => {
  webInputs.elements.buttonDisplayInputs().click();
});

Then('user sees own data', () => {
  webInputs.elements.numberFieldOutput().should("have.text", "12345");
  webInputs.elements.textFieldOutput().should("have.text", "QWERTY");
  webInputs.elements.passwordFieldOutput().should("have.text", "0000");
  webInputs.elements.dateFieldOutput().should("have.text", "2024-11-06");
});

When('user press button Clear Inputs', () => {
  webInputs.elements.buttonClearInputs().click();
});

Then('user sees blank fields', () => {
  webInputs.elements.numberField().should("be.empty");
  webInputs.elements.textField().should("be.empty");
  webInputs.elements.passwordField().should("be.empty");
  webInputs.elements.dateField().should("be.empty");
});
