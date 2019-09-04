// Options for time period
OP_MONTH = option_month();
OP_YEAR = option_year();

// Inner html for education card        
HTML_EDU = "<div class=\"school_name\">" +
                "<div class='card-label'>School Name: </div>" +
                "<input class= 'card-input-js' id = \"id_school_name\" name = \"school_name\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"education_level\">" +
                "<div class='card-label'>Education Level: </div>" +
                "<select class= 'card-input-js' id = \"id_education_level\" name = \"job_type\">" +
                	"<option value=\"Bachelor\">Bachelor</option>" +
                	"<option value=\"Master\">Master</option>" +
                	"<option value=\"PHD\">PHD</option>" +
                "</select>" +
            "</div>" +
            "<div class=\"major\">" +
                "<div class='card-label'>Major: </div>" +
                "<div><input class= 'card-input-js' id = \"id_major\" name = \"major\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"time_period\">" +
                "<div class='card-label'>Start Time: </div>" +
                "<select class= 'card-input-js' id=\"id_edu_start_time_month\" name=\"edu_start_time_month\">" + OP_MONTH + "</select>" +
                "<select class= 'card-input-js' id=\"id_edu_start_time_year\" name=\"edu_start_time_year\">" + OP_YEAR + "</select>" +
                "<br>" +
                "<div class='card-label'>End Time: </div>" +
                "<select class= 'card-input-js' id=\"id_edu_end_time_month\" name=\"edu_end_time_month\">" + OP_MONTH + "</select>" +
                "<select class= 'card-input-js' id=\"id_edu_end_time_year\" name=\"edu_end_time_year\">" + OP_YEAR + "</select>" +
            "</div>" +
            "<br>"+
            "<div class='container-login100-form-btn'>"+
            "<button class=\"login100-form-btn\" id=\"id_education_discard_button\" name = \"education_discard_button\" onclick=\"discard(1)\" type=\"button\">"+
            "Discard"+
            "</button>"+
            "&nbsp;"+
            "<button class=\"login100-form-btn\" id=\"id_education_submit_button\" name = \"education_submit_button\" onclick=\"submitEducation()\" type=\"button\">"+
            "Submit"+
            "</button>"+
            "</div>";

// Inner html for experience card
HTML_EXP = "<div class=\"job_title\">" +
                "<div class='card-label'>Job Title: </div>" +
                "<div><input class= 'card-input-js' id = \"id_job_title\" name = \"job_title\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"job_type\">" +
                "<div class='card-label'>Job Type: </div>" +
                "<select class= 'card-input-js' id = \"id_job_type\" name = \"job_type\">" +
                	"<option value=\"Full time\">full time</option>" +
                	"<option value=\"Internship\">internship</option>" +
                	"<option value=\"Research\">research</option>" +
                "</select>" +
            "</div>" +
            "<div class=\"company_name\">" +
                "<div class='card-label'>Company Name: </div>" +
                "<div><input class= 'card-input-js' id = \"id_company_name\" name = \"company_name\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"company_address\">" +
                "<div class='card-label'>Company Address: </div>" +
                "<div><input class= 'card-input-js' id = \"id_company_address\" name = \"company_address\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"time_period\">" +
                "<div class='card-label'>Start Time: </div>" +
                "<select class= 'card-input-js' id=\"id_exp_start_time_month\" name=\"exp_start_time_month\">" + OP_MONTH + "</select>" +
                "<select class= 'card-input-js' id=\"id_exp_start_time_year\" name=\"exp_start_time_year\">" + OP_YEAR + "</select>" +
                "<br>" +
                "<div class='card-label'>End Time: </div>" +
                "<select class= 'card-input-js' id=\"id_exp_end_time_month\" name=\"exp_end_time_month\">" + OP_MONTH + "</select>" +
                "<select class= 'card-input-js' id=\"id_exp_end_time_year\" name=\"exp_end_time_year\">" + OP_YEAR + "</select>" +
            "</div>" +
            "<div class=\"details\">" +
                "<div class='card-label'>Details: </div>" +
                "<ul style=\"margin:auto\" id=\"id_experience_detail\"></ul>" +
                "<button class=\"glyphicon glyphicon-pencil\" onclick=\"addDetails(2)\" type=\"button\"></button>" +
            "</div>" +
            "<br>"+
            "<div class='container-login100-form-btn'>"+
            "<button class=\"login100-form-btn\" id=\"id_education_discard_button\" name = \"education_discard_button\" onclick=\"discard(2)\" type=\"button\">"+
            "Discard"+
            "</button>"+
            "&nbsp;"+
            "<button class=\"login100-form-btn\" id = \"id_experience_submit_button\" name = \"experience_submit_button\" onclick=\"submitExperience()\" type=\"button\">"+
            "Submit"+
            "</button>"+
            "</div>";
            

// Inner html for project card
HTML_PRJ = "<div class=\"project_title\">" +
                "<div class='card-label'>Project Title: </div>" +
                "<div><input class= 'card-input-js' id = \"id_project_title\" name = \"project_title\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"organization_name\">" +
                "<div class='card-label'>Organization Name: </div>" +
                "<div><input class= 'card-input-js' id = \"id_organization_name\" name = \"organization_name\" type = \"text\"></div>" +
            "</div>" +
            "<div class=\"time_period\">" +
                "<div class='card-label'>Start Time: </div>" +
                "<select class= 'card-input-js' id=\"id_prj_start_time_month\" name=\"prj_start_time_month\">" + OP_MONTH + "</select>" +
                "<select class= 'card-input-js' id=\"id_prj_start_time_year\" name=\"prj_start_time_year\">" + OP_YEAR + "</select>" +
                "<br>" +
                "<div class='card-label'>End Time: </div>" +
                "<select class= 'card-input-js' id=\"id_prj_end_time_month\" name=\"prj_end_time_month\">" + OP_MONTH + "</select>" +
                "<select class= 'card-input-js' id=\"id_prj_end_time_year\" name=\"prj_end_time_year\">" + OP_YEAR + "</select>" +
            "</div>" +
            "<div class=\"details\">" +
                "<div class='card-label'>Details: </div>" +
                "<ul id=\"id_project_detail\"></ul>" +
                "<button class=\"glyphicon glyphicon-pencil\" onclick=\"addDetails(3)\" type=\"button\"></button>" +
            "</div>" +

            
            "<br>"+
            "<div class='container-login100-form-btn'>"+
            "<button class=\"login100-form-btn\" id=\"id_education_discard_button\" name = \"education_discard_button\" onclick=\"discard(3)\" type=\"button\">"+
            "Discard"+
            "</button>"+
            "&nbsp;"+
            "<button class=\"login100-form-btn\" id = \"id_project_submit_button\" name = \"project_submit_button\" onclick=\"submitProject()\" type=\"button\">"+
            "Submit"+
            "</button>"+
            "</div>";

// Inner html for project card
HTML_SKL = "<div class=\"text\">" +
                "<div><input class= 'card-input-js' id = \"id_text\" name = \"text\" type = \"text\"></div>" +
            "</div>" +
            
            "<br>"+
            "<div class='container-login100-form-btn'>"+
            "<button class=\"login100-form-btn\" id=\"id_education_discard_button\" name = \"education_discard_button\" onclick=\"discard(4)\" type=\"button\">"+
            "Discard"+
            "</button>"+
            "&nbsp;"+
            "<button class=\"login100-form-btn\" id = \"id_skill_submit_button\" name = \"skill_submit_button\" onclick=\"submitSkill()\" type=\"button\">"+
            "Submit"+
            "</button>"+
            "</div>";


function option_month(){
	var abbr = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"];
	var full = ["January", "February", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"];
	var month = "";
	for(var i = 0; i < 12; i++){
		month = month.concat("<option value=\"" + abbr[i] + "\">" + full[i] + "</option>\n");
	}
	return month;
}

function option_year(){
	var year = "";
	for(var i = 2025; i >= 1961; i--){
		year = year.concat("<option value=\"" + i.toString() + "\">" + i.toString() + "</option>")
	}
	return year;
}

function contact_info_update(){
	console.log("Entering contact_info_update");
	var phone_number_value = document.getElementById("id_phone_number").value;
	var email_value = document.getElementById("id_email").value;

	// Construct new request
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState != 4) return;
        if (req.status != 200) return;
        console.log("contact_update_message")
        //window.location.reload();
        console.log("contact_update_message")
        var message = document.getElementById("contact_update_message");
        while(message.hasChildNodes()){
        	message.removeChild(message.firstChild);
        }
        var new_msg = document.createElement("div");
        new_msg.innerHTML = "Successfully updated!"
        message.appendChild(new_msg);
    }

    req.open("POST", "contact_info_update", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("phone_number=" + phone_number_value
    		+ "&email=" + email_value
    		+ "&csrfmiddlewaretoken=" + getCSRFToken());
}

function add(block){
	console.log("Entering add");
	var list_id;
	var newHTML = document.createElement("li");
	switch(block){
		case 1:
			list_id = "id_education_add";
			newHTML.innerHTML = HTML_EDU;
			break;
		case 2:
			list_id = "id_experience_add";
			newHTML.innerHTML = HTML_EXP;
			break;
		case 3:
			list_id = "id_project_add";
			newHTML.innerHTML = HTML_PRJ;
			break;
		case 4:
			list_id = "id_skill_add";
			newHTML.innerHTML = HTML_SKL;
	}

    var list = document.getElementById(list_id);
    // check whether there is remaining add block
    if(list.hasChildNodes()) return ;

    list.appendChild(newHTML);
}

function addDetails(block){
	console.log("Entering addDetails");
	var list_id;
	var newDetail = document.createElement("li");
	switch(block){
		case 2:
			list_id = "id_experience_detail";
			newDetail.innerHTML = "<input class= 'card-input-js' id = \"id_detail\" name = \"experience_detail\" type = \"text\">";
			break;
		case 3:
			list_id = "id_project_detail";
			newDetail.innerHTML = "<input class= 'card-input-js' id = \"id_detail\" name = \"project_detail\" type = \"text\">";
			break;
	}
	var list = document.getElementById(list_id);
    list.appendChild(newDetail)
}

function discard(block){
    console.log("Entering discard");
    var list_id;
    switch(block){
        case 1:
            list_id = "id_education_add";
            break;
        case 2:
            list_id = "id_experience_add";
            break;
        case 3:
            list_id = "id_project_add";
            break;
        case 4:
            list_id = "id_skill_add";
    }

    var list = document.getElementById(list_id);

    // discard edit card
    while(list.hasChildNodes()){
        list.removeChild(list.firstChild);
    }

}

function submitEducation(){
	console.log("Entering submitEducation");
	// Get value for each field
    var school_name_value = document.getElementById("id_school_name").value;
    var education_level_value = document.getElementById("id_education_level").value;
    var major_value = document.getElementById("id_major").value;
    var start_time_value = document.getElementById("id_edu_start_time_month").value 
                           + " " + document.getElementById("id_edu_start_time_year").value;
    var end_time_value = document.getElementById("id_edu_end_time_month").value 
                           + " " + document.getElementById("id_edu_end_time_year").value;

    // Construct new request
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState != 4) return;
        if (req.status != 200) return;
        var response = JSON.parse(req.responseText);
        if (response.error == "") {
            window.location.reload();
        } else {
            displayError(response.error, "education");
        }
    }

    req.open("POST", "submit_education", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("school_name=" + school_name_value
    		+ "&education_level=" + education_level_value
    		+ "&major=" + major_value
    		+ "&start_time=" + start_time_value
    		+ "&end_time=" + end_time_value
    		+ "&csrfmiddlewaretoken=" + getCSRFToken());

}

function del(block, id){
	console.log("Entering delete");

	var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState != 4) return;
        if (req.status != 200) return;
        var response = JSON.parse(req.responseText);
        if (response.error == "") {
            window.location.reload();
        } else {
            displayError(response.error, "education");
        }
    }

    req.open("POST", "delete_block", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("block=" + block.toString()
    		+ "&id=" + id.toString()
    		+ "&csrfmiddlewaretoken=" + getCSRFToken());
}

function submitExperience(){
	console.log("Entering submitExperience");
	// Get value for each field
    var job_title_value = document.getElementById("id_job_title").value;
    var job_type_value = document.getElementById("id_job_type").value;
    var company_name_value = document.getElementById("id_company_name").value;
    var company_address_value = document.getElementById("id_company_address").value;
    var start_time_value = document.getElementById("id_exp_start_time_month").value 
                           + " " + document.getElementById("id_exp_start_time_year").value;
    var end_time_value = document.getElementById("id_exp_end_time_month").value 
                           + " " + document.getElementById("id_exp_end_time_year").value;
    var details = document.getElementsByName("experience_detail");
    var details_value = "";
    for(var i = 0; i < details.length; i++){
    	details_value = details_value.concat(details[i].value + "|");
    }

    // Construct new request
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState != 4) return;
        if (req.status != 200) return;
        var response = JSON.parse(req.responseText);
        if (response.error == "") {
            window.location.reload();
        } else {
            displayError(response.error, "experience");
        }
    }

    req.open("POST", "submit_experience", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("job_title=" + job_title_value
    		+ "&job_type=" + job_type_value
    		+ "&company_name=" + company_name_value
    		+ "&company_address=" + company_address_value
    		+ "&start_time=" + start_time_value
    		+ "&end_time=" + end_time_value
    		+ "&details=" + details_value
    		+ "&csrfmiddlewaretoken=" + getCSRFToken());

}

function submitProject(){
	console.log("Entering submitProject");
	// Get value for each field
    var project_title_value = document.getElementById("id_project_title").value;
    var organization_name_value = document.getElementById("id_organization_name").value;
    var start_time_value = document.getElementById("id_prj_start_time_month").value 
                           + " " + document.getElementById("id_prj_start_time_year").value;
    var end_time_value = document.getElementById("id_prj_end_time_month").value 
                           + " " + document.getElementById("id_prj_end_time_year").value;
    var details = document.getElementsByName("project_detail");
    var details_value = "";
    for(var i = 0; i < details.length; i++){
    	details_value = details_value.concat(details[i].value + "|");
    }

    // Construct new request
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState != 4) return;
        if (req.status != 200) return;
        var response = JSON.parse(req.responseText);
        if (response.error == "") {
            window.location.reload();
        } else {
            displayError(response.error, "project");
        }
    }

    req.open("POST", "submit_project", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("project_title=" + project_title_value
    		+ "&organization_name=" + organization_name_value
    		+ "&start_time=" + start_time_value
    		+ "&end_time=" + end_time_value
    		+ "&details=" + details_value
    		+ "&csrfmiddlewaretoken=" + getCSRFToken());

}

function submitSkill(){
	console.log("Entering submitSkill");
	var text_value = document.getElementById("id_text").value;

	// Construct new request
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState != 4) return;
        if (req.status != 200) return;
        var response = JSON.parse(req.responseText);
        if (response.error == "") {
            window.location.reload();
        } else {
            displayError(response.error, "skills");
        }
    }

    req.open("POST", "submit_skill", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("text=" + text_value
    		+ "&csrfmiddlewaretoken=" + getCSRFToken());
}

function getCSRFToken() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        c = cookies[i].trim();
        if (c.startsWith("csrftoken=")) {
            return c.substring("csrftoken=".length, c.length);
        }
    }
    return "unknown";
}

function displayError(message, type) {
    var errorElement = document.getElementById(type + "_error");
    errorElement.innerHTML = message;
}

