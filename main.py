import uvicorn, subprocess
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI(title="GUI for power modes")
balanced_script = "balanced.sh"
power_save_script = "power-saver.sh"
power_mode = "powerprofilesctl get"

@app.get("/balanced")
async def balanced():
    """
    Switches to balanced power mode by running the balanced.sh script.
    Returns a message indicating the mode change.
    """
    subprocess.run(f"/run/media/roman/Files/Python/pythonPowerModsKDE/{balanced_script}", shell=True)
    return {"message": "Balanced mode"}

@app.get("/power_save")
async def power_save():
    """
    Switches to power save mode by running the power-saver.sh script.
    Returns a message indicating the mode change.
    """
    subprocess.run(f"/run/media/roman/Files/Python/pythonPowerModsKDE/{power_save_script}", shell=True)
    return {"message": "Power save mode"}

@app.get("/power_mode")
async def get_power_mode():
    """
    Retrieves the current power mode by running the powerprofilesctl get command.
    Returns the power mode as a string.
    """
    res = subprocess.run(power_mode, capture_output=True, text=True, shell=True)
    out = res.stdout
    return {"power mode": out}

@app.get("/github")
async def github_link():
    """
    Redirects to the GitHub repository of the project.
    """
    return RedirectResponse("https://github.com/CodeCraftsman89")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
