export const SEARCH_SELECTORS = {
  searchInput: 'input[placeholder="Pesquisar Amazon.com.br"]',
  searchButton: '#nav-search-submit-button',
  resultsContainer: '[data-component-type="s-search-result"]'
};

export const BOOK_SELECTORS = {
  bookByTitle: (title) => `img[alt="${title}"]`,
  bookTitle: '#productTitle',
  bookAuthor: '#bylineInfo',
  bookLanguage: '#bylineInfo',
  bookFormat: 'li[aria-posinset="2"] .rpi-attribute-value span', // Assumindo que é o 2º item
  bookPages: 'li[aria-posinset="1"] .rpi-attribute-value span',
  publicationDate: 'li[aria-posinset="4"] .rpi-attribute-value span',
  addToCartButton: '#add-to-cart-button'
};

export const CART_SELECTORS = {
  confirmationMessage: 'h1.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold',
  SUCCESS_MESSAGE: 'Adicionado ao carrinho'
};
