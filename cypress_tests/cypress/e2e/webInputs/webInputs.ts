import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";
import { webInputsPage } from "../webInputsPage";

Given("user open Submit form page", () => {
  cy.visit("/");
  cy.fixture("selectors.json").then((JSON) => {
    cy.get(JSON.webInputsPage).click()
  })
});

Then("user fill in Number, Text, Password, Date fields", () => {
  cy.typeText('input[id*="input-number"]', "12345");
  webInputsPage.inputText("QWERTY");
  webInputsPage.inputPassword("0000");
  webInputsPage.inputDate("2024-11-06");
});

When("user press button Display Inputs", () => {
  webInputsPage.elements.buttonDisplayInputs().click();
});

Then("user sees own data", () => {
  webInputsPage.elements.numberFieldOutput().should("have.text", "12345");
  webInputsPage.elements.textFieldOutput().should("have.text", "QWERTY");
  webInputsPage.elements.passwordFieldOutput().should("have.text", "0000");
  webInputsPage.elements.dateFieldOutput().should("have.text", "2024-11-06");
});

When("user press button Clear Inputs", () => {
  webInputsPage.elements.buttonClearInputs().click();
});

Then("user sees blank fields", () => {
  webInputsPage.elements.numberField().should("be.empty");
  webInputsPage.elements.textField().should("be.empty");
  webInputsPage.elements.passwordField().should("be.empty");
  webInputsPage.elements.dateField().should("be.empty");
});
