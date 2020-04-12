import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium import webdriver

class CheckBot:

    def __init__(self, username,password,vehicleNumber,unitDesignator,mileage,logisPhone,portable1,portable2,portableOxygen,medicalAir,mainO2,lifepack,ivpump,apackLocation,apack,apackexp,drugboxLocation,drugbox,drugboxexp,rsi,rsiexp,stjoeCards,fuelcard,umCards
):
        company_id = "243"
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')

        wd = webdriver.Chrome(options=chrome_options)
        wd.set_window_size(600,1024)
        wd.get("https://suite.vairkko.com/APP/index.cfm/account/Login?reqEvent=main.index&qs=")

        print(wd.title)

        wd.find_element_by_name("companyid").send_keys(company_id)
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_id("submitBtn").click()

        print(wd.title)

        sleep(3)
        # elem = wd.find_elements_by_partial_link_text("Tools")
        toolbar = wd.find_element_by_xpath("//*[@id=\"headermenu-ul\"]/li[5]")
        toolbar.click()

        print(wd.title)

        tools = wd.find_element_by_xpath("//*[@id=\"left-panel\"]/nav/ul/li[5]")
        tools.click()

        check_sheets = wd.find_element_by_xpath("//*[@id=\"left-panel\"]/nav/ul/li[5]/ul/li[2]")
        check_sheets.click()
        sleep(2)
        print(wd.title)


        eastern_nextgen = wd.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div[2]/div/div[2]/div[2]/div/p/a[3]")
        eastern_nextgen.click()
        print(wd.title)

        vehicle = wd.find_element_by_name("vehicle")
        vehicle.click()
        option = vehicle.send_keys(vehicleNumber)
        vehicle.click()
        wd.find_element_by_name("unitID").send_keys(unitDesignator)
        wd.find_element_by_name("serviceMileage").send_keys(mileage)


        apackexp = wd.find_element_by_xpath("//*[@id=\"itemSelector1_210613_fillReqText\"]").send_keys(apackexp)

        apack = wd.find_element_by_name("itemSelector1_201889_fillReqText").send_keys(apack)
        apckloc = wd.find_element_by_name("itemSelector1_201888_fillReqText").send_keys(apackLocation)

        rsiexpir = wd.find_element_by_name("itemSelector1_201891_fillReqText").send_keys(rsiexp)
        rsinum = wd.find_element_by_name("itemSelector1_201890_fillReqText").send_keys(rsi)


        dbexpir = wd.find_element_by_name("itemSelector1_200715_fillReqText").send_keys(drugboxexp)
        db = wd.find_element_by_name("itemSelector1_200703_fillReqText").send_keys(drugbox)
        dbLoc = wd.find_element_by_name("itemSelector1_200698_fillReqText").send_keys(drugboxLocation)

        pump = wd.find_element_by_name("itemSelector1_218575_fillReqText").send_keys(ivpump)
        maino2 = wd.find_element_by_name("itemSelector1_200965_fillReqText").send_keys(mainO2)
        medAir = wd.find_element_by_name("itemSelector1_200966_fillReqText").send_keys(medicalAir)
        lpnum = wd.find_element_by_name("itemSelector1_239043_fillReqText").send_keys(lifepack)
        spare_bat = wd.find_element_by_name("itemSelector1_255305_fillReqText").send_keys("Yes")
        portableo2 = wd.find_element_by_name("itemSelector1_261637_fillReqText").send_keys(portableOxygen)
        radio2 = wd.find_element_by_name("itemSelector1_201887_fillReqText").send_keys(portable2)
        radio1 = wd.find_element_by_name("itemSelector1_201886_fillReqText").send_keys(portable1)

        portables_present = wd.find_element_by_name("itemSelector1_200686_fillReqText").send_keys("present")
        logisphonenum = wd.find_element_by_name("itemSelector1_220198_fillReqText").send_keys(logisPhone)
        logis_functional = wd.find_element_by_name("itemSelector1_200685_fillReqText").send_keys("present")
        stjoes = wd.find_element_by_name("itemSelector1_201883_fillReqText").send_keys(stjoeCards)
        fuel = wd.find_element_by_name("itemSelector1_201885_fillReqText").send_keys(fuelcard)
        um = wd.find_element_by_name("itemSelector1_201884_fillReqText").send_keys(umCards)

        dropdowns = wd.find_elements_by_tag_name("select")
        for items in dropdowns:
            item_id = items.get_property("id")
            item = wd.find_element_by_name(item_id)

            options = item.find_elements_by_tag_name("option")

            if options[0].text == "Please Select" and options[1].text == "Good Condition":
                item.send_keys(options[1].text)
            if options[0].text == "Please Select" and options[1].text == "Full":
                item.send_keys("Full")
            if options[0].text == "Please Select" and options[1].text == "Yes":
                item.send_keys("Yes")
            if options[0].text == "Please Select" and options[1].text == "No":
                item.send_keys("No")
            if options[0].text == "Please Select" and options[1].text == "Good":
                item.send_keys("Good")
            if options[0].text == "Please Select" and options[1].text == "Good Condition":
                item.send_keys("Key: Good Condition")
            if options[0].text == "Please Select" and options[1].text == "Present":
                item.send_keys("Present")
            if options[0].text == "Please Select" and options[1].text == "Functional":
                item.send_keys("Functional")
            if options[0].text == "Please Select" and options[1].text == "Present and functional":
                item.send_keys("Present and functional")
            if options[0].text == "Functional":
                item.send_keys("Functional")
            if options[0].text == "No additional problems/concerns":
                item.send_keys("No additional problems/concerns")

        save_to_drafts = wd.find_element_by_id("saveProg_id-gen")
        save_to_drafts.click()

        print("Is Completed")


