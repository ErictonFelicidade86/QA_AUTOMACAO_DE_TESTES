import { BOOK_SELECTORS, SEARCH_SELECTORS, CART_SELECTORS } from '../../selectors/bookSelectors';
import { BOOK_DATA } from '../../../fixtures/bookData';
import { normalizeText } from '../../utils/textUtils';

class AmazonBookSearchPage {
  
  navigateToHome() {
    cy.visit('/');
    this.verifyHomePageLoaded();
    return this;
  }

  searchForBook(bookTitle = BOOK_DATA.TITLE) {
    cy.get(SEARCH_SELECTORS.searchInput)
      .should('be.visible')
      .clear()
      .type(bookTitle);
    
    cy.get(SEARCH_SELECTORS.searchButton)
      .should('be.enabled')
      .click();
    
    this.verifySearchResults(bookTitle);
    return this;
  }

  selectBookFromResults(bookTitle = BOOK_DATA.TITLE) {
    cy.get(BOOK_SELECTORS.bookByTitle(bookTitle))
      .should('be.visible')
      .click();
    
    this.verifyBookDetailsPageLoaded();
    return this;
  }

  verifyBookDetails(expectedDetails = BOOK_DATA) {
    this.verifyBookTitle(expectedDetails.TITLE);
    this.verifyBookLanguage(expectedDetails.LANGUAGE);
    this.verifyBookAuthor(expectedDetails.AUTHOR);
    this.verifyBookFormat(expectedDetails.FORMAT);
    this.verifyBookPages(expectedDetails.PAGES);
    this.verifyBookPublicationDate(expectedDetails.PUBLICATION_DATE);
    return this;
  }

  addBookToCart() {
    cy.get(BOOK_SELECTORS.addToCartButton)
      .should('be.visible')
      .should('be.enabled')
      .click();
    
    this.verifyBookAddedToCart();
    return this;
  }

  verifyCartConfirmation() {
    cy.get(CART_SELECTORS.confirmationMessage)
      .should('be.visible')
      .should('contain.text', CART_SELECTORS.SUCCESS_MESSAGE);
    
    return this;
  }

  // Métodos privados de verificação
  verifyHomePageLoaded() {
    cy.get(SEARCH_SELECTORS.searchInput).should('be.visible');
    cy.get(SEARCH_SELECTORS.searchButton).should('be.visible');
  }

  verifySearchResults(searchTerm) {
    cy.get(SEARCH_SELECTORS.resultsContainer)
      .should('be.visible')
      .should('contain.text', searchTerm);
  }

  verifyBookDetailsPageLoaded() {
    cy.get(BOOK_SELECTORS.bookTitle).should('be.visible');
    cy.url().should('include', '/dp/');
  }

  verifyBookTitle(expectedTitle) {
  cy.get(BOOK_SELECTORS.bookTitle)
    .should('be.visible')
    .invoke('text')
    .then((actualText) => {
      const normalizedActual = normalizeText(actualText);
      const normalizedExpected = normalizeText(expectedTitle);
      
      // Log para debug
      cy.log(`Texto atual: "${actualText}"`);
      cy.log(`Texto normalizado: "${normalizedActual}"`);
      cy.log(`Texto esperado: "${normalizedExpected}"`);
      
      expect(normalizedActual).to.equal(normalizedExpected);
    });
  }

  verifyBookAuthor(expectedAuthor) {
    cy.get(BOOK_SELECTORS.bookAuthor)
      .should('be.visible')
      .should('contain.text', expectedAuthor);
  }

  verifyBookLanguage(expectedLanguage) {
    cy.get(BOOK_SELECTORS.bookLanguage)
      .scrollIntoView()              // evita falso negativo de visibilidade
      .invoke('text')
      .then((raw) => {
        const clean = raw
          .normalize('NFC')
          .replace(/\u00a0/g, ' ')   // NBSP -> espaço normal
          .replace(/\s+/g, ' ')      // colapsa \n, \t, múltiplos espaços
          .trim();

        cy.log(`Texto processado do bylineInfo: "${clean}"`);
        cy.log(`Idioma esperado: "${expectedLanguage}"`);
        
        // Verifica se o texto contém o idioma esperado
        expect(clean).to.include(expectedLanguage);
      });
  }

  verifyBookFormat(expectedFormat) {
    cy.get(BOOK_SELECTORS.bookFormat)
      .scrollIntoView()
      .invoke('text')
      .then((raw) => {
        const clean = raw
          .normalize('NFC')
          .replace(/\u00a0/g, ' ')   // NBSP -> espaço normal
          .replace(/\s+/g, ' ')      // colapsa \n, \t, múltiplos espaços
          .trim();

        cy.log(`Formato processado: "${clean}"`);
        cy.log(`Formato esperado: "${expectedFormat}"`);
        
        expect(clean).to.include(expectedFormat);
      });
  }
  verifyBookPages(expectedPages) {
    cy.get(BOOK_SELECTORS.bookPages)
      .should('contain.text', expectedPages);
  }

  verifyBookPublicationDate(expectedDate) {
    cy.get(BOOK_SELECTORS.publicationDate)
      .should('contain.text', expectedDate);
  }

  // verifyBookAddedToCart() {
  //   cy.get(CART_SELECTORS.addToCartButton)
  //     .should('have.attr', 'disabled');
  // }
  verifyBookAddedToCart() {
    // Validar mensagem de confirmação após adicionar ao carrinho
    cy.get(CART_SELECTORS.confirmationMessage)
      .should('be.visible')
      .invoke('text')
      .then((text) => {
        const clean = text.normalize('NFC').trim();
        cy.log(`Mensagem de confirmação: "${clean}"`);
        expect(clean).to.eq(CART_SELECTORS.SUCCESS_MESSAGE);
      });
  }
}

export default new AmazonBookSearchPage();