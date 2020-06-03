# Chocolatey(在windows下像linux一样安装软件)

## Install

* 参考官网：https://chocolatey.org/install

* 非admin用户安装：https://chocolatey.org/docs/installation#non-administrative-install

1. Save the script below as `ChocolateyInstallNonAdmin.ps1`.
2. Use the script below, determine where you might want Chocolatey installed if it is not to `C:\ProgramData\chocoportable`.
3. Open PowerShell.exe.
4. Run the following `Set-ExecutionPolicy Bypass -Scope Process -Force;`
5. Run `.\ChocolateyInstallNonAdmin.ps1`.

## Usage

* 参考：https://segmentfault.com/a/1190000021892579
