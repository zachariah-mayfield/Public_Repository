
Function Get-CMD_ProcessOutput {
  Param (
    [Parameter(Mandatory=$true)]$FileName,$Args
  )
  $Process = New-Object System.Diagnostics.Process
  $Process.StartInfo.UseShellExecute = $false
  $Process.StartInfo.RedirectStandardOutput = $true
  $Process.StartInfo.RedirectStandardError = $true
  $Process.StartInfo.FileName = $FileName
  IF ($Args) {
    $Process.StartInfo.Arguments = $Args
  }
  $Out = $Process.Start()
  $StandardError = $Process.StandardError.ReadToEnd()
  $StandardOutput = $Process.StandardOutput.ReadToEnd()
  $Output = New-Object PSObject
  $Output | Add-Member -type NoteProperty -name StandardError -Value $StandardError
  $Output | Add-Member -type NoteProperty -name StandardOutput -Value $StandardOutput
  return $Output
}
