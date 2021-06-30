from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

with open ('data.txt','r') as f:
    empty_dict={}
    string=f.readlines()
    for i in string:
        if i != '\n':
            empty_dict[i.split(':')[0].strip()]=(i.split(':')[-1])[:-1].strip()

url='https://lms.mahaonline.gov.in/'
driver=webdriver.Chrome('C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver')

driver.get(url)

driver.find_element_by_id('UserName').send_keys(empty_dict['Username'])
driver.find_element_by_id('Password').send_keys(empty_dict['Password'])
driver.find_element_by_id('btnLogin').click()

url='https://lms.mahaonline.gov.in/ShopEstabilishment/ShopEstabilishment?ServiceID=3&Department=Shop'
driver.get(url)
driver.find_element_by_id('Confirm').click()


objShpEstab_Division=Select(driver.find_element_by_id("objShpEstab_Division_Value")).select_by_value('1');time.sleep(0.4)
objShpEstab_Distict=Select(driver.find_element_by_id("objShpEstab_Distict_Value")).select_by_value('2');time.sleep(0.4)
objShpEstab_Office=Select(driver.find_element_by_id("objShpEstab_Office_Value")).select_by_value('30');time.sleep(0.4)

driver.find_element_by_id("objShpEstab_InstitutionName").send_keys(empty_dict['Company'])

objShpEstab_PreviousEstablishmentRegType=Select(driver.find_element_by_id("objShpEstab_PreviousEstablishmentRegType_ID")).select_by_value('3')

driver.find_element_by_id("objAddressUCModel_AddrofBuilding_C").send_keys(empty_dict['CBuilding'])
driver.find_element_by_id("objAddressUCModel_AddrofStreet_C").send_keys(empty_dict['CStreet'])
driver.find_element_by_id("objAddressUCModel_AddrofLandmark_C").send_keys(empty_dict['CLandmark'])
driver.find_element_by_id("objAddressUCModel_AddrofLocality_C").send_keys(empty_dict['CLocality'])
driver.find_element_by_id("objShpEstab_InstitutionContactNo").send_keys(empty_dict['Contact']);time.sleep(0.4)
driver.find_element_by_id("objShpEstab_InstitutionEmailId").clear();time.sleep(0.4)
driver.find_element_by_id("objShpEstab_InstitutionEmailId").send_keys(empty_dict['EmailId'])


objAddressUCModel_DistrictCode_C=Select(driver.find_element_by_id("objAddressUCModel_DistrictCode_C")).select_by_visible_text('Thane');time.sleep(0.4)
objAddressUCModel_TalukaCode_C=Select(driver.find_element_by_id("objAddressUCModel_TalukaCode_C")).select_by_visible_text('Thane');time.sleep(0.4)
objAddressUCModel_VillageCode_C=Select(driver.find_element_by_id("objAddressUCModel_VillageCode_C")).select_by_visible_text('Navi Mumbai (Municipal Corporation.)')
driver.find_element_by_id("objAddressUCModel_PinCode_C").send_keys(empty_dict['CPincode'])
objShpEstab_LandType_Value=Select(driver.find_element_by_id("objShpEstab_LandType_Value")).select_by_value('R')
driver.find_element_by_id("objShpEstab_NatureofBusiness").send_keys(empty_dict['N_O_B'])
objShpEstab_InstitInPublicPrivateArea_Value=Select(driver.find_element_by_id("objShpEstab_InstitInPublicPrivateArea_Value")).select_by_value('PU')
driver.find_element_by_id("objShpEstab_TotalWorkers_Other_Male").send_keys(empty_dict['Male'])
driver.find_element_by_id("objShpEstab_TotalWorkers_other_Females").send_keys(empty_dict['Female'])
driver.find_element_by_id("objShpEstab_TotalWorkers_other_Transgender").send_keys(empty_dict['Trans'])
driver.find_element_by_id("objShpEstab_TotalWorkers_Apprenticeship_Male").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_Apprenticeship_Females").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_Apprenticeship_Transgender").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_ContractLabour_Male").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_ContractLabour_Females").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_ContractLabour_Transgender").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_PartTime_Male").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_PartTime_Females").send_keys("0")
driver.find_element_by_id("objShpEstab_TotalWorkers_PartTime_Transgender").send_keys("0")



driver.find_element_by_id("objShpEstab_OwnersName").send_keys(empty_dict['OwnersName'])
driver.find_element_by_id("objAddressUCModel_AddrofBuilding_P").send_keys(empty_dict['Building_P'])
driver.find_element_by_id("objAddressUCModel_AddrofStreet_P").send_keys(empty_dict['Street_P'])
driver.find_element_by_id("objAddressUCModel_AddrofLandmark_P").send_keys(empty_dict['Landmark_P'])
driver.find_element_by_id("objAddressUCModel_AddrofLocality_P").send_keys(empty_dict['Locality_P'])

objAddressUCModel_DistrictCode_P=Select(driver.find_element_by_id("objAddressUCModel_DistrictCode_P")).select_by_visible_text('Thane');time.sleep(0.4)
objAddressUCModel_TalukaCode_P=Select(driver.find_element_by_id("objAddressUCModel_TalukaCode_P")).select_by_visible_text('Thane');time.sleep(0.4)
objAddressUCModel_VillageCode_P=Select(driver.find_element_by_id("objAddressUCModel_VillageCode_P")).select_by_visible_text('Navi Mumbai (Municipal Corporation.)');time.sleep(0.2)

driver.find_element_by_id("objAddressUCModel_PinCode_P").send_keys(empty_dict['PinCode_P'])
driver.find_element_by_id("objAddressUCModel_ResidentSince_P").send_keys("2020")
driver.find_element_by_id("objAddressUCModel_UIDNo_employer").send_keys(empty_dict['UIDNo_employer'])
driver.find_element_by_id("objAddressUCModel_EmailID_employer").send_keys(empty_dict['EmailId'])
driver.find_element_by_id("objAddressUCModel_MobileNo__employer").send_keys(empty_dict['Contact'])
driver.find_element_by_id("objAddressUCModel_Status_employer").send_keys("proprietor")




objShpEstab_EstablishmentTypeMst_Value=Select(driver.find_element_by_id("objShpEstab_EstablishmentTypeMst_Value")).select_by_value('CE');time.sleep(0.5)
objShpEstab_EstablishmentType_Value=Select(driver.find_element_by_id("objShpEstab_EstablishmentType_Value")).select_by_value('147');time.sleep(0.2)
driver.find_element_by_id("objShpEstab_BusinessType").send_keys("readymade garments shop")
objShpEstab_EstablishmentCategory_Value=Select(driver.find_element_by_id("objShpEstab_EstablishmentCategory_Value")).select_by_value('SO')
driver.find_element_by_id("objShpEstab_InstiOwnersFamilydetails").send_keys("0")
driver.find_element_by_id("objShpEstab_InstitOwnersTotalFamilyMembers_Males").send_keys("0")
driver.find_element_by_id("objShpEstab_InstitOwnersTotalFamilyMembers_Females").send_keys("0")
driver.find_element_by_id("objShpEstab_InstitOwnersTotalFamilyMembers_Transgender").send_keys("0")
checkboxElement = driver.find_element_by_id("checkboxPrimary")
checkboxElement.click()

