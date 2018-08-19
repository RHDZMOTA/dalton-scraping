from typing import Dict, List, Set
from selenium import webdriver
from config import Settings
from model import *

import uuid


class Dalton(object):
    URL_HOME = "https://daltontoyota.com.mx/"
    URL_MODEL = URL_HOME + "modelos/{model}"

    def __init__(self, download_all=True):
        self.browser = self._select_web_driver()
        self.browser.get(self.URL_HOME)
        self.vehicle_models: Dict = self._get_vehicle_models()
        self.models = None
        if download_all:
            self.models = self.all_models()
            self.close_connection()

    def _select_web_driver(self):
        driver = None
        driver_path = Settings.Selenium.driver
        if "chrome" in driver_path:
            driver = webdriver.Chrome(driver_path)
        if "phantom" in driver_path:
            driver = webdriver.PhantomJS(driver_path)
        return driver

    def _get_vehicle_models(self) -> Set[str]:
        models = []
        for element in self.browser.find_elements_by_xpath("//a[@href]"):
            href = element.get_attribute("href")
            if "model" not in href:
                continue
            model = [e for e in href.split("/") if e != ""][-1]
            models.append(model)
        return set(models)

    def get_model(self, model: str) -> Model:
        if model not in self.vehicle_models:
            raise ValueError("Parameter <model> not in <vehicle_models>")
        model_id = str(uuid.uuid4())
        model_url = self.URL_MODEL.format(model=model)
        self.browser.get(model_url)
        colors = self._get_colors(model_id)
        versions = self._get_versions(model_id)
        interior, exterior = self._get_car_images()
        specs = [elm.get_attribute("href") for elm in self.browser.find_elements_by_xpath("//a[@href]") if ".pdf" in elm.get_attribute("href")][0]
        return Model(model_id, model, colors, versions, specs, interior, exterior)

    def all_models(self) -> List[Model]:
        if self.models:
            return self.models
        models = []
        for model in self.vehicle_models:
            try:
                models.append(self.get_model(model))
            except Exception as e:
                print("> Error while trying to fetch model: " + model)

        return models

    def _get_images(self):
        return self.browser.find_elements_by_xpath('//img[@alt="Dalton"]')

    def _get_car_images(self):
        interior, exterior = [], []
        for image in self._get_images():
            src = image.get_attribute("src")
            if "gallery" not in src:
                continue
            if "interior" in src:
                interior.append(src)
            if "exterior" in src:
                exterior.append(src)
        return interior, exterior

    def _get_colors(self, model_id: str) -> List[Color]:
        colors = []
        for color_element in self._get_images():
            if "car" not in color_element.get_attribute("id"):
                continue
            color = Color(model_id, color_element.get_attribute("id"), color_element.get_attribute("src"))
            colors.append(color)
        return colors

    def _get_versions(self, model_id: str) -> List[Version]:
        versions = []
        for content in self.browser.find_elements_by_class_name("box-content"):
            version_html = content.get_attribute("innerHTML")
            version = Version(model_id, version_html)
            versions.append(version)
        return versions

    def close_connection(self):
        self.browser.quit()
