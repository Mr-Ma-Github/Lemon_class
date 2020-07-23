*** Settings ***
Library               Collections
Library               RequestsLibrary

*** Test Cases ***
用例1-Get Requests
    Create Session    github    http://api.github.com
    ${res}=          Get Request    github    /users/bulkan
    Status Should Be  200    ${res}
    Log    ${res}   
    Dictionary Should Contain Value    ${res.json()}    Bulkan Evcimen
    
用例2-Get Requests
    Create Session    qcd    http://47.107.168.87:8080
    &{req_data}=    Create Dictionary    mobilephone=18688773467    pwd=123456
    ${res}=    Get Request    qcd    /futureloan/mvc/api/member/register    params=${req_data}
    Log    ${res}
    Log    ${res.text}    
    Log    ${res.status_code}
    Log    ${res.json}            
    
用例3-Post Requests    #post必须要添加headers
    Create Session    qcd    http://47.107.168.87:8080
    &{req_data}=    Create Dictionary    mobilephone=18688773467    pwd=123456
    &{header}=    Create Dictionary    Content-Type=application/x-www-form-urlencoded    
    ${res}=    Get Request    qcd    /futureloan/mvc/api/member/register    data=${req_data}    headers=${header}
    Log    ${res}
    Log    ${res.text}    
    Log    ${res.status_code}
    Log    ${res.json}            

