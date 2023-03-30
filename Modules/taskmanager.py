import winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
key.Close()
