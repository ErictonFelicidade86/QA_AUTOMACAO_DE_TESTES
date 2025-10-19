/// <reference types="cypress"/>

import amazonBookPage from '../support/page/home/AmazonBookSearchPage';
import { BOOK_DATA } from '../fixtures/bookData';

describe('Compra de Livro na Amazon', () => {
  
  beforeEach(() => {
    amazonBookPage.navigateToHome();
  });

  context('Fluxo de Compra Completo', () => {
    it('Deve pesquisar, selecionar, validar detalhes e adicionar livro ao carrinho', () => {
      amazonBookPage
        .searchForBook()
        .selectBookFromResults()
        .verifyBookDetails()
        .addBookToCart()
        .verifyCartConfirmation();
    });
  });

  context('Validação Individual', () => {
    // Verificação de busca é feita dentro do método da página
    it('Deve Pesquisar o Livro com sucesso', () => {
      amazonBookPage.searchForBook(BOOK_DATA.TITLE);
    });

    it('Deve exibir os detalhes do livro corretamente', () => {
      amazonBookPage
        .searchForBook()
        .selectBookFromResults()
        .verifyBookDetails({
          TITLE: BOOK_DATA.TITLE,
          AUTHOR: BOOK_DATA.AUTHOR,
          LANGUAGE: BOOK_DATA.LANGUAGE,
          FORMAT: BOOK_DATA.FORMAT,
          PAGES: BOOK_DATA.PAGES,
          PUBLICATION_DATE: BOOK_DATA.PUBLICATION_DATE
        });
    });
  });
});