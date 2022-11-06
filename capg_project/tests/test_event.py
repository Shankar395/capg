import datetime
import pytest
from Library.excel_library import Readexcel
from POM.event_module import BmsPage


class TestBmsPage:
    read_xl = Readexcel()
    data = read_xl.read_test_data()

    @pytest.mark.parametrize("location, name, phoneno, Email", data)
    def test_Event(self, init_driver, location, name, phoneno, Email):
        driver = init_driver
        try:
            tp = BmsPage(driver)
            tp.bengaluru(location)
            tp.click_bengaluru()
            tp.click_on_events()
            tp.click_on_browse()
            tp.click_on_Art_Beat_Bengaluru()
            tp.click_on_Texture_painting()
            tp.click_Book()
            tp.click_on_Add()
            tp.click_on_proceed()
            tp.enter_Name(name)
            tp.enter_phone_no(phoneno)
            tp.enter_Email(Email)
            tp.click_on_checkbox()
            tp.click_on_submit()
            tp.click_on_login_to_proceed()

        except BaseException:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            path = r"C:\Users\Shankar Kadam\PycharmProjects\capg_project\screenshots"
            driver.save_screenshot(path + name)
