# 📝 História de Usuário

> “Como usuário, quero buscar um livro específico e adicioná-lo ao carrinho para poder finalizá-lo posteriormente.”

---

## ✅ Critérios de Aceite

O livro encontrado deve:

- E a edição em **inglês**
- O autor é **Chip Huyen**
- Ser **Você está comprando o livro físico** (não Kindle)
- Ele é **novo**
- Ao adicionar ao carrinho, deve aparecer a mensagem **“Adicionado ao carrinho”**

---

## 🧭 Casos de Teste

| ID    | Caso de Teste                                                                 | Pré-condição                      | Passos                                                                                                                                               | Resultado Esperado                                                |
|-------|--------------------------------------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| TC_01 | Acessar página inicial da Amazon                                               | Navegador aberto                  | 1. Acessar [https://www.amazon.com.br](https://www.amazon.com.br)                                                                                    | Página inicial deve carregar com sucesso                          |
| TC_02 | Pesquisar pelo livro “AI Engineering: Building Applications with Foundation Models” | Página inicial carregada          | 1. Digitar título no campo de busca<br>2. Clicar em “Pesquisar”                                                                                       | Lista de resultados aparece contendo o livro desejado             |
| TC_03 | Selecionar o livro correto                                                    | Lista de resultados carregada     | 1. Clicar no resultado que corresponda exatamente ao título desejado                                                                                | Página de produto é aberta com detalhes do livro                  |
| TC_04 | Validar detalhes do livro                                                     | Página do produto aberta          | 1. Verificar idioma = inglês<br>2. Verificar autor = Chip Huyen<br>3. Verificar formato = Livro físico<br>4. Verificar condição = Novo                 | Todos os critérios devem ser verdadeiros                          |
| TC_05 | Adicionar o livro ao carrinho                                                | Página do produto válida          | 1. Clicar em “Adicionar ao carrinho”                                                                                                                 | Exibir mensagem “Adicionado ao carrinho” com sucesso              |
| TC_06 | Validar mensagem de confirmação                                              | Livro adicionado                  | 1. Observar mensagem apresentada                                                                                                                    | Texto exibido deve ser exatamente “Adicionado ao carrinho”        |
