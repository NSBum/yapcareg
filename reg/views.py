from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import RegisterForm, AddParentForm, EditParentForm

from .models import Instrument, Parent, Student, Instrument


def index(request):
    all_instruments = Instrument.objects.order_by("name")
    context = {
        "all_instruments": all_instruments,
    }
    template = loader.get_template("reg/test.html")
    return HttpResponse(template.render(context, request))


def about(request):
    context = {
        "title": "About YAPCA reg",
        "pg": "about",
    }
    template = loader.get_template("reg/about.html")
    return HttpResponse(template.render(context, request))


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "reg/register.html", {"form": form})


@login_required
def addparent(request):
    if request.method == "POST":
        form = AddParentForm(request.POST)
        if form.is_valid():
            user = request.user
            print(user.username)
            parent = Parent(user=request.user,
                            first_name=form.cleaned_data['fn'],
                            last_name=form.cleaned_data['ln'],
                            cell_phone=form.cleaned_data['cell'],
                            email=form.cleaned_data['email'],
                            address=form.cleaned_data['address_1'],
                            city=form.cleaned_data['city'],
                            province=form.cleaned_data['province'],
                            postal_code=form.cleaned_data['postal_code'],
                            should_correspond=form.cleaned_data['wants_email'])
            parent.save()
            return redirect("account")
    else:
        form = AddParentForm(initial={'wants_email': True})

    return render(request, "reg/addparent.html", {"form": form})


@login_required
def editparent(request, parent_id):
    """
    Edit a parent's information.

    This view allows an authenticated user to edit the information of a specific parent
    associated with their account. The view supports both GET and POST methods. If the
    request method is POST and the provided form data is valid, the parent's information
    is updated and the user is redirected to the account page. If the request method is GET,
    the edit form is pre-populated with the existing parent data.

    Parameters:
        request (HttpRequest): The incoming HTTP request.
        parent_id (int): The ID of the parent to be edited.

    Returns:
        HttpResponse: A rendered HTML template displaying the edit form.
                      For successful POST requests, the user is redirected to the account page.
    """

    # Retrieve the specified parent object or raise a 404 error
    parent = get_object_or_404(Parent, id=parent_id)

    if request.method == 'POST':
        # Create a ParentForm instance with POST data and the retrieved parent instance
        form = EditParentForm(request.POST)

        if form.is_valid():
            user = request.user
            # TODO: maybe make the EditParentForm a ModelForm so we don't have to do all this explicit validation
            parent.first_name = form.cleaned_data['fn']
            parent.last_name=form.cleaned_data['ln']
            parent.email = form.cleaned_data['email']
            parent.cell_phone=form.cleaned_data['cell']
            parent.address=form.cleaned_data['address_1']
            parent.city=form.cleaned_data['city']
            parent.province=form.cleaned_data['province']
            parent.postal_code=form.cleaned_data['postal_code']
            parent.should_correspond=form.cleaned_data['wants_email']
            parent.save()
            return redirect("account")
    else:
        # Create a EditParentForm instance pre-populated with the existing parent data
        form = EditParentForm(initial={
            'fn': parent.first_name,
            'ln': parent.last_name,
            'cell': parent.cell_phone,
            'email': parent.email,
            'address_1': parent.address,
            'city': parent.city,
            'province': parent.province,
            'postal_code': parent.postal_code,
            'wants_email': parent.should_correspond,
        })
    # Render the edit parent form template with the form and parent data
    return render(request, 'reg/editparent.html', {'form': form, 'parent': parent})


def account(request):
    # Access the logged-in user
    user = request.user

    # for each student, build a list of instruments
    students = Student.objects.filter(user=user)
    student_data = {}
    for student in students:
        instruments = Instrument.objects.filter(student=student)
        instrument_names = ', '.join([instrument.name for instrument in instruments])
        student_data[student.id] = instrument_names

    # Pass the user to the template context
    context = {
        "title": "YAPCA account",
        'user': user,
        'student_instrument_data': student_data
    }
    template = loader.get_template("reg/account.html")
    return HttpResponse(template.render(context, request))


def delete_parent(request, parent_id):
    item = get_object_or_404(Parent, id=parent_id)
    print(item)
    if request.method == 'POST':
        item.delete()
        return redirect('account')  # Redirect to a success page or item list page

    return redirect('account')  # Redirect to a different page if needed
