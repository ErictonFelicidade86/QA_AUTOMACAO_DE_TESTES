class homePage {
    
    goTo() {
        cy.AcessarPagAmazon();
    }

    bookSearch() {
        cy.PesquisaLivro('AI Engineering: Building Applications with Foundation Models');
    }
    
    selectBook() {
        cy.LivroSelecionado();
    }

    bookDetails() {
        cy.DetalhesLivro();
    }
    
    addBookToCart() {
        cy.AddCarrinho();
    }

    confirmationMessage() {
        cy.MensagemConfirmacao();
    } 


} export default new homePage