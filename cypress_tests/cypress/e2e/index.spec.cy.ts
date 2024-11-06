describe("Open Practice.com WebPage", () => {
  beforeEach("Open web page", () => {
    cy.visit("/");
  });

  it('Open "Web Inputs" section', () => {
    cy.get("[href*='inputs']").click();
  });
});
