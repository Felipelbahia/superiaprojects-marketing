#!/usr/bin/env python3
"""Find a Chromium-based browser and run it headless (shared by brand_html.py and brand_logo_assets.py).

Standard library only (Python 3.9+). Works on macOS, Windows and Linux. The browser is used as a
renderer for local files: it prints HTML to PDF and rasterizes SVG to PNG. Nothing is downloaded
and no remote code runs; the page being rendered is a file the script just wrote.
"""
import os
import shutil
import signal
import subprocess
import sys
import tempfile
from pathlib import Path


class ChromeNotFound(RuntimeError):
    pass


def _candidates():
    plat = sys.platform
    if plat == "darwin":
        apps = ["Google Chrome", "Chromium", "Microsoft Edge", "Brave Browser"]
        for app in apps:
            yield "/Applications/%s.app/Contents/MacOS/%s" % (app, app)
            yield str(Path.home() / "Applications" / ("%s.app" % app) / "Contents" / "MacOS" / app)
    elif plat.startswith("win"):
        rels = [r"Google\Chrome\Application\chrome.exe", r"Microsoft\Edge\Application\msedge.exe",
                r"Chromium\Application\chrome.exe"]
        for var in ("ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"):
            base = os.environ.get(var)
            if base:
                for rel in rels:
                    yield os.path.join(base, rel)
    else:
        for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"):
            found = shutil.which(name)
            if found:
                yield found


def find_chrome(explicit=None):
    """Return the path of a Chromium-based browser. Order: --chrome, BRAND_CHROME, system locations."""
    tried = []
    for cand in [explicit, os.environ.get("BRAND_CHROME")]:
        if cand:
            if Path(cand).is_file():
                return cand
            tried.append(cand)
    for cand in _candidates():
        tried.append(cand)
        if Path(cand).is_file():
            return cand
    raise ChromeNotFound(
        "Chrome, Chromium ou Edge não encontrado. Instale um deles ou indique o caminho com "
        "--chrome <caminho> (ou a variável BRAND_CHROME). Locais procurados: %s" % "; ".join(tried or ["nenhum"]))


def _kill_tree(proc):
    """Stop the browser and the helper processes it started (a plain kill leaves the helpers running)."""
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGKILL)
        else:
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True)
    except (OSError, ProcessLookupError):
        proc.kill()


def run_headless(chrome, args, timeout=None):
    """Run the browser headless with a throwaway profile. Returns the CompletedProcess.

    Raises RuntimeError when the browser does not finish in time (default 120 s, or BRAND_CHROME_TIMEOUT).
    """
    timeout = timeout or int(os.environ.get("BRAND_CHROME_TIMEOUT", "120"))
    profile = tempfile.mkdtemp(prefix="brand-chrome-")
    try:
        cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
               "--no-default-browser-check", "--force-device-scale-factor=1",
               "--user-data-dir=%s" % profile] + list(args)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=(os.name == "posix"))
        try:
            out, err = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            _kill_tree(proc)
            proc.communicate()
            raise RuntimeError("O navegador não terminou em %d s (máquina sobrecarregada?). Tente de novo, aumente o limite com "
                               "BRAND_CHROME_TIMEOUT=<segundos> ou use outro navegador com --chrome." % timeout)
        return subprocess.CompletedProcess(cmd, proc.returncode, out, err)
    finally:
        shutil.rmtree(profile, ignore_errors=True)  # a locked file on Windows must not hide the real result


def file_url(path):
    return Path(path).resolve().as_uri()
