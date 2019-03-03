# Selenium Robot Framework
## Framework use Python 3 and Robot Framework.
To run test use following command:
With default config:
`robot project\web\test\`
With set config:
`robot loglevel TRACE -v ENV:dev -v BROWSER:chrome -v LOCALE:ru -v HEADLESS:true project\web\test\`
With allure report:
`robot -v ENV:ea --listener allure_robotframework --outputdir .\output\robot -x xunitoutput.xml project\web\test\`
To generate allure report use following command in allure command line:
`allure generate output/allure --clean`
Multiple thread tests run:
`pabot --processes 2 project\web\test`
