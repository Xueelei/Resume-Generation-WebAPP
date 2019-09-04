import pdfkit
import os
from pdf2image import convert_from_path
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ResumeForest.models import *
from ResumeForest.forms import *
from django.core.files import File
from ResumeForest.template import *

PDF_DIR = "./ResumeForest/migrations/PDF/"
JPG_DIR = "./ResumeForest/migrations/JPG/"

# Possible text for pisition model and location model
EDUCATION_LEVEL_TEXT = ['Bachelor', 'Master', 'PhD', 'Other']
JOB_TYPE_TEXT = ['Full Time', 'Internship', 'Part Time', 'On Campus']
POSITION_TEXT = ['Software Development Engineer', 'Machine Learning Engineer', 'Deep Learning Engineer', 'Hardware Engineer', 
                'Electrical Engineer', 'Big Data Engineer', 'Data Scientist', 'Business and Data Analyst', 'Full Stack Engineer',
                'Other']
LOCATION_TEXT = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
                 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
                 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 
                 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 
                 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
                 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Other']


@login_required
def info_collect_action(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None

    if profile == None:
        profile = Profile(user=request.user, email=request.user.email)
        profile.save()

    context = {'phone_number': profile.phone_number, 'email': profile.email,
               'educations': profile.educations.all(), 'experiences': profile.experiences.all(),
               'projects': profile.projects.all(), 'skills': profile.skills.all(),
               'education_level_text': EDUCATION_LEVEL_TEXT, 'job_type_text': JOB_TYPE_TEXT,
               'position_text': POSITION_TEXT, 'location_text': LOCATION_TEXT}
    return render(request, 'eyee_generation.html', context)


@login_required
def contact_info_update_action(request):
    print("Entering contact_info_update_action")

    profile = Profile.objects.get(user=request.user)
    profile.phone_number = request.POST['phone_number']
    profile.email = request.POST['email']
    profile.save()

    context = {'phone_number': profile.phone_number, 'email': profile.email,
               'educations': profile.educations.all(), 'experiences': profile.experiences.all(),
               'projects': profile.projects.all(), 'skills': profile.skills.all()}
    return render(request, 'eyee_generation.html', context)


@login_required
def submit_education_action(request):
    print("Entering submit_education")

    if request.method != 'POST':
        raise Http404

    # Error handling
    fields = ['school_name', 'education_level', 'major', 'start_time', 'end_time']
    message = error_handler(request, fields)
    if message != '':
        json_error = '{ "error": "' + message + '" }'
        return HttpResponse(json_error, content_type='application/json')

    # Construct new education info
    new_education = Education(school_name=request.POST['school_name'],
                              education_level=request.POST['education_level'],
                              major=request.POST['major'],
                              start_time=request.POST['start_time'],
                              end_time=request.POST['end_time'])
    new_education.save()

    profile = Profile.objects.get(user=request.user)
    profile.educations.add(new_education)
    profile.save()

    response_text = '{ "error": "' + message + '" }'
    return HttpResponse(response_text, content_type='application/json')


@login_required
def submit_experience_action(request):
    print("Entering submit_experience")

    if request.method != 'POST':
        raise Http404

    # Error handling
    fields = ['job_title', 'job_type', 'company_name', 'company_address', 'start_time', 'end_time']
    message = error_handler(request, fields)
    if message != '':
        json_error = '{ "error": "' + message + '" }'
        return HttpResponse(json_error, content_type='application/json')

    detail_list = request.POST['details'].split('|')
    detail_list.remove('')
    # Construct new experience info
    new_experience = Experience(job_title=request.POST['job_title'],
                                job_type=request.POST['job_type'],
                                company_name=request.POST['company_name'],
                                company_address=request.POST['company_address'],
                                start_time=request.POST['start_time'],
                                end_time=request.POST['end_time'])
    new_experience.save()
    for detail_text in detail_list:
        new_detail = Detail(text=detail_text)
        new_detail.save()
        new_experience.details.add(new_detail)
    new_experience.save()

    profile = Profile.objects.get(user=request.user)
    profile.experiences.add(new_experience)
    profile.save()

    response_text = '{ "error": "' + message + '" }'
    return HttpResponse(response_text, content_type='application/json')


@login_required
def submit_project_action(request):
    print("Entering submit_project")

    if request.method != 'POST':
        raise Http404

    # Error handling
    fields = ['project_title', 'organization_name', 'start_time', 'end_time']
    message = error_handler(request, fields)
    if message != '':
        json_error = '{ "error": "' + message + '" }'
        return HttpResponse(json_error, content_type='application/json')

    detail_list = request.POST['details'].split('|')
    detail_list.remove('')
    # Construct new experience info
    new_project = Project(project_title=request.POST['project_title'],
                          organization_name=request.POST['organization_name'],
                          start_time=request.POST['start_time'],
                          end_time=request.POST['end_time'])
    new_project.save()
    for detail_text in detail_list:
        new_detail = Detail(text=detail_text)
        new_detail.save()
        new_project.details.add(new_detail)
    new_project.save()

    profile = Profile.objects.get(user=request.user)
    profile.projects.add(new_project)
    profile.save()

    response_text = '{ "error": "' + message + '" }'
    return HttpResponse(response_text, content_type='application/json')


@login_required
def submit_skill_action(request):
    print("Entering submit_skill")

    if request.method != 'POST':
        raise Http404

    # Error handling
    fields = ['text']
    message = error_handler(request, fields)
    if message != '':
        json_error = '{ "error": "' + message + '" }'
        return HttpResponse(json_error, content_type='application/json')

    new_detail = Detail(text=request.POST['text'])
    new_detail.save()

    profile = Profile.objects.get(user=request.user)
    profile.skills.add(new_detail)
    profile.save()

    response_text = '{ "error": "' + message + '" }'
    return HttpResponse(response_text, content_type='application/json')


@login_required
def delete_block_action(request):
    profile = Profile.objects.get(user=request.user)
    block = int(request.POST['block'])
    block_id = int(request.POST['id'])
    print("Entering delete block " + str(block) + " of id " + str(block_id))

    if block == 1:
        education = Education.objects.get(id=block_id)
        profile.educations.remove(education)
        education.delete()
    if block == 2:
        experience = Experience.objects.get(id=block_id)
        for detail in experience.details.all():
            experience.details.remove(detail)
            detail.delete()
        profile.experiences.remove(experience)
        experience.delete()
    if block == 3:
        project = Project.objects.get(id=block_id)
        for detail in project.details.all():
            project.details.remove(detail)
            detail.delete()
        profile.projects.remove(project)
        project.delete()
    if block == 4:
        skill = Detail.objects.get(id=block_id)
        profile.skills.remove(skill)
        skill.delete()

    message = ''
    response_text = '{ "error": "' + message + '" }'
    return HttpResponse(response_text, content_type='application/json')

@login_required
def bio_generate_action(request):
    profile = Profile.objects.get(user=request.user)

    context = {'educations': profile.educations.all(), 'experiences': profile.experiences.all(),
                'projects': profile.projects.all(), 'skills': profile.skills.all(),
                'education_level_text': EDUCATION_LEVEL_TEXT, 'job_type_text': JOB_TYPE_TEXT,
                'position_text': POSITION_TEXT, 'location_text': LOCATION_TEXT, }
    return render(request, 'bio_generation.html', context)


@login_required
def resume_generate_action(request):
    context = {}
    print("Entering generate_action")

    if not os.path.isdir(PDF_DIR):
        os.mkdir(PDF_DIR)

    if not os.path.isdir(JPG_DIR):
        os.mkdir(JPG_DIR)

    # create html file
    html_filename = request.user.username + ".html"
    create_html(request, html_filename)

    # html to pdf
    pdf_filename = PDF_DIR + request.user.username + ".pdf"
    # path_wkthmltopdf = r'C:\Users\dell\Anaconda3\Lib\site-packages\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # pdfkit.from_file(html_filename, pdf_filename, configuration=config)
    pdfkit.from_file(html_filename, pdf_filename)

    # pdf to image
    jpg_filename = JPG_DIR + request.user.username + ".jpg"
    pages = convert_from_path(pdf_filename, 500)
    page = pages[0]
    page.save(jpg_filename, 'JPEG')

    position_list = []
    for position_text in request.POST.getlist('positions[]'):
        position = Position.objects.get(text=position_text)
        position_list.append(position)

    location_list = []
    for location_text in request.POST.getlist('locations[]'):
        location = Location.objects.get(text=location_text)
        location_list.append(location)

    # Check whether bio already exists
    employee = Employee.objects.get(user=request.user)
    bio_list = Employee.objects.get(user=request.user).bio_list
    new_bio = None
    for bio in bio_list.all():
        if bio.education_level != request.POST['education_level']:
            print("education_level")
            continue
        if bio.job_type != request.POST['job_type']:
            print("job_type")
            continue
        if list(bio.positions.all()) != position_list:
            print(bio.positions.all())
            print(position_list)
            print("positions")
            continue
        if list(bio.locations.all()) != location_list:
            print("locations")
            continue
        new_bio = bio
        break

    print(request.POST)
    if new_bio == None:
        print("Generating new bio")
        # If bio does not exist, create a new bio
        new_bio = Bio(user=request.user,
                      education_level=request.POST['education_level'],
                      job_type=request.POST['job_type'])
        new_bio.save()
        for position_text in request.POST.getlist('positions[]'):
            position = Position.objects.get(text=position_text)
            new_bio.positions.add(position)

        for location_text in request.POST.getlist('locations[]'):
            location = Location.objects.get(text=location_text)
            new_bio.locations.add(location)
        new_bio.save()
    else:
        print("bio already exist")
        # If bio already exists, set the previous master resume as slave
        for resume in new_bio.resume_list.all():
            if resume.master == True:
                resume.master = False
                resume.save()
        new_bio.save()

    # Construct new resume
    # save pdf into resume
    new_resume = Resume(user=request.user,
                        master=True)
    f = open(pdf_filename, 'rb')
    pdf_file = File(f)
    new_resume.file.save(pdf_filename, pdf_file)
    f.close()

    # save image into resume
    f = open(jpg_filename, 'rb')
    jpg_file = File(f)
    new_resume.picture.save(jpg_filename, jpg_file)
    f.close()

    # delete local files
    os.remove(html_filename)
    os.remove(pdf_filename)
    os.remove(jpg_filename)

    new_resume.save()

    new_bio.resume_list.add(new_resume)
    new_bio.save()

    if new_bio not in employee.bio_list.all():
        employee.bio_list.add(new_bio)
        employee.save()

    length = len(employee.bio_list.all())
    
    context = {'user': request.user, 'bio_list': employee.bio_list.all(), 'len':length}

    return render(request, 'eyee_management.html', context)

@login_required
def delete_action(request, id):
    employee = Employee.objects.get(user=request.user)
    resume = Resume.objects.get(id=id)

    for bio in employee.bio_list.all():
        if resume in bio.resume_list.all():
            bio.resume_list.remove(resume)
            bio.save()
            if len(bio.resume_list.all()) == 0:
                employee.bio_list.remove(bio)
                employee.save()
                bio.delete()
            elif resume.master:
                length = len(bio.resume_list.all())
                new_master = bio.resume_list.all()[length - 1]
                new_master.master = True
                new_master.save()

    resume.file.delete()
    resume.picture.delete()
    resume.delete()
    length = len(employee.bio_list.all())
    context = {'user': request.user, 'bio_list': employee.bio_list.all(), 'len':length}

    return render(request, 'eyee_management.html', context)

@login_required
def set_master_action(request, id):
    new_master = Resume.objects.get(id=id)
    employee = Employee.objects.get(user=request.user)

    for bio in employee.bio_list.all():
        if new_master in bio.resume_list.all():
            for resume in bio.resume_list.all():
                if resume.master:
                    resume.master = False
                    resume.save()
                    break
            break

    new_master.master = True
    new_master.save()

    length = len(employee.bio_list.all())
    context = {'user': request.user, 'bio_list': employee.bio_list.all(), 'len':length}
    return render(request, 'eyee_management.html', context)

@login_required
def get_jpg(request, id):
    resume = get_object_or_404(Resume, id=id)
    print('Picture #{} fetched from db'.format(id))

    if not resume.picture:
        raise Http404

    return HttpResponse(resume.picture, content_type='image/jpeg')


@login_required
def get_pdf(request, id):
    resume = get_object_or_404(Resume, id=id)
    print('PDF #{} fetched from db'.format(id))

    if not resume.file:
        raise Http404

    return HttpResponse(resume.file, content_type='application/pdf')


@login_required
def error_handler(request, fields):
    print("Entering error_handler")
    message = ''
    for field in fields:
        print("checking " + field)
        if not field in request.POST or not request.POST[field]:
            message = 'You must enter a ' + field
            return message
    return message