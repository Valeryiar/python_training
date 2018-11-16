# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(capabilities=cap, executable_path="C:\\path\\to\\geckodriver.exe")
browser.get('http://google.com/')
browser.quit()


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="dbs", header="sergseg", footer="eshaseh"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

