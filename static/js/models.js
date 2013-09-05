var CRTModel=Backbone.Model.extend({
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/cor_training/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                        company_name:(this.get('company_name')|| ''),
                        employee_name:(this.get('employee_name')||''),
                        personal_email:(this.get('personal_email')||''),
                        offical_email:(this.get('offical_email')||''),
                        mobile:(this.get('mobile')||''),
                        phone:(this.get('phone')||''),
                        message:(this.get('message')||''),
                }
                ),
                beforeSend: function(){
                    $('#crform #id_err_company_name').html('');
                    $('#crform #id_err_employee_name').html('');
                    $('#crform #id_err_personal_email').html('');
                    $('#crform #id_err_offical_email').html('');
                    $('#crform #id_err_mobile').html('');
                    $('#crform #id_err_phone').html('');
                    $('#crform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#crform').html(),{});
                    $('#crform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:'Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#crform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    for (field in errors.cor_training) {
                        var error = errors['cor_training'][field];
                        $('#crform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//CRTModel Closed


/* Industrial Training Model*/
var ITModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/id_training/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                        student_name:(this.get('student_name')|| ''),
                        email:(this.get('email')|| ''),
                        mobile:(this.get('mobile')|| ''),
                        collage:(this.get('collage')|| ''),
                        degree:(this.get('degree')|| ''),
                        intership_period:(this.get('intership_period')|| ''),
                        platform:(this.get('platform')|| ''),
                        message:(this.get('message')|| ''),
                }
                ),
                beforeSend: function(){
                        $('#itform #id_err_student_name').html('');
                        $('#itform #id_err_email').html('');
                        $('#itform #id_err_mobile').html('');
                        $('#itform #id_err_collage').html('');
                        $('#itform #id_err_degree').html('');
                        $('#itform #id_err_intership_period').html('');
                        $('#itform #id_err_platform').html('');
                        $('#itform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#itform').html(),{});
                    $('#itform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#itform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.id_training) {
                        var error = errors['id_training'][field];
                        $('#itform #id_err_' + field).html(" " + error + " ");
                        //$('#itform #id_err_' + field).html(" " + field + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//ITModel Closed

var ATModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/ac_training/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    student_name:(this.get('student_name')|| ''),
                    email:(this.get('email')|| ''),
                    degree:(this.get('degree')|| ''),
                    branch:(this.get('branch')|| ''),
                    mobile:(this.get('mobile')|| ''),
                    collage_name:(this.get('collage_name')|| ''),
                    collage_website:(this.get('collage_website')|| ''),
                    message:(this.get('message')|| ''),
                }),
                beforeSend: function(){
                    $('#atform #id_err_student_name').html('');
                    $('#atform #id_err_email').html('');
                    $('#atform #id_err_degree').html('');
                    $('#atform #id_err_branch').html('');
                    $('#atform #id_err_mobile').html('');
                    $('#atform #id_err_collage_name').html('');
                    $('#atform #id_err_collage_website').html('');
                    $('#atform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#atform').html(),{});
                    $('#atform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#atform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.ac_training) {
                        var error = errors['ac_training'][field];
                        console.log('#id_err_'+field);
                        $('#atform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//ATModel Closed

var PCModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/python/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    email:(this.get('email')|| ''),
                    category:(this.get('category')|| ''),
                    message:(this.get('message')|| ''),
                }),
                beforeSend: function(){
                    $('#pcform #id_err_name').html('');
                    $('#pcform #id_err_email').html('');
                    $('#pcform #id_err_category').html('');
                    $('#pcform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#pcform').html(),{});
                    $('#pcform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    $('#pcform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.python) {
                        var error = errors['python'][field];
                        console.log('#id_err_'+field);
                        $('#pcform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//PCModel Closed


var DCModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/django/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    email:(this.get('email')|| ''),
                    category:(this.get('category')|| ''),
                    message:(this.get('message')|| ''),
                }),
                beforeSend: function(){
                    $('#dcform #id_err_name').html('');
                    $('#dcform #id_err_email').html('');
                    $('#dcform #id_err_category').html('');
                    $('#dcform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#dcform').html(),{});
                    $('#dcform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#dcform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.django) {
                        var error = errors['django'][field];
                        console.log('#id_err_'+field);
                        $('#dcform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//DCModel Closed

var OCModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/os/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    email:(this.get('email')|| ''),
                    category:(this.get('category')|| ''),
                    message:(this.get('message')|| ''),
                }),
                beforeSend: function(){
                    $('#ocform #id_err_name').html('');
                    $('#ocform #id_err_email').html('');
                    $('#ocform #id_err_category').html('');
                    $('#ocform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#ocform').html(),{});
                    $('#ocform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:'Your request has been submitted',
                    });
                    console.log(alert);
                    $('#ocform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.os) {
                        var error = errors['os'][field];
                        console.log('#id_err_'+field);
                        $('#ocform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//OCModel Closed

var MCModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/midrange/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    email:(this.get('email')|| ''),
                    category:(this.get('category')|| ''),
                    message:(this.get('message')|| ''),
                }),
                beforeSend: function(){
                    $('#mcform #id_err_name').html('');
                    $('#mcform #id_err_email').html('');
                    $('#mcform #id_err_category').html('');
                    $('#mcform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#mcform').html(),{});
                    $('#mcform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#mcform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.midrange) {
                        var error = errors['midrange'][field];
                        console.log('#id_err_'+field);
                        $('#mcform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//MCModel Closed

var WDModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/development/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                enctype: 'multipart/form-data',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    email:(this.get('email')|| ''),
                    country:(this.get('country')|| ''),
                    mobile:(this.get('mobile')|| ''),
                    project_budget:(this.get('project_budget')|| ''),
                    project_start_date:(this.get('project_start_date')|| ''),
                    project_file:(this.get('project_file')|| ''),
                    project_message:(this.get('project_message')|| ''),
                }),
                beforeSend: function(){
                    $('#wdform #id_err_name').html('');
                    $('#wdform #id_err_email').html('');
                    $('#wdform #id_err_country').html('');
                    $('#wdform #id_err_mobile').html('');
                    $('#wdform #id_err_project_budget').html('');
                    $('#wdform #id_err_project_start_date').html('');
                    $('#wdform #id_err_project_file').html('');
                    $('#wdform #id_err_project_message').html('');
                },
                success:function(data){
                    var a=_.template($('#wdform').html(),{});
                    $('#wdform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#wdform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.development) {
                        var error = errors['development'][field];
                        console.log('#id_err_'+field);
                        $('#wdform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//WDModel Closed

var ErpInquiryModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/inquiry/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                enctype: 'multipart/form-data',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    job_title:(this.get('job_title')|| ''),
                    phone:(this.get('phone')|| ''),
                    email:(this.get('email')|| ''),
                    company_name:(this.get('company_name')|| ''),
                    company_website:(this.get('company_website')|| ''),
                    product:(this.get('product')|| ''),
                    message:(this.get('message')|| ''),
                }),
                beforeSend: function(){
                    $('#erpinquiryform #id_err_name').html('');
                    $('#erpinquiryform #id_err_job_title').html('');
                    $('#erpinquiryform #id_err_phone').html('');
                    $('#erpinquiryform #id_err_email').html('');
                    $('#erpinquiryform #id_err_company_name').html('');
                    $('#erpinquiryform #id_err_company_website').html('');
                    $('#erpinquiryform #id_err_product').html('');
                    $('#erpinquiryform #id_err_message').html('');
                },
                success:function(data){
                    var a=_.template($('#erpinquiryform').html(),{});
                    $('#erpinquiryform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#erpinquiryform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.inquiry) {
                        var error = errors['inquiry'][field];
                        console.log('#id_err_'+field);
                        $('#erpinquiryform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//ErpInquiryModel Closed


var DemoModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/demorequest/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    mobile:(this.get('mobile')|| ''),
                    email:(this.get('email')|| ''),
                    modules:(this.get('modules')|| ''),
                    Type_of_demo:(this.get('Type_of_demo')|| ''),
                    date:(this.get('date')|| ''),
                    time:(this.get('time')|| ''),
                }),
                beforeSend: function(){
                    $('#demoform #id_err_name').html('');
                    $('#demoform #id_err_mobile').html('');
                    $('#demoform #id_err_email').html('');
                    $('#demoform #id_err_modules').html('');
                    $('#demoform #id_err_Type_of_demo').html('');
                    $('#demoform #id_err_date').html('');
                    $('#demoform #id_err_time').html('');
                },
                success:function(data){
                    var a=_.template($('#demoform').html(),{});
                    $('#demoform').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#demoform #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.demorequest) {
                        var error = errors['demorequest'][field];
                        console.log('#id_err_'+field);
                        $('#demoform #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//DemoModel Closed


var ContactusModel=Backbone.Model.extend({     
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/contactus/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                global: true,
                data: JSON.stringify({
                    name:(this.get('name')|| ''),
                    mobile:(this.get('mobile')|| ''),
                    Email:(this.get('Email')|| ''),
                    Message:(this.get('Message')|| ''),
                }),
                beforeSend: function(){
                    $('#contactus_form #id_err_name').html('');
                    $('#contactus_form #id_err_mobile').html('');
                    $('#contactus_form #id_err_Email').html('');
                    $('#contactus_form #id_err_Message').html('');
                },
                success:function(data){
                    var a=_.template($('#contactus_form').html(),{});
                    $('#contactus_form').html(a);
                    var alert = _.template($('#alert-template').html(),{ //loading from templates.html
                    type:'success',
                    bold_message:'Thanks ',
                    general_message:' Yeh,We wone it',
                    });
                    console.log(alert);
                    $('#contactus_form #success-saved').html(alert);
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    console.log(errors);
                    for (field in errors.contactus) {
                        var error = errors['contactus'][field];
                        console.log('#id_err_'+field);
                        $('#contactus_form #id_err_' + field).html(" " + error + " ");
                    }   
                },//error function closed
        });
    }//if loop closed
},//sync function closed
});//ContactusModel Closed


var CourseModel=Backbone.Model.extend({
    url:'/api/v1/courses/?format=json'
});

var CourseCollection = Backbone.Collection.extend({
        url:'/api/v1/courses/?format=json',
});

var ERPModuleCollection=Backbone.Collection.extend({
    url:'/api/v1/modules/?format=json',
});
