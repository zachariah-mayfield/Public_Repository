Set-ExecutionPolicy RemoteSigned -force

IF (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.Windows.Identity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
  $Arguments = "& '" + $myinvocation.mycommand.definition + "'"
  Start-Process powershell -Verb runAs -ArgumentList $Arguments
  Break
}

Start-Transcript -Path "C:\Logs\Tableau_$(Get-Date).log"

$Tableau_API_UserName = CyberArk_UserName
$Tableau_API_Password = CyberArk_Password
$TableauServerName = "Your-Company-Tableau-Server-Name"
$Environment = 'Development'

#region Function Get-Tableau_API_Token
Function Get-Tableau_API_Token {
  [CmdletBinding()]
  Param (
    # $Tableau_API_UserName
    [Parameter(Mandatory=$true)
    [string]$Tableau_API_UserName,
    # $Tableau_API_Password
    [Parameter(Mandatory=$true)
    [string]$Tableau_API_Password,
    # $TableauServerName
    [Parameter(Mandatory=$true)
    [string]$TableauServerName,
    # $Environment
    [Parameter(Mandatory=$true)]
    [ValidateSet('Development', 'UAT', 'Production')]
    [string]$Environment,
    # $TableauServerAPI_Version
    [Parameter(Mandatory=$true)
    [string]$TableauServerAPI_Version
  )
  Begin {
    # Set the Security Protocol Type
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
  }
  Process {
    Try {
#region Tableau API Token
      # Headers
      $Headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
      $Headers.Add("Content-Type", "application/xml")
      # Body
      $Body = "<tsRequest>
      `n    <credentials name=`"$($Tableau_API_UserName)`" password=`"$($Tableau_API_Password)`">
      `n    <site contentUrl=`"`" />
      `n    </credentials>
      `n</tsRequest>"
      # Tableau Server API Call
      $Tableau_API_Token = ((Invoke-RestMethod "https://$($TableauServerName).$($Environment).Company-Domain.com/api/$($TableauServerAPI_Version)/auth/signin/" -Method 'POST' -Headers $Headers -Body $Body -ErrorAction Stop).TsResponse.Credentials.token)
      $Tableau_API_Token
#endregion Tableau API Token      
    }# END TRY
    Catch {
      IF ($null -ne $Error[0].Exception.Message) {
        $Error_Exception = ($_.Exception | Select *)
        $Error_Exception
      }# END IF
      $LASTEXITCODE
      Stop-Transcript
      EXIT $LASTEXITCODE
    }# END Catch
  }# END Process
  End {}
}# END Function Get-Tableau_API_Token

#region Function Get-Tableau_API_Token

Stop-Transcript
