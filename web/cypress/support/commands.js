/// <reference types="cypress"/>

// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
// 
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************

// Apenas comandos genéricos reutilizáveis
Cypress.Commands.add('login', (username, password) => {
  // Implementação genérica de login
});

Cypress.Commands.add('waitForLoading', () => {
  cy.get('.loading-spinner').should('not.exist');
});


// Caso de Teste 1: Acessa página inicial da Amazona
// Cypress.Commands.add('AcessarPagAmazon', ()=> {
//     cy.visit('/')
// });

// // Caso de Teste 2: Pesquisar pelo livro “AI Engineering: Building Applications with Foundation Models
// Cypress.Commands.add('PesquisaLivro', (descBook)=> {
//     cy.get('input[placeholder="Pesquisar Amazon.com.br"]')
//       .should('be.visible')
//       .clear().type(descBook);
    
//       // Ação do click no botão
//     cy.get('#nav-search-submit-button')
//       .click();
// });

// // Caso de Teste 3: Selecionar o livro correto
// Cypress.Commands.add('LivroSelecionado', ()=> {
//     cy.get('img[alt="AI Engineering: Building Applications with Foundation Models"]')
//       .should('be.visible')
//       .click();
// });

// // Caso de Teste 4: Validar detalhes do livro
// Cypress.Commands.add('DetalhesLivro', ()=> {
//     // Validar se a Edição Inglês e o Autor do Livro
//     cy.get('#bylineInfo')
//       .scrollIntoView()              // evita falso negativo de visibilidade
//       .invoke('text')
//       .then((raw) => {
//         const clean = raw
//           .normalize('NFC')
//           .replace(/\u00a0/g, ' ')   // NBSP -> espaço normal
//           .replace(/\s+/g, ' ')      // colapsa \n, \t, múltiplos espaços
//           .trim();

//         const label = clean.split('|')[0].split('por')[0].trim();

//         expect(label).to.eq('Edição Inglês');   // Vvalidando se o texto é igual
//         expect(clean).to.include('Chip Huyen'); // Validando se o texto é igual
//         expect(clean).to.include('Autor');      // Validando se o texto é igual
//     });

       // Validação que o livro é Físico
//     cy.get('li[aria-posinset="1"] .rpi-attribute-label span')
//       .should('have.text', 'Número de páginas');

//     cy.get('li[aria-posinset="1"] .rpi-attribute-value span')
//       .invoke('text')
//       .then((text) => {
//         const clean = text.normalize('NFC').replace(/\u00a0/g, ' ').trim();
//         expect(clean).to.eq('532 páginas');  
//       });
    
       // Validação que da Data da Publicação do Livre
//     cy.get('li[aria-posinset="4"] .rpi-attribute-label span')
//       .should('have.text', 'Data da publicação');

//     cy.get('li[aria-posinset="4"] .rpi-attribute-value span')
//       .invoke('text')
//       .then((text) => {
//         const clean = text.normalize('NFC').replace(/\u00a0/g, ' ').trim();
//         expect(clean).to.eq('7 janeiro 2025');
//       });
// })

// Caso de Teste 5: Adicionar o livro ao carrinho
// Cypress.Commands.add('AddCarrinho', ()=> {
//     // Adicionar o livro ao carrinho
//     cy.get('#add-to-cart-button').should('be.visible').click();
// })

// Caso de Teste 6: Validar mensagem de confirmação
// Cypress.Commands.add('MensagemConfirmacao', ()=> {
//     // Validar mensagem de confirmação
//     cy.get('h1.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
//       .invoke('text')
//       .then((text) => {
//         const clean = text.normalize('NFC').trim();
//         expect(clean).to.eq('Adicionado ao carrinho');
//     });
// })