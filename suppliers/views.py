from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Drug, Supplier, State

def search_page(request):
    # Render the initial search form
    states = State.objects.all()  # Get all states to populate the filter
    return render(request, 'suppliers/search_page.html', {'states': states})

def search_drugs(request):
    # This view processes the search request
    states = State.objects.all()  # Get all states to keep the state dropdown
    drugs = Drug.objects.none()  # Initialize an empty queryset for drugs

    # Check for search parameters in the request
    drug_name = request.GET.get('drug_name', '')
    state_id = request.GET.get('state', '')

    # If the search is cleared (no parameters), return an empty result set for HTMX
    if not drug_name and not state_id:
        if request.headers.get('HX-Request'):
            return HttpResponse('')  # Empty response clears the results div
        else:
            return render(request, 'suppliers/search_page.html', {'states': states, 'drugs': drugs})

    # If there are search parameters, proceed to filter results
    if drug_name or state_id:  # If either parameter is provided
        drugs = Drug.objects.all()  # Start with all drugs

        if drug_name:
            drugs = drugs.filter(name__icontains=drug_name)  # Filter by drug name
        
        if state_id:
            drugs = drugs.filter(supplier__states__id=state_id)  # Filter by state

        # Check if the request is an HTMX request by checking for the HX-Request header
        if request.headers.get('HX-Request'):
            html = render_to_string('suppliers/drug_results.html', {'drugs': drugs, 'states': states})
            return HttpResponse(html)

    # If not HTMX request, render the search page again
    return render(request, 'suppliers/search_page.html', {'states': states, 'drugs': drugs})
    
    
def admin_page(request):
  suppliers: Supplier.objects.all()
  most_searched_drugs = Drug.objects.order_by('-search_count')[:5]
  return render(request, 'admin_page.html',{'suppliers': suppliers, 'most_searched_drugs':most_searched_drugs})
  