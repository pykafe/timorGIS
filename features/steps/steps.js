const { When, Then, After, setDefaultTimeout } = require('@cucumber/cucumber');
const assert = require('assert');
const { Builder, By, until } = require('selenium-webdriver');

setDefaultTimeout(10 * 1000);

When('we visit Timor Journey', async function () {
    // Write code here that turns the phrase above into concrete actions
    this.driver = new Builder()
        .forBrowser('chrome')
        .build();

    this.driver.wait(until.elementLocated(By.css('body')));

    await this.driver.get('http://127.0.0.1:8000/en/vue/');
});

Then('we should see the app is loading photos', async function () {
    // Write code here that turns the phrase above into concrete actions
    return 'pending';
});

Then('we should see many photos in a grid', async function () {
    // Write code here that turns the phrase above into concrete actions
    var imageCards = await this.driver.findElements(By.css('div.image_card'));
    assert(imageCards.length > 0, "NO image cards found");
});

After(async function() {
    this.driver.close();
});