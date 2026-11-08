import subprocess
import sys
from pathlib import Path

from django.shortcuts import render


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def wildfires_list(request):
    form_data = {}
    form_errors = []
    wildfires = None

    if request.GET:
        state = request.GET.get('state', '').strip()
        year = request.GET.get('year', '').strip()

        form_data = {'state': state, 'year': year}

        if not state or not year:
            form_errors.append('Both state and year are required.')
        else:
            try:
                project_root = _project_root()
                script_path = project_root / 'main.py'
                result = subprocess.run(
                    [sys.executable, str(script_path), state, year],
                    cwd=str(project_root),
                    capture_output=True,
                    text=True,
                    check=False,
                )

                if result.returncode == 0:
                    wildfires = result.stdout
                else:
                    form_errors.append(
                        f'Error retrieving wildfire data: {result.stderr.strip() or result.stdout.strip() or "unknown error"}'
                    )
            except Exception as e:
                form_errors.append(f'Error: {str(e)}')

    return render(request, 'wildfires/wildfires.html', {
        'form_data': form_data,
        'form_errors': form_errors,
        'wildfires': wildfires
    })