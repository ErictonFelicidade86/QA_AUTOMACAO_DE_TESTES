/// <reference types="cypress"/>
import homePage from "../support/page/home/homePage";

const home = homePage;

describe('Realizar busca de um livro específico e adicioná-lo ao carrinho', () => {
  
  it('Acessar página inicial da Amazon', () => {
    home.goTo();            // Acessar página inicial da Amazon
  });

  it('Pesquisar pelo livro “AI Engineering: Building Applications with Foundation Models', ()=> {
    home.goTo();            // Acessar página inicial da Amazon
    home.bookSearch();      // Pesquisa pelo titulo
  });

  it('Selecionar o livro correto', () => {
    home.goTo();            // Acessar página inicial da Amazon
    home.bookSearch();      // Pesquisa pelo titulo
    home.selectBook();      // Lista de resultados
  });

  it('Validar detalhes do livro', ()=> {
    home.goTo();            // Acessar página inicial da Amazon
    home.bookSearch();      // Pesquisa pelo titulo
    home.selectBook();      // Lista de resultados
    home.bookDetails();     // Validar detalhes do livro
  });
  it('Adicionar o livro ao carrinho', ()=> {
    home.goTo();            // Acessar página inicial da Amazon
    home.bookSearch();      // Pesquisa pelo titulo
    home.selectBook();      // Lista de resultados
    home.bookDetails();     // Validar detalhes do livro
    home.addBookToCart();   // Adicionar o livro ao carrinho
  });

  it.only('Fluxo completo da busca do livro especifico', ()=> {
    home.goTo();                  // Acessar página inicial da Amazon
    home.bookSearch();            // Pesquisa pelo titulo
    home.selectBook();            // Lista de resultados
    home.bookDetails();           // Validar detalhes do livro
    home.addBookToCart();         // Adicionar o livro ao carrinho
    home.confirmationMessage();   // Validar mensagem de confirmação
  });
  
});
