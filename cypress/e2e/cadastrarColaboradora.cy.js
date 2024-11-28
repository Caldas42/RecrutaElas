describe('Cadastrando colaboradora', () => {
    it('cenario1', () => {
        cy.visit('/delete_cypress/');
        cy.get('[href="/login/"] > h1').click();
        cy.get('#username').type('cypress');
        cy.get('#password').type('abc123');
        cy.get('.button').click();
        cy.get('[href="/aplicacao/home_cadastros/"] > .card').click();
        cy.get('.novo-cadastro-card').click()
    })

    it('cenario2', () => {
        cy.visit('/');
        cy.get('[href="/login/"] > h1').click();
        cy.get('#username').type('cypress');
        cy.get('#password').type('abc123');
        cy.get('.button').click();
        cy.get('[href="/aplicacao/home_cadastros/"] > .card').click();
        cy.get('.novo-cadastro-card').click()
    })

    it('cenario3', () => {
        cy.visit('/');
        cy.get('[href="/login/"] > h1').click();
        cy.get('#username').type('cypress');
        cy.get('#password').type('abc123');
        cy.get('.button').click();
        cy.get('[href="/aplicacao/home_cadastros/"] > .card').click();
        cy.get('.novo-cadastro-card').click()
    })
})