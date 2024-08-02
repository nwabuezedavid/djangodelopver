
from django.urls import path
from .views import *


urlpatterns = [
    path('', home , name="home"),
    path('contact/', contact , name="contact"),
    path('about/', about , name="about"),
    path('Activate/', Activate , name="Activate"),
    path('Activated/', Activated , name="Activated"),
    path('disabled/', disabledaccount , name="disabledaccount"),
    path('loan/', LOan , name="loan"),
    path('transfers/', transfers , name="transfers"),
    path('linktoactivate/<pk>/', linktoactivate , name="linktoactivate"),
   
    path('Auth/', loginuser , name="loginuser"),
 
    path('logout/', logoutUser , name="logoutUser"),
    path('resetpass/', resetpass , name="resetpass"),
    path('forgotten/', forgotten , name="forgotten"),

# dashboard

    path('dashboard/<pk>/', dashboard , name="dashboard"),
    path('fundingfinal/<pk>/', fundingf , name="fundingf"),
    path('funding/<pk>/', funding , name="funding"),
    path('localTransfer/<pk>/', innertransfer , name="innertransfer"),
    path('samebank/<pk>/', samebank , name="samebank"),
    path('finalD/<pk>/', finialtransfer , name="finialtransfer"),
    path('Accountsummary/<pk>/', Accountsum , name="Accountsum"),
    path('loan/<pk>/', loancover , name="loancover"),
    path('loanform/<pk>/', loanform , name="loanform"),
    path('Checkdeposit/<pk>/', Checkdepositx , name="Checkdepositx"),
    path('loan-pending/<pk>/', loanpend , name="loanpend"),
    path('withdraw-Fund/<pk>/', widthdrawalF , name="widthdrawalF"),
    path('create-pin/<pk>/', pinuser , name="pin"),
    path('withdraw-Fund-history/<pk>/', widthdrawalhistory , name="widthdrawalhistory"),
    path('withdraw-Fund-check/<pk>/', widthdrawalcheck , name="widthdrawalcheck"),
    path('add-withdraw-Fund/<pk>/', AddwidthdrawalF , name="AddwidthdrawalF"),
    path('pending/<pk>/', pending , name="pending"),
    path('profile/<pk>/', profile , name="profile"),
    path('security/<pk>/', security , name="security"),
    path('btc-history/<pk>/', btchistory , name="btchistory"),
    path('Check/<pk>/', successful , name="successful"),
    path('Check2/<pk>/', successful2 , name="successful2"),
    path('Btcpay/<pk>/', Btcpay , name="Btcpay"),
    path('kycD/<pk>/', kycD , name="kycD"),
    path('kycD/<pk>/', kycD , name="kycD"),
    path('Kycx/<pk>/', Kyc , name="Kyc"),




# admin
    path('adminauth/<pk>/', adminauth , name="admin"),
    path('adminauth-edit/<pk>/', adminauthedit , name="adminauthedit"),
    path('adminauth-edit-personal/<pk>/', adminautheditpersonal , name="adminautheditpersonal"),
    path('adminauth-edit-personal-security/<pk>/', personalsecurity , name="personalsecurity"),
    path('personal-tran/<pk>/', ptran , name="ptran"),
    path('personal-tran-delete/<pk>/<cc>/', ptrandelete , name="ptrandelete"),
    path('personal-tran-delete-al/<pk>/<cc>/', allptrandelete , name="allptrandelete"),
    path('personal-tran-approved/<pk>/<cc>/', ptranapproved , name="ptranapproved"),
    path('personal-tran-approved-alcx/<pk>/<cc>/', allptranapproved , name="allptranapproved"),
    path('fund-user/<pk>/', funuser , name="funuser"),
    path('All-trans/<pk>/', alltran , name="alltran"),
    path('request-send-btc/<pk>/', senduser , name="senduser"),
    path('request-send-btc-view/<pk>/', senduserbtcview , name="senduserbtcview"),
    path('request-send-kyc/<pk>/', senduserkcy , name="senduserkcy"),
    path('request-send-kyc-list-approved/<pk>/', approvedkyc , name="approvedkyc"),
    path('request-send-kyc-list-delete-all/<pk>/', allkycdelete , name="allkycdelete"),
    path('request-send-kyc-list/<pk>/', senduserkcyview , name="senduserkcyview"),
    path('delete-btc-user/<pk>/', allbtcdelete , name="allbtcdelete"),
    path('delete-btc-user-ss/<pk>/', deletebtc , name="deletebtc"),
    path('app-btc-user-ss/<pk>/', approvedx , name="approvedx"),
    path('deete-btc-user-ss/<pk>/', deltex , name="deltex"),
    path('create-btc-Wallet-ss/<pk>/', createwalletcrypto , name="createwalletcrypto"),
    path('history-btc-Wallet-ss/<pk>/', BtchistoryV , name="BtchistoryV"),
    path('Edite-btc-Wallet-ss/<pk>/', createwalletedite , name="createwalletedite"),
    path('delete-btc-user-a/<pk>/', approvedbtc , name="approvedbtc"),
    path('edite-site-a/<pk>/', EditeSite , name="EditeSite"),
    path('delete-d-user/<pk>/', deleteuserc , name="deleteuserc"),
    path('delete-d-user-kyc/<pk>/', deletekyc , name="deletekyc"),
    path('delete-d-deposit-all/<pk>/', ptrandeleteall , name="ptrandeleteall"),
    path('delete-d-deposit-all-c/<pk>/', allptrandeleteall , name="allptrandeleteall"),
    path('disp-tran-approved/<pk>/<cc>/', disptranapproved , name="disptranapproved"),
    path('disp-tran-approved-ds/<pk>/<cc>/', alldisptranapproved , name="alldisptranapproved"),
    path('check-send-deposit/<pk>/', checkdepositeadmin , name="checkdepositeadmin"),
    path('check-approve-deposit/<pk>/', approvedcheck , name="approvedcheck"),
    path('check-delete-deposit/<pk>/', deletecheck , name="deletecheck"),
    path('check-alldelete-deposit/<pk>/', allcheckdelete , name="allcheckdelete"),
    path('check-view-deposit/<pk>/', sendusercheck , name="sendusercheck"),
    path('check-view-withdrawal/<pk>/', allaccountwithdrawAL , name="allaccountwithdrawAL"),
    path('delete-view-withdrawal/<pk>/<cc>/', deleteaccom , name="deleteaccom"),

    path('mailxx/', mailxs , name="mails"),


]