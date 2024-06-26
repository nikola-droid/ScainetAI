Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "%USERPROFILE%\Documents\GitHub\ScainetAI\Runner.bat" & Chr(34), 0
WinScriptHost.Run Chr(34) & "%USERPROFILE%\Documents\GitHub\ScainetAI\Runner_1.bat" & Chr(34), 0
Set WinScriptHost = Nothing