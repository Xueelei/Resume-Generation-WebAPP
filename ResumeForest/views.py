import pdfkit
import os
from pdf2image import convert_from_path
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from ResumeForest.models import *
from ResumeForest.forms import *
from django.core.files import File
from ResumeForest.resume import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from ResumeForest.tokens import account_activation_token
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


# # Possible text for pisition model and location model
# POSITION_TEXT = ['Software Development Engineer', 'Machine Learning', 'Hardware', 'Big Data']
# LOCATION_TEXT = ['New York', 'Pittsburgh', 'Washington', 'Chicago']

# Create your views here.

# Register the user
def register_action(request):
    context = {}

    # Database model setup: Position, Location
    try:
        position = Position.objects.get(id=1)
    except:
        position = None
    if position == None:
        DBSetup(request)

    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'register.html', context)

    form = RegistrationForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request, 'register.html', context)

    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['confirm_password'])
    new_user.is_active = False
    new_user.save()

    # Send confirmation email to the user
    mail_subject = 'Activate your ResumeForest Account!'
    current_site = get_current_site(request)
    message = render_to_string('acc_active_email.html', {
        'user': new_user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)).decode(),
        'token': account_activation_token.make_token(new_user),
    })
    to_email = form.cleaned_data.get('email')
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


    # Create the corresponding user types
    user_type = form.cleaned_data.get('user_type')



    if user_type == 'employer':

        new_profile = EmployerBio(user=new_user)
        new_profile.save()
        new_employer = Employer(user=new_user,
                                bio=new_profile)
        new_employer.save()


    else:
        new_employee = Employee(user=new_user)
        new_employee.save()

        profile = Profile(user=new_user, email=new_user.email)
        profile.save()
    context["success"] = True
    return render(request, "register.html", context)


# Receive confirmation and activate the user
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)


        is_employer = Employer.objects.filter(user=user)

        if len(is_employer) >= 1:
            return redirect(reverse('employer_home'))
        else:
            return redirect(reverse('employee_home'))
    else:
        return HttpResponse('Activation link is invalid!')


# Login function
def login_action(request):
    context = {}

    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'login.html', context)

    form = LoginForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
    login(request, new_user)

    employer = Employer.objects.filter(user=request.user)
    if len(employer) != 0:
        return redirect('employer_home')

    else:
        return redirect('employee_home')



def logout_action(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def employer_home_action(request):
    context = {'user': request.user}
    context['form'] = SearchForm()

    return render(request, 'eyer_search.html', context)


# Display the resume in the employer search part
@login_required
def check_resume(request, id):
    resume = get_object_or_404(Resume, id=id)

    if not resume.file:
        raise Http404

    return HttpResponse(resume.picture, content_type='image/jpeg')


# Connect the resume to the employer
def connect_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    employee_usr = resume.user

    employee = get_object_or_404(Employee, user=employee_usr)

    me = get_object_or_404(Employer, user=request.user)

    me.contact_list.add(employee)
    me.bio.link_resume.add(resume)

# Send the email to the resume's owner
def send_email(request, id):
    resume = get_object_or_404(Resume, id=id)

    employee_usr = resume.user

    employee = get_object_or_404(Employee, user=employee_usr)

    employer = get_object_or_404(Employer, user=request.user)

    notes = employer.bio.message

    myemail = employer.bio.email

    has_email = True
    try:
        validate_email(myemail)
    except ValidationError as e:
        has_email = False
    else:
        pass

    message = render_to_string('contact_email.html', {
        'message': notes,
        'email': has_email,
        'myname': request.user.first_name + ' ' + request.user.last_name,
        'education': employer.bio.education,
        'myemail': myemail,
        'company': employer.bio.company

    })

    mail_subject = "Greetings from an employer from Resume Forest!"
    to_email = employee.user.email

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


# Wrapper for connect resume and send email
@login_required
def send_interest(request, id):
    connect_resume(request, id)
    send_email(request, id)
    return employer_search_result_action(request)


# Connect all resumes in the search results
@login_required
def connect_all(request):
    context = {}
    for item in request.POST:

        if "userid" in item:
            id = request.POST[item]
            connect_resume(request, id)
            send_email(request, id)

    return redirect('employer_home')


@login_required
def employer_search_result_action(request):
    context = {'user': request.user}
    me = request.user
    employer = get_object_or_404(Employer, user=me)

    # already_connect = []
    education = request.POST['education']

    position = request.POST['position']
    location = request.POST['location']
    job_type = request.POST['type']

    contact = request.POST['contact']

    # Force every field to be filled
    if education == "Empty" or position == "Empty" or location == "Empty" or job_type=="Empty" or contact == "Empty":
        context = {'user': request.user}
        context['form'] = SearchForm()
        context['message'] = True
        return render(request, 'eyer_search.html', context)

    pos_obj = Position.objects.get(text=position)
    loc_obj = Location.objects.get(text=location)

    results = Bio.objects.filter(positions__in=[pos_obj],
                                locations__in=[loc_obj],
                                education_level=education,
                                job_type=job_type)


    r_list = []
    for bi in results:
        for r in bi.resume_list.all():
            if r.master == True:
                r_list.append(r)

    link_resume = employer.bio.link_resume.all()

    final = []
    if contact == 'Yes':
        for r in r_list:
            if r in link_resume:
                final.append(r)

    else:
        if contact == 'No':
            for r in r_list:
                if r not in link_resume:
                    final.append(r)
        else:
            final = r_list
    # number of elements
    results = final
    n = len(results)
    context["n"] = n
    context["results"] = results
    context['position'] = position
    context['location'] = location
    context['education'] = education

    return render(request, 'eyer_search_result.html', context)

@login_required
def employee_home_action(request):
    context = {}

    employee = Employee.objects.get(user=request.user)

    length = len(employee.bio_list.all())

    context = {'user': request.user, 'bio_list': employee.bio_list.all(), 'len': length}

    return render(request, 'eyee_management.html', context)

# Update employer's profile
@login_required
def employer_profile_action(request):
    context = {}
    me = get_object_or_404(EmployerBio, user=request.user)
    context['form'] = EmployerProfileForm(instance=me)

    return render(request, 'eyer_edit_profile.html', context)


def employer_update_profile(request):
    context = {}
    me = get_object_or_404(EmployerBio, user=request.user)
    form = EmployerProfileForm(request.POST, instance=me)
    if not form.is_valid():
        context['form'] = form

    else:
        form.save()
        context['form'] = form

    return render(request, 'eyer_edit_profile.html', context)

# Set up the database for stored positions and locations
def DBSetup(request):
    print("Entering DBSetup")
    for text in POSITION_TEXT:
        new_position = Position(text=text)
        new_position.save()
    for text in LOCATION_TEXT:
        new_location = Location(text=text)
        new_location.save()
