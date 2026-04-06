import subprocess
import json
from django.shortcuts import render

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
                # Run main.py with state and year arguments
                result = subprocess.run(
                    ['python', 'main.py', state, year],
                    cwd='/Users/austin/Documents/Code/wildfire-tracker',
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    wildfires = result.stdout
                else:
                    form_errors.append('Error retrieving wildfire data.')
            except Exception as e:
                form_errors.append(f'Error: {str(e)}')
    
    return render(request, 'wildfires/wildfires.html', {
        'form_data': form_data,
        'form_errors': form_errors,
        'wildfires': wildfires
    })