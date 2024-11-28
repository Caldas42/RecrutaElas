describe('Criando pastas de colaboradoras', () => {
    it('Criando uma pasta de colaboradoras', () => {
        cy.visit('/delete_cypress/')
        cy.get('.button').click()
        cy.get('[href="/login/"]').click()
        cy.get('p > a').click()
        cy.get('#username').type('cypress')
        cy.get('#password').type('abc123')
        cy.get('#password_confirm').type('abc123')
        cy.get('.button').click()
        cy.get('#username').type('cypress')
        cy.get('#password').type('abc123')
        cy.get('.button').click()
        cy.get('[href="/aplicacao/home_cadastros/"] > .card').click()
        cy.get('[href="/aplicacao/gerenciar_pastas/"] > h1').click()
        cy.get('.pasta-icone2').click()
        cy.get('#nomePasta').type('Costureiras')
        cy.get('.btn-submit').click()
        cy.get('p').invoke('text').should('have.string', "Costureiras")
    })

    it('Criando uma pasta com colaboradora', () => {
        cy.visit('/delete_cypress/')
        cy.get('.button').click()
        cy.get('[href="/login/"]').click()
        cy.get('p > a').click()
        cy.get('#username').type('cypress')
        cy.get('#password').type('abc123')
        cy.get('#password_confirm').type('abc123')
        cy.get('.button').click()
        cy.get('#username').type('cypress')
        cy.get('#password').type('abc123')
        cy.get('.button').click()
        cy.get('[href="/aplicacao/home_cadastros/"] > .card').click()
        cy.get('h2').click()
        cy.get('#textFormNome').type('Andressa')
        cy.get('#numberFormIdade').type('30')
        cy.get('#numberFormCpf').type('65390182170')
        cy.get('#numberFormCelular').type('81994350921')
        cy.get('#textFormEmail').type('andressa@gmail.com')
        cy.get('#numberFormCep').type('51089472')
        cy.get('#textFormCidade').type('Recife')
        cy.get('#textFormBairro').type('Boa Viagem')
        cy.get('#textFormRua').type('Rua conde')
        cy.get('#numberFormNumero').type('456')
        cy.get('#textFormComplemento').type('bloco 1 apt 201')
        cy.get('#textFormEscolaridade').type('Ensino médio completo')
        cy.get('#textFormExperiencia').type('nunca trabalhei')
        cy.get('#textFormDisponibilidade').type('tempo integral')
        cy.get('#textFormInteresse').type('não tenho')
        cy.get('[for="selectSkillCostura"]').click()
        cy.get('.button').click()
        cy.get('.mensagem').invoke('text').should('have.string', "Cadastro adicionado com sucesso!")
    })

    it('Esquecendo de colocar o nome quando for criar a pasta', () => {
        cy.visit('/delete_cypress/')
        cy.get('.button').click()
        cy.get('[href="/login/"]').click()
        cy.get('p > a').click()
        cy.get('#username').type('cypress')
        cy.get('#password').type('abc123')
        cy.get('#password_confirm').type('abc123')
        cy.get('.button').click()
        cy.get('#username').type('cypress')
        cy.get('#password').type('abc123')
        cy.get('.button').click()
    })
})