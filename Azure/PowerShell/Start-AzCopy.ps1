
$environment: Development
$Subscription_ID: 'Your-Azure-Subscription-ID'
$Tenant_ID: 'Your-Azure-Tenant-ID'
$Service_Principal: 'Your_Azure_Service_Principal_Name'
$Object_ID: 'Your-Azure-Object-ID'
$Client_ID: 'Your-Azure-Client-ID'
$Secret: 'Your-Azure-Secret'
$Resource_Group: 'Your_Azure_Resource_Group_Name'
$Application_ID: 'Your-Azure-Application-ID'
$Storage_Account: 'Your_Azure_Storage_Account_Name'
$Storage_Container: 'Your_Azure_Storage_Container_Name'


Function Start-AzCopy {
  Param (
    [Parameter(Mandatory=$true)
    [string]$Service_Principal,

    [Parameter(Mandatory=$true)]
    [string]$Application_ID,

    [Parameter(Mandatory=$true)]
    [string]$Application_ID,

    [Parameter(Mandatory=$true)]
    [string]$Tenant_ID,

    [Parameter(Mandatory=$true)]
    [string]$BlobName,

    [Parameter(Mandatory=$true)]
    [string]$ResourceGroupName
  )
