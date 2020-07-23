*** Settings ***
Library    SeleniumLibrary    
Resource    ../页面对象层/登录页面关键字.robot
Variables    ../测试数据层/公共数据.py
Variables    ../测试数据层/登录数据.py

*** Keywords ***
打开浏览器并访问前程贷系统
    Open Browser    ${web_login_url}    chrome 
    登录页面关键字.登录操作    ${success_data.username}    ${success_data.password}
    