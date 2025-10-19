const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    viewportHeight: 1600,
    viewportWidth: 1920,
    baseUrl:'https://www.amazon.com.br',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    screenshotOnRunFailure: true,
  },
});
