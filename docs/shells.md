# PowerShell and terminal guide

[Back to the repository](../README.md) · [Windows CMD guide](cmd.md)

A terminal is the application that hosts a shell. Windows Terminal can run PowerShell, CMD, or a Linux shell through WSL; each uses its own command syntax. Choose the section that matches the shell in your active tab.

All examples require Python 3.11 or newer and use only the standard library. Run each block in order and resolve any error before continuing. Installation commands change your computer; the remaining sections work inside your project folder.

## Windows PowerShell

These commands work in Windows PowerShell 5.1 and PowerShell 7 on Windows. Open PowerShell from Start or select its profile in Windows Terminal.

### Install or update Python

Install the official Python install manager using WinGet:

```powershell
winget --version
winget install --id 9NQ7512CXL7T --exact --source msstore
```

Review the installer prompts, then close PowerShell and open a new window:

```powershell
pymanager install --update default
pymanager list
pymanager exec --version
python --version
```

With the manager's standard configuration, `default` selects the latest stable Python release. If you configured another default, that choice takes precedence. Installation is for your Windows account. See [Python's Windows documentation](https://docs.python.org/3/using/windows.html) and the [installation troubleshooting notes](cmd.md#if-installation-is-unavailable).

To update the manager later:

```powershell
winget upgrade --id 9NQ7512CXL7T --exact --source msstore
```

Reopen PowerShell, then repeat `pymanager install --update default` and check the version. Existing virtual environments retain their own interpreter; create a new environment when moving a project to another Python version.

### Clone and navigate

Start in the parent folder where you want to keep the repository. Git must already be installed.

```powershell
git --version
git clone https://github.com/drshilpijainphd-code/python-explained.git
Set-Location python-explained
Get-Location
Get-ChildItem
```

Clone only once. For an existing checkout, use `Set-Location` with its actual path. Save the repository location for this session:

```powershell
$repoRoot = (Get-Location).Path
Set-Location examples
Get-ChildItem -Filter *.py
python .\07_csv_sales_summary.py
Set-Location ..
```

`cd` is an alias for `Set-Location`. Unlike CMD, PowerShell does not use `cd /d`. To return to the saved path, including its drive:

```powershell
Set-Location -LiteralPath $repoRoot
```

Quote literal paths containing spaces, for example `Set-Location -LiteralPath 'D:\Projects\Python Learning\python-explained'`. Replace that illustrative path with one that exists. See Microsoft's [Set-Location reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-location).

To visit a folder and return, start at the repository root:

```powershell
Push-Location examples
python .\10_sqlite_database.py
Pop-Location
Get-Content .\examples\07_csv_sales_summary.py
```

### Run examples and checks

From the repository root:

```powershell
python .\examples\01_hello_python.py
python .\examples\12_command_line_tool.py --name 'Alex Morgan'
python .\examples\12_command_line_tool.py --help
python .\scripts\run_examples.py
python -m unittest discover -s tests -v
```

After a Python command, `$LASTEXITCODE` contains its exit status: zero means success. To run the tests only when all example outputs pass, use this block, which also works in Windows PowerShell 5.1:

```powershell
python .\scripts\run_examples.py
if ($LASTEXITCODE -eq 0) {
    python -m unittest discover -s tests -v
}
```

If `python` resolves to an older installation, inspect `Get-Command python -All`. You can replace `python` with `pymanager exec` in these commands to use the managed runtime.

### Optional virtual environment

From the repository root, create the environment and run its interpreter directly:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe .\scripts\run_examples.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

If your PowerShell policy permits local scripts, you can optionally activate it:

```powershell
.\.venv\Scripts\Activate.ps1
python .\examples\01_hello_python.py
deactivate
```

If activation is blocked, use the direct interpreter commands above. They work without changing the execution policy. The [Python venv documentation](https://docs.python.org/3/library/venv.html) explains activation and environment layout.

## macOS and Linux terminals

The following project commands work in Bash and Zsh. On Windows, use this section only inside a Linux environment such as WSL. Install Python inside that environment as well.

### Install Python on macOS

If [Homebrew](https://brew.sh/) is already installed and configured in your shell:

```bash
brew update
brew install python3
python3 --version
command -v python3
```

For an existing Homebrew installation of Python, use `brew upgrade python3` after `brew update`. This selects the current Python formula supplied by Homebrew; package availability can lag a new upstream release. See [Homebrew's Python guidance](https://docs.brew.sh/Homebrew-and-Python).

Without Homebrew, open the official macOS downloads page and use its current stable installer:

```bash
open https://www.python.org/downloads/macos/
```

Reopen the terminal after installation and run `python3 --version`.

### Install Python on Ubuntu or Debian

Use the distribution's package manager:

```bash
sudo apt update
sudo apt install python3 python3-venv git
python3 --version
command -v python3
```

These packages provide the Python version supported by your distribution, which may differ from the latest upstream release. Verify that it is at least 3.11 for this repository. The same install command updates these packages when newer versions are available in your configured repositories. Other Linux distributions use different package managers.

Keep the distribution-managed Python in place because operating-system tools may depend on it. Consult [Ubuntu's Python setup guide](https://ubuntu.com/developers/docs/howto/python-setup/) for the supported development setup.

### Clone, navigate, and run

Start in your projects folder with Python and Git installed:

```bash
git --version
git clone https://github.com/drshilpijainphd-code/python-explained.git
cd python-explained
pwd
ls
```

Clone only once. From the repository root:

```bash
repo_root="$PWD"
cd examples
ls *.py
python3 07_csv_sales_summary.py
cd ..
python3 examples/12_command_line_tool.py --name 'Alex Morgan'
python3 examples/12_command_line_tool.py --help
cat examples/07_csv_sales_summary.py
```

Use `cd "$repo_root"` to return to the saved repository location. Quote paths containing spaces. In Bash and Zsh, `cd -` returns to the previous directory; `cd ..` moves to the parent directory.

### Optional virtual environment and checks

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python --version
python scripts/run_examples.py
python -m unittest discover -s tests -v
deactivate
```

Activation is optional. Run the checks directly through the environment when preferred:

```bash
.venv/bin/python scripts/run_examples.py && .venv/bin/python -m unittest discover -s tests -v
```

`&&` runs the second command only if the first succeeds. Immediately afterward, `echo "$?"` prints the final exit status. Expect `15/15 examples passed.` from the runner and `Ran 14 tests` followed by `OK` from the tests.

## Command reference

Each row is a separate reference. File paths are relative to the repository root.

| Task | Windows PowerShell | Bash / Zsh |
| --- | --- | --- |
| Current directory | `Get-Location` | `pwd` |
| List files | `Get-ChildItem` | `ls` |
| Include hidden files | `Get-ChildItem -Force` | `ls -a` |
| Enter examples | `Set-Location examples` | `cd examples` |
| Parent directory | `Set-Location ..` | `cd ..` |
| Read a file | `Get-Content README.md` | `cat README.md` |
| Find Python | `Get-Command python -All` | `command -v python3` |
| Inspect Git changes | `git status --short` | `git status --short` |
| View unstaged changes | `git diff` | `git diff` |

For CMD syntax, including `cd /d`, `where`, and batch activation, use the [dedicated CMD guide](cmd.md).
