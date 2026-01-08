# 获取当前系统PATH
$systemPath = [Environment]::GetEnvironmentVariable("Path", "Machine")

# 定义Miniconda路径
$minicondaPaths = "C:\Users\12721\Miniconda3\envs\mamba-env;C:\Users\12721\Miniconda3\envs\mamba-env\Scripts;C:\Users\12721\Miniconda3\Scripts"

# 合并路径（Miniconda优先）
$newPath = "$minicondaPaths;$systemPath"

# 设置新的系统PATH
[Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")

Write-Host "系统PATH已更新，请重启电脑"
