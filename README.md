# Selenium and Appium Robot Framework
## Python 3.7 and Robot Framework.
This framework used for selenium web and api testing using PageObject. Can generate allure report.
## Install framework:
- install Python 3.7
- set PYTHONPATH to workspace dir: `export PYTHONPATH="/":$PYTHONPATH`
- install requirements: `pip install -r $WORKSPACE/requirements.txt`
- run tests script using robotframework
##To run tests use following command:
- With default config:
`robot project\web\test\`
- With config:
`robot loglevel TRACE -v ENV:dev -v BROWSER:chrome -v LOCALE:ru -v HEADLESS:true project\web\test\`
- With allure report:
`robot -v ENV:ea --listener allure_robotframework --outputdir .\output\robot -x xunitoutput.xml project\web\test\`
  - To generate allure report use following command in allure command line:
`allure generate output\allure --clean`
- Multiple thread tests run:
`pabot --processes 2 project\web\test`
- Run test using tags(testrailid for example)
`robot --include testrailid=111 project\web`
# Run Mobile test
## Appium Settings
- Set avd and appium setting to configuration/configuration.py
- Store app.apk to configuration/environments dir and set "app_name" to config.json
- Run test using robot


