from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint
import random

def test_brooke_adoption():
    driver = webdriver.Chrome(executable_path="/Users/gregoriovincent/Downloads/chromedriver")
    driver.get("http://puppies.herokuapp.com/")
    # Step 1 Select Brooke
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/div[4]/form[1]/div[1]/input[1]").click()
    # Step 2 Adopt Her
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/form[1]/div[1]/input[1]").click()
    # Step 3 Add a Chew Toy and Travel Carrier
    driver.find_element_by_css_selector("#toy").click()
    driver.find_element_by_css_selector("#carrier").click()
    # Step 4 Complete Adoption and Fill out Details
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/form[1]/div[1]/input[1]").click()
    driver.find_element_by_css_selector("#order_name").send_keys("Gregorio Vincent")
    driver.find_element_by_css_selector("#order_address").send_keys("123 Fake St.")
    driver.find_element_by_css_selector("#order_email").send_keys("email@email.com")
    # Step 5 Select Check Payment Type and Complete Adoption
    select = Select(driver.find_element_by_id('order_pay_type'))
    select.select_by_visible_text("Check")
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/fieldset[1]/form[1]/div[6]/input[1]").click()
    # Step 6 Use Assertion to Verify Successful Adoption
    notice = driver.find_element_by_css_selector("#notice").text
    assert "Thank you for adopting a puppy!" in notice
    driver.close()

def test_sparky_adoption():
    driver = webdriver.Chrome(executable_path="/Users/gregoriovincent/Downloads/chromedriver")
    # Step 1 Select Sparky from the Second Page
    driver.get("http://puppies.herokuapp.com/agency/index?page=2")
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/div[4]/form[1]/div[1]/input[1]").click()
    # Step 2 Choose to Adopt Sparky
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/form[1]/div[1]/input[1]").click()
    # Step 3 Select Collar
    driver.find_element_by_css_selector("#collar").click()
    # Step 4 Complete Adoption and Fill out Details
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/form[1]/div[1]/input[1]").click()
    driver.find_element_by_css_selector("#order_name").send_keys("Gregorio Vincent")
    driver.find_element_by_css_selector("#order_address").send_keys("123 Fake St.")
    driver.find_element_by_css_selector("#order_email").send_keys("email@email.com")
    select = Select(driver.find_element_by_id('order_pay_type'))
    # Step 5 Select Credit Card Payment and Complete Adoption
    select.select_by_visible_text("Credit card")
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/fieldset[1]/form[1]/div[6]/input[1]").click()
    # Step 6 Use Assertion to Verify Successful Adoption
    notice = driver.find_element_by_css_selector("#notice").text
    assert "Thank you for adopting a puppy!" in notice
    driver.close()

def test_adopt_2_random_dogs():
    driver = webdriver.Chrome(executable_path="/Users/gregoriovincent/Downloads/chromedriver")
    driver.get("http://puppies.herokuapp.com/")
    # Step 1 Select Random Dog
    dogs = driver.find_elements_by_tag_name("input")
    dog = dogs[randint(0, len(dogs)-1)]
    dog.click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/form[1]/div[1]/input[1]").click()
    # Step 2 Select Collar
    driver.find_element_by_css_selector("#collar").click()
    # Step 3 Select 2nd Random Dog
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/form[2]/div[1]/input[1]").click()
    dogs = driver.find_elements_by_tag_name("input")
    dog = dogs[randint(0, len(dogs)-1)]
    dog.click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/form[1]/div[1]/input[1]").click()
    # Step 4 Select Collar for 2nd dog
    driver.find_element_by_css_selector("#collar").click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/form[1]/div[1]/input[1]").click()
    # Step 5 Complete Adoption of both dogs and Fill out Details
    driver.find_element_by_css_selector("#order_name").send_keys("Gregorio Vincent")
    driver.find_element_by_css_selector("#order_address").send_keys("123 Fake St.")
    driver.find_element_by_css_selector("#order_email").send_keys("email@email.com")
    select = Select(driver.find_element_by_id('order_pay_type'))
    select.select_by_visible_text("Credit card")
    # Step 6 Use Assertion to Verify Successful Adoption
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/fieldset[1]/form[1]/div[6]/input[1]").click()
    notice = driver.find_element_by_css_selector("#notice").text
    assert "Thank you for adopting a puppy!" in notice
    driver.close()

def test_adopt_2_random_dogs_3_random_items():
    driver = webdriver.Chrome(executable_path="/Users/gregoriovincent/Downloads/chromedriver")
    driver.get("http://puppies.herokuapp.com/")
    # Step 1 Select Random Dog
    dogs = driver.find_elements_by_tag_name("input")
    dog = dogs[randint(0, len(dogs)-1)]
    dog.click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/form[1]/div[1]/input[1]").click()
    # Step 2 Select 3 Random products
    products = driver.find_elements_by_xpath('//input[@type="checkbox"]')
    three_random_products = random.sample(products, 3)
    for product in three_random_products:
        product.click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/form[2]/div[1]/input[1]").click()
    # Step 3 Select 2nd Random Dog
    dogs = driver.find_elements_by_tag_name("input")
    dog = dogs[randint(0, len(dogs)-1)]
    dog.click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/div[1]/form[1]/div[1]/input[1]").click()
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/form[1]/div[1]/input[1]").click()
    # Step 4 Complete Adoption of both dogs and Fill out Details
    driver.find_element_by_css_selector("#order_name").send_keys("Gregorio Vincent")
    driver.find_element_by_css_selector("#order_address").send_keys("123 Fake St.")
    driver.find_element_by_css_selector("#order_email").send_keys("email@email.com")
    select = Select(driver.find_element_by_id('order_pay_type'))
    select.select_by_visible_text("Credit card")
    driver.find_element_by_xpath("//body/div[@id='container']/div[@id='wrapper']/div[@id='content']/div[2]/fieldset[1]/form[1]/div[6]/input[1]").click()
    # Step 5 Use Assertion to Verify Successful Adoption
    notice = driver.find_element_by_css_selector("#notice").text
    assert "Thank you for adopting a puppy!" in notice
    driver.close()
