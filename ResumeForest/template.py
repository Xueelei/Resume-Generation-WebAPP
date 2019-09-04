from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ResumeForest.models import *

@login_required
def create_html(request, html_filename):
    print(request.POST)

    message = get_message(request, int(request.POST['template']))
    f = open(html_filename,'w')
    f.write(message)
    f.close()

@login_required
def get_message(request, template):
    profile = Profile.objects.get(user=request.user)
    phone_number = profile.phone_number
    email = profile.email

    educations = []
    experiences = []
    projects = []
    skills = []
    if 'educations' in request.POST:
        educations = Education.objects.filter(id__in=request.POST.getlist('educations'))
    if 'experiences' in request.POST:
        experiences = Experience.objects.filter(id__in=request.POST.getlist('experiences'))
    if 'projects' in request.POST:
        projects = Project.objects.filter(id__in=request.POST.getlist('projects'))
    if 'skills' in request.POST:
        skills = Detail.objects.filter(id__in=request.POST.getlist('skills'))
        
    if template == 1:
        message = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <title>Resume | """ + request.user.first_name + """ """ + request.user.last_name + """</title>
    <meta name="robots" content="noindex, nofollow" />
    <style type="text/css" media="all">
        html{ background-color:#EEE; padding:0 1em; }
        body { background-color:#FFF; font-family:"Trebuchet MS", Helvetica, Arial; padding:1em; border:solid #AAA; border-width:1px 3px 3px 1px; margin:1em auto; max-width: 50em; }
        #address{ height:5em; width:47em; margin:1em 0 1em 0; }
        #address div{ width:45em; float:left; padding:0 .5em 0 1.5em; border-left:1px solid #CCC; }
        #address div#first{ border-left:none; }
        #address h3{ border-bottom: none; margin-top: 0; }   
        .date { float:right; font-size:.8em; margin-top:.4em; text-align:right; }
        abbr, acronym{ border-bottom:1px dotted #333; cursor:help; }   
        address{ font-style:italic; color:#333; font-size:.9em; }
        .name{ font-size:1.8em; font-family: Helvetica, Verdana, Arial, sans-serif; }
        .contact{ margin: 1em 0 0 0; }
        h2 { clear:both; font-size: 1.4em; font-weight:bold; margin-top:.5em; font-variant: small-caps; padding-left:.25em; background-color:#EEE; border-bottom: 1px solid #999; letter-spacing: .06em; }
        h3 {margin: 1em 0 0 0;}
    </style>
    <style type="text/css" media="print">
        body { background-color:#FFF; border-width:0 0 0 0; margin:0; width:100% }
    </style>
</head>
<body>
    <span class="name">""" + request.user.first_name + """ """ + request.user.last_name + """</span> <br>
        <span>Phone: """ +  phone_number + """   |   </span>
        <span>Email: """ + email + """</a></span>"""

        message += "<h2>Educations</h2>"
        for education in educations:
            message += "<span class=\"date\">" + education.start_time + " &raquo; " + education.end_time + "</span>"
            message += "<h3>" + education.school_name + "</h3>"
            message += "<address>" + education.education_level + " of " + education.major + "</address>"
    
        message += "<h2>Experiences</h2>"
        for experience in experiences:
            message += "<span class=\"date\">" + experience.start_time + " &raquo; " + experience.end_time + "</span>"
            message += "<h3>" + experience.job_title + "</h3>"
            message += "<address>" + experience.company_name + ", " + experience.company_address + "</address>"
            message += "<ul>"
            for detail in experience.details.all():
                message += "<li>" + detail.text + "</li>"
            message += "</ul>"
        
        message += "<h2>Projects</h2>"
        for project in projects:
            message += "<span class=\"date\">" + project.start_time + " &raquo; " + project.end_time + "</span>"
            message += "<h3>" + project.project_title + "</h3>"
            message += "<address>" + project.organization_name + "</address>"
            message += "<ul>"
            for detail in project.details.all():
                message += "<li>" + detail.text + "</li>"
            message += "</ul>"

        message += "<h2>Skills</h2>"
        message += "<ul>"
        for skill in skills:
            message += "<li>" + skill.text + "</li>"
        message += "</ul>"
        
        message += "</body></html>"

        return message

    if template == 2:
        message = """<html>
<head>
<title>Resume | """ + request.user.first_name + """ """ + request.user.last_name + """</title>

<meta name="viewport" content="width=device-width"/>
<meta name="description" content="The Curriculum Vitae of Joe Bloggs."/>
<meta charset="UTF-8"> 

<link href='http://fonts.googleapis.com/css?family=Rokkitt:400,700|Lato:400,300' rel='stylesheet' type='text/css'>

<style type="text/css" rel="stylesheet"  media="all">

html,body,div,span,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,abbr,address,cite,code,del,dfn,em,img,ins,kbd,q,samp,small,strong,sub,sup,var,b,i,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,figcaption,figure,footer,header,hgroup,menu,nav,section,summary,time,mark,audio,video 
{ border:0; font:inherit; font-size:100%; margin:0; padding:0; vertical-align:baseline; }
article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section { display:block; }
html, body {background: #181818; font-family: 'Lato', helvetica, arial, sans-serif; font-size: 16px; color: #222;}
.clear {clear: both;}
p { font-size: 1em; line-height: 1.4em; margin-bottom: 20px; color: #444; }
#cv { width: 90%; max-width: 800px; background: #f3f3f3; margin: 30px auto; }
.mainDetails { padding: 25px 35px; border-bottom: 2px solid #cf8a05; background: #ededed; }
#name h1 { font-size: 2.5em; font-weight: 700; font-family: 'Rokkitt', Helvetica, Arial, sans-serif; margin-bottom: -6px; }
#name h2 { font-size: 1.3em; margin-left: 2px; font-family: 'Rokkitt', Helvetica, Arial, sans-serif; }
#mainArea { padding: 0 40px; }
#headshot { width: 12.5%; float: left; margin-right: 30px; }
#headshot img { width: 100%; height: auto; -webkit-border-radius: 50px; border-radius: 50px }
#name { float: left; }
#contactDetails { float: right; } 
#contactDetails ul { list-style-type: none; font-size: 0.9em; margin-top: 2px; }
#contactDetails ul li { margin-bottom: 3px; color: #444; }
#contactDetails ul li a, a[href^=tel] { color: #444;  text-decoration: none; -webkit-transition: all .3s ease-in; -moz-transition: all .3s ease-in; -o-transition: all .3s ease-in; -ms-transition: all .3s ease-in; transition: all .3s ease-in }
#contactDetails ul li a:hover { color: #cf8a05; }
section { border-top: 1px solid #dedede; padding: 20px 0 0; }
section:first-child { border-top: 0; }
section:last-child { padding: 20px 0 10px;}
.sectionTitle { float: left; width: 25%; }
.sectionContent { float: right; width: 72.5%; }
.sectionTitle h1 { font-family: 'Rokkitt', Helvetica, Arial, sans-serif; font-style: italic; font-size: 1.5em; color: #cf8a05; }
.sectionContent h2 { font-family: 'Rokkitt', Helvetica, Arial, sans-serif; font-size: 1.5em; margin-bottom: -2px; }
.subDetails { font-size: 0.8em; font-style: italic; margin-bottom: 3px; }
.keySkills { list-style-type: none; -moz-column-count:3; -webkit-column-count:3; column-count:3; margin-bottom: 20px; font-size: 1em; color: #444; }
.keySkills ul li { margin-bottom: 3px; }
@media all and (min-width: 602px) and (max-width: 800px) {
    #headshot { display: none; } 
    .keySkills { -moz-column-count:2; -webkit-column-count:2; column-count:2; }
}
@media all and (max-width: 601px) {
    #cv { width: 95%; margin: 10px auto; min-width: 280px; }
    #headshot { display: none;}
    #name, #contactDetails { float: none; width: 100%; text-align: center; }
    .sectionTitle, .sectionContent { float: none; width: 100%; }
    .sectionTitle { margin-left: -2px; font-size: 1.25em; }
    .keySkills { -moz-column-count:2; -webkit-column-count:2; column-count:2; }
}
@media all and (max-width: 480px) {
    .mainDetails { padding: 15px 15px; }
    section { padding: 15px 0 0; }
    #mainArea { padding: 0 25px; }
    .keySkills { -moz-column-count:1; -webkit-column-count:1; column-count:1; }
    #name h1 { line-height: .8em; margin-bottom: 4px; }
}
</style>
</head>

<body id="top">
<div id="cv">
    <div class="mainDetails">
        <div id="name">
            <h1>""" + request.user.first_name + """ """ + request.user.last_name + """</h1>
            <h2> Seeking for """ + request.POST['job_type'] + """</h2>
        </div>
        
        <div id="contactDetails">
            <ul>
                <li>e: <a href=mailto:\"""" + email + """\" target="_blank">""" + email + """</a></li>
                <li>m: """ + phone_number +  """</li>
            </ul>
        </div>
        <div class="clear"></div>
    </div>
    
    <div id="mainArea">
        
        <section>
            <div class="sectionTitle"> <h1>Experience</h1> </div>
            <div class="sectionContent">"""

        for experience in experiences:
            message += "<article>"
            message += "<h2>" + experience.job_title + " at " + experience.company_name + "</h2>"
            message += "<p class=\"subDetails\">" + experience.start_time +  " - " + experience.end_time + "</p>"
            message += "<ul class=\"keySkills\">"
            for detail in experience.details.all():
                message += "<li>" + detail.text + "</li>"
            message += "</ul></article>"

        message += """<div class="clear"></div>
            </section>
            <section>
                <div class="sectionTitle"> <h1>Project</h1> </div>
                <div class="sectionContent">"""

        for project in projects:
            message += "<article>"
            message += "<h2>" + project.project_title + " at " + project.organization_name + "</h2>"
            message += "<p class=\"subDetails\">" + project.start_time +  " - " + project.end_time + "</p>"
            message += "<ul class=\"keySkills\">"
            for detail in project.details.all():
                message += "<li>" + detail.text + "</li>"
            message += "</ul></article>"

        message += """<div class="clear"></div>
            </section>
            <section>
                <div class="sectionTitle">
                    <h1>Education</h1>
                </div>
                
                <div class="sectionContent">"""

        for education in educations:
            message += "<article>"
            message += "<h2>" + education.school_name + "</h2>"
            message += "<p class=\"subDetails\">" + education.start_time + " - " + education.end_time + "</p>"
            message += "<p>" + education.education_level + " of " + education.major + "</p>"
            message += "</article>"

        message += """
            </div>
            <div class="clear"></div>
        </section>
        
        <section>
            <div class="sectionTitle">
                <h1>Key Skills</h1>
            </div>
            
            <div class="sectionContent">
                <ul class="keySkills">"""

        for skill in skills:
            message += "<li>" + skill.text + "</li>"

        message += """</ul>
            </div>
            <div class="clear"></div>
        </section>
        
    </div>
</div>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-3753241-1");
pageTracker._initData();
pageTracker._trackPageview();
</script>
</body>
</html>"""
        return message

    if template == 3:
        message = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>

    <title>Resume | """ + request.user.first_name + """ """ + request.user.last_name + """</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.7.0/build/reset-fonts-grids/reset-fonts-grids.css" media="all" /> 
    <style type="text/css">
        .msg { padding: 10px; background: #222; position: relative; }
        .msg h1 { color: #fff;  }
        .msg a { margin-left: 20px; background: #408814; color: white; padding: 4px 8px; text-decoration: none; }
        .msg a:hover { background: #266400; }
        body { font-family: Georgia; color: #444; }
        #inner { padding: 10px 80px; margin: 80px auto; background: #f5f5f5; border: solid #666; border-width: 8px 0 2px 0; }
        .yui-gf { margin-bottom: 2em; padding-bottom: 2em; border-bottom: 1px solid #ccc; }
        #hd { margin: 2.5em 0 3em 0; padding-bottom: 1.5em; border-bottom: 1px solid #ccc }
        #hd h2 { text-transform: uppercase; letter-spacing: 2px; }
        #bd, #ft { margin-bottom: 2em; }
        #ft { padding: 1em 0 5em 0; font-size: 92%; border-top: 1px solid #ccc; text-align: center; }
        #ft p { margin-bottom: 0; text-align: center;   }
        #hd h1 { font-size: 48px; text-transform: uppercase; letter-spacing: 3px; }
        h2 { font-size: 152% }
        h3, h4 { font-size: 122%; }
        h1, h2, h3, h4 { color: #333; }
        p { font-size: 100%; line-height: 18px; padding-right: 3em; }
        a { color: #990003 }
        a:hover { text-decoration: none; }
        strong { font-weight: bold; }
        li { line-height: 24px; border-bottom: 1px solid #ccc; }
        p.enlarge { font-size: 144%; padding-right: 6.5em; line-height: 24px; }
        p.enlarge span { color: #000 }
        .contact-info { margin-top: 7px; }
        .first h2 { font-style: italic; }
        .last { border-bottom: 0 }
        a#pdf { display: block; float: left; background: #666; color: white; padding: 6px 50px 6px 12px; margin-bottom: 6px; text-decoration: none;  }
        a#pdf:hover { background: #222; }
        .job { position: relative; margin-bottom: 1em; padding-bottom: 1em; border-bottom: 1px solid #ccc; }
        .job h4 { position: absolute; top: 0.35em; right: 0 }
        .job p { margin: 0.75em 0 0 0; }
        .last { border: none; }
        .skills-list {  }
        .skills-list ul { margin: 0; }
        .skills-list li { margin: 3px 0; padding: 3px 0; }
        .skills-list li span { font-size: 152%; display: block; margin-bottom: -2px; padding: 0 }
        .talent { width: 32%; float: left }
        .talent h2 { margin-bottom: 6px; }
        #srt-ttab { margin-bottom: 100px; text-align: center;  }
        #srt-ttab img.last { margin-top: 20px }
        .yui-gf .yui-u{width:80.2%;}
        .yui-gf div.first{width:12.3%;}
    </style>
</head>
<body>

<div id="doc2" class="yui-t7">
    <div id="inner">
    
        <div id="hd">
            <div class="yui-gc">
                <div class="yui-u first">
                    <h1>""" + request.user.first_name + """ """ + request.user.last_name + """</h1>
                </div>

                <div class="yui-u">
                    <div class="contact-info">
                        <h3><a href=mailto:\"""" + email + """\">""" + email + """</a></h3>
                        <h3>""" + phone_number + """</h3>
                    </div>
                </div>
            </div>
        </div>

        <div id="bd">
            <div id="yui-main">
                <div class="yui-b">

                    <div class="yui-gf">
                        <div class="yui-u first">
                            <h2>Skills</h2>
                        </div>
                        <div class="yui-u">"""
        for skill in skills:
            message += "<p>" + skill.text + "</p>"

        message += """</div>
                    </div>

                    <div class="yui-gf">
    
                        <div class="yui-u first">
                            <h2>Experience</h2>
                        </div>
                        <div class="yui-u">"""

        experience_last = None
        if experiences != []:
            experience_last = experiences[len(experiences) - 1]

        for experience in experiences:
            if experience == experience_last:
                message += "<div class=\"job last\">"
            else:
                message += "<div class=\"job\">"
            message += "<h2>" + experience.job_type + " of " + experience.job_title + "</h2>"
            message += "<h3>" + experience.company_name + "</h3>"
            message += "<h4>" + experience.start_time + " - " + experience.end_time + "</h4>"
            for detail in experience.details.all():
                message += "<p>" + detail.text + "</p>"
            message += "</div>"

        message += """
                        </div>
                    </div>

                    <div class="yui-gf">
    
                        <div class="yui-u first">
                            <h2>Project</h2>
                        </div>
                        <div class="yui-u">"""

        project_last = None
        if projects != []:
            project_last = projects[len(projects) - 1]

        for project in projects:
            if project == project_last:
                message += "<div class=\"job last\">"
            else:
                message += "<div class=\"job\">"
            message += "<h2>" + project.project_title + "</h2>"
            message += "<h4>" + project.start_time + " - " + project.end_time + "</h4>"
            for detail in project.details.all():
                message += "<p>" + detail.text + "</p>"
            message += "</div>"

        message += """
                        </div>
                    </div>
                    <div class="yui-gf last">
                        <div class="yui-u first">
                            <h2>Education</h2>
                        </div>"""
        for education in educations:
            message += "<div class=\"yui-u\">"
            message += "<h2>" + education.school_name + "</h2>"
            message += "<h3>" + education.education_level + " of " + education.major + "</h3>"
            message += "</div>"

        message += """</div>
                </div>
            </div>
        </div>
        <div id="ft">
            <p>""" +  request.user.first_name + """ """ + request.user.last_name + " &mdash; <a href=\"mailto:" + email + "\">" + email + "</a> &mdash; " + phone_number + """</p>
        </div>
    </div>
</div>
</body>
</html>"""
        return message





