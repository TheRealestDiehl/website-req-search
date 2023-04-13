@given(u'we have gone to {site}')
def step_impl(context, site):
    context.site = site
    context.browser = webdriver.Chrome()
    if not site.startswith("http"):
        site = "https://" + site
    context.browser.get(site)
    time.sleep(5)

@when(u'we search for "{category}"')
def step_impl(context, category):
    element_id = "twotabsearchtextbox"
    search_imput = context.browser.find_element(By.ID, element_id)
    search_input.clear()
    search_input.send_keys(category)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

@then(u'we find items from "{vendor}"')
def step_impl(context, vendor):
    page = context.browser.page_source
    assert vendor.upper() in page.upper()