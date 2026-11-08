import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

from django.shortcuts import render


def _import_root_main_module():
    root = Path(__file__).resolve().parents[3]
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    import main as root_main
    return root_main


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
                root_main = _import_root_main_module()
                stdout = io.StringIO()
                with redirect_stdout(stdout):
                    root_main.main(state, year)
                wildfires = stdout.getvalue().strip()
            except Exception as e:
                form_errors.append(f'Error retrieving wildfire data: {str(e)}')

    return render(request, 'wildfires/wildfires.html', {
        'form_data': form_data,
        'form_errors': form_errors,
        'wildfires': wildfires
    })