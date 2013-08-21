var CRTModel=Backbone.Model.extend({
sync: function (method, model, options){
    if (method === 'create'){
         return $.ajax({
                datatype:'json',
                type:'POST',
                contentType: 'application/json',
                url:'/api/v1/cor_training/?username=dmalik5\&api_key=4791c10acb8d425fbab86dc05adc49087d3050c2',
                data: JSON.stringify({
                        company_name:(this.get('company_name')|| ''),
                        employee_name:(this.get('employee_name')||''),
                        personal_email:(this.get('personal_email')||''),
                        offical_email:(this.get('offical_email')||''),
                        mobile:(this.get('mobile')||''),
                        phone:(this.get('phone')||''),
                        message:(this.get('message')||''),
                }),
                success:function(data){
                  console.log("Account saved");
                  $('#form_modal').html("<button class = \"btn btn-danger\" data-dismiss=\"modal\" aria-hidden=\"true\"> Close </button>");
                },
                error:function(jqXHR, textStatus, errorThrown){
                    var errors = JSON.parse(jqXHR.responseText) 
                    for (field in errors.cor_training) {
                        var error = errors['cor_training'][field];
                        $('#id_err_' + field).html(" " + error + " ");
                    }   
                },
        });
    }
},
});

var CourseModel=Backbone.Model.extend({
    url:'/api/v1/courses/?format=json'
});

var CourseCollection = Backbone.Collection.extend({
        url:'/api/v1/courses/?format=json',
});
