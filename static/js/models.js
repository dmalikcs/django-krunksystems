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



var CourseModel=Backbone.Model.extend({
    url:'/api/v1/courses/?format=json'
});

var CourseCollection = Backbone.Collection.extend({
        url:'/api/v1/courses/?format=json',
});

var ERPModuleCollection=Backbone.Collection.extend({
    url:'/api/v1/modules/?format=json',
});
