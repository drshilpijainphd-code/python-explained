# Windows Command Prompt (CMD) guide

[Back to the repository](../README.md)

Use these commands in **Command Prompt**, also called CMD. Open it from the Start menu or type `cmd` in File Explorer's address bar to start in the folder you are viewing.

Each section states its starting folder. Copy the commands without adding a prompt such as `C:\>`.

## Install the latest stable Python from CMD

On Windows 10 or 11, use WinGet to install the official **Python install manager**. This installs Python for your Windows account; it is not an all-users deployment.

Check WinGet, then install the manager:

```bat
winget --version
winget install --id 9NQ7512CXL7T --exact --source msstore
```

Review any prompts shown by WinGet. After installation, **close CMD and open a new CMD window**, then run:

```bat
pymanager install --update default
pymanager list
pymanager exec --version
python --version
```

With the manager's standard configuration, `default` selects the latest stable Python release. A customized default can select another version. This avoids hard-coding a release number that becomes outdated. `pymanager` also avoids conflicts with an older `py` launcher.

The first command installs the selected runtime or updates it if a newer release is available. `pymanager exec --version` verifies the managed interpreter. Compare it with `python --version` to check what your usual command runs.

These commands follow the [official Python install-manager instructions](https://www.python.org/downloads/release/pymanager-261/) and [Python's Windows documentation](https://docs.python.org/3/using/windows.html).

### Update later

Update the manager, reopen CMD, then update the selected Python runtime:

```bat
winget upgrade --id 9NQ7512CXL7T --exact --source msstore
```

In the new CMD window:

```bat
pymanager install --update default
pymanager exec --version
```

Existing virtual environments keep their own interpreter. Create a new environment when switching a project to a different Python version.

### If installation is unavailable

If `winget` is missing, install or update Microsoft's **App Installer**, then reopen CMD. Microsoft's [WinGet setup guide](https://learn.microsoft.com/en-us/windows/package-manager/winget/) links to it.

If Microsoft Store access is restricted, open the official download page from CMD and install the Python install manager available there:

```bat
start "" "https://www.python.org/downloads/windows/"
```

If `python --version` still shows an older installation, inspect command resolution:

```bat
where python
where pymanager
pymanager list
```

You can run this project's examples explicitly with the managed interpreter:

```bat
pymanager exec examples\01_hello_python.py
```

Run that last command from the repository root. It does not require removing an existing Python installation.

## Check the prerequisites

```bat
python --version
git --version
where python
where git
```

Use Python 3.11 or newer. If `python` is unavailable but the Windows Python launcher is installed, try `py --version` and substitute `py` in the commands below.

Install missing tools from the [Python website](https://www.python.org/downloads/) and [Git website](https://git-scm.com/downloads). Reopen CMD afterward so it picks up any PATH changes.

## Clone the repository

Open CMD in the parent folder where you keep your projects. This block creates a `python-projects` directory there:

```bat
cd
if not exist "python-projects" mkdir "python-projects"
cd python-projects

git clone https://github.com/drshilpijainphd-code/python-explained.git
cd python-explained
dir
```

If a command fails, stop and resolve the error before continuing. Clone only once. If the repository already exists, enter its folder instead.

From the repository root, save its location for this CMD session:

```bat
set "REPO_ROOT=%CD%"
dir README.md
dir examples
```

The `REPO_ROOT` variable is available only in the current CMD session unless you set it again.

## Navigate with cd

Start at the repository root:

```bat
cd examples
cd
python 02_temperature_converter.py

cd ..
cd docs
dir /b *.md

cd ..
```

The block ends back at the repository root. In CMD, `cd` with no argument displays the current directory. `cd ..` moves to its parent. [Microsoft's cd reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd) describes the syntax.

| Command | Purpose |
| --- | --- |
| `cd` | Display the current directory |
| `dir` | List files and folders |
| `dir /b` | Show names without the detailed listing |
| `dir /a` | Include hidden entries |
| `cd examples` | Enter examples from the repository root |
| `cd ..` | Move to the parent directory |
| `cd ..\..` | Move up two directory levels |
| `cd \` | Go to the root of the current drive |
| `cd /d "%REPO_ROOT%"` | Return to the saved repository directory, including its drive |

Each table row is a separate reference, not a sequence to run. The last row requires the `REPO_ROOT` assignment above.

### Change drives and handle spaces

Use `/d` to change the drive and directory in one command. Quote paths containing spaces. This is an illustration; replace the path with an existing folder on your machine:

```bat
cd /d "D:\Projects\Python Learning\python-explained"
```

You can also change drives with a drive letter such as `D:`, but that goes to the directory last used on that drive. `cd /d` is clearer when you know the full destination.

### Visit a folder and return

From the repository root:

```bat
pushd examples
python 10_sqlite_database.py
popd
cd
```

`pushd` saves the current directory before entering another one; `popd` returns to it. See the [Microsoft pushd reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/pushd).

## Run and inspect the examples

From the repository root:

```bat
python examples\01_hello_python.py
python examples\07_csv_sales_summary.py
python examples\11_statistics_summary.py
python examples\12_command_line_tool.py --name "Alex Morgan"
python examples\12_command_line_tool.py --help
```

To read source code in the terminal:

```bat
type examples\07_csv_sales_summary.py
```

For a longer file, use `more` to view it a page at a time:

```bat
more < docs\cmd.md
```

Press Space to advance a page or Q to quit. The [example guide](examples.md) gives the expected output for all 15 programs.

## Use an optional virtual environment

No third-party packages are required. A virtual environment is useful when you start extending the project.

From the repository root:

```bat
python -m venv .venv
call .venv\Scripts\activate.bat
python --version
where python
python examples\01_hello_python.py
deactivate
```

While activated, `where python` should list the environment's Python before other installations. `call` also makes the activation command suitable for use inside a batch file.

Activation is optional. You can invoke the environment's Python directly:

```bat
.venv\Scripts\python.exe examples\01_hello_python.py
```

The `.venv` directory is excluded by `.gitignore`. See the [Python venv documentation](https://docs.python.org/3/library/venv.html) for details.

## Run the checks

From the repository root:

```bat
python scripts\run_examples.py
python -m unittest discover -s tests -v
```

The first command should report `15/15 examples passed.` The second should report `Ran 14 tests` and `OK`.

To use the virtual environment without activating it:

```bat
.venv\Scripts\python.exe scripts\run_examples.py
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

CMD also supports `&&`, which runs the next command only when the previous one succeeds:

```bat
python scripts\run_examples.py && python -m unittest discover -s tests -v
```

Immediately after a command, inspect its exit status with:

```bat
echo %ERRORLEVEL%
```

For these Python checks, zero means success; a nonzero value means a failure.

## Inspect local changes

These commands show changes without publishing them:

```bat
git status --short
git diff --stat
git diff
```

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `python` is not recognized | Try `py --version`; otherwise install Python and reopen CMD. |
| `git` is not recognized | Install Git and reopen CMD. |
| Python reports "can't open file" | Use `cd` to check your location. From the root, use `examples\filename.py`; inside examples, use `filename.py`. |
| CMD cannot find a directory | Run `dir`, check the folder name, and quote paths containing spaces. |
| Changing to a path on another drive appears not to work | Use `cd /d "full-path"`. |
| Git says the destination already exists | Enter the existing repository instead of cloning again. |
| The environment does not activate | Use `call .venv\Scripts\activate.bat`, or run its `python.exe` directly. |
| Tests report "Ran 0 tests" | Return to the repository root and use the exact discovery command above. |
