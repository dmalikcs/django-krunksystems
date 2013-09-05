//ZeroView 
AboutView=Backbone.View.extend({
        el:$('#aboutus'),
        events:{
        'click a#about_id':'AboutusView',
        'click a#zero_id':'ZeroView',
        'click a#idea_id':'IdeaView',
        'click a#letskrunk_id':'LetsKrunkView',
        'click a#dna_id':'DnaView',
        },
        AboutusView:function(event){
            var zero =_.template($('#about_template').html(),{});
            $('#about_container').html(zero);
        },
        ZeroView:function(event){
            var zero =_.template($('#zero_template').html(),{});
            $('#about_container').html(zero);
        },
        IdeaView:function(event){
            var idea =_.template($('#idea_template').html(),{});
            $('#about_container').html(idea);
        },
        LetsKrunkView:function(event){
            var krunk =_.template($('#letskrunk_template').html(),{});
            $('#about_container').html(krunk);
        },
        DnaView:function(event){
            var dna =_.template($('#dna_template').html(),{});
            $('#about_container').html(dna);
        },
        initialize:function(){
            console.log("AboutView called");
            this.render();
            this.AboutusView();
        },
        render:function(){
            var zero =_.template($("#aboutus_template").html(),{});
            this.$el.html(zero);
        },
});

ContactusView=Backbone.View.extend({
        el:$('#contactus_page'),
        events:{
        'click button#submit_request':'ContactSubmitView',
        'click button#clear_form':'FormClear',
        },
        initialize:function(){
            console.log("ContactView called");
            this.render();
        },
        render:function(){
            var contactus =_.template($("#contactus_template").html(),{});
            this.$el.html(contactus);
        },
        FormClear:function(event){
            $('#contactus_form #id_name').val('');
            $('#contactus_form #id_err_name').html('');
            $('#contactus_form #id_mobile').val('');
            $('#contactus_form #id_err_mobile').html('');
            $('#contactus_form #id_Email').val('');
            $('#contactus_form #id_err_Email').html('');
            $('#contactus_form #id_Message').val('');
            $('#contactus_form #id_err_Message').html('');
        },
        ContactSubmitView:function(event){
            name=$('#contactus_form #id_name').val();
            mobile=$('#contactus_form #id_mobile').val();
            Email=$('#contactus_form #id_Email').val();
            Message=$('#contactus_form #id_Message').val();
            var Contactusmodel=new ContactusModel({
                name:name,
                mobile:mobile,
                Email:Email,
                Message:Message,
            });
            Contactusmodel.save();
            return false;
        },
});

TrainingView=Backbone.View.extend({
        el:$('#service_container'),
        initialize:function(){
            this.render();
        },
        render:function(){
            var zero =_.template($("#service_training_template").html(),{});
            this.$el.html(zero);
        },
        events:{
        'click a.coursedisplay':'CourseDisplay',
        'click #crform_submit':'CRTAdd',
        'click #itform_submit':'ITAdd',
        'click #atform_submit':'ATAdd',
        },
        CourseDisplay:function(events){
            var cc=new CourseCollection();
            cc.fetch({
                    success:function(collection,response){
                    var display=_.template($('#coursedisplay_template').html(),{people:response.objects});
                    $('#coursetraining').html(display);
                    },
                    });
        } ,
    CRTAdd:function(event){
            company_name=$('#crform #id_company_name').val();
            employee_name=$('#crform #id_employee_name').val();
            personal_email=$('#crform #id_personal_email').val();
            offical_email=$('#crform #id_offical_email').val();
            mobile=$('#crform #id_mobile').val();
            phone=$('#crform #id_phone').val();
            message=$('#crform #id_message').val();
    var CRTmodel=new CRTModel({
               company_name:company_name,
                employee_name:employee_name,
                personal_email:personal_email,
                offical_email:offical_email,
                mobile:mobile,
                phone:phone,
                message:message,
          });
        CRTmodel.save();
        return false;
        },
    ITAdd: function(){ //ITadd training 
        student_name=$('#itform #id_student_name').val();
        email=$('#itform #id_email').val();
        mobile=$('#itform #id_mobile').val();
        collage=$('#itform #id_collage').val();
        degree=$('#itform #id_degree').val();
        intership_period=$('#itform #id_intership_period').val();
        platform=$('#itform #id_platform').val();
        message=$('#itform #id_message').val();
    var ITmodel=new ITModel({
        student_name:student_name,
        email:email,
        mobile:mobile,
        collage:collage,
        degree:degree,
        intership_period:intership_period,
        platform:platform,
        message:message,
      });
        ITmodel.save();
        return false;
            
    },
    ATAdd:function(){ //ATAdd Training
        console.log('AT add called');
        /*AcademyTraining */
        student_name=$('#atform #id_student_name').val();
        email=$('#atform #id_email').val();
        degree=$('#atform #id_degree').val();
        branch=$('#atform #id_branch').val();
        mobile=$('#atform #id_mobile').val();
        collage_name=$('#atform #id_collage_name').val();
        collage_website=$('#atform #id_collage_website').val();
        message=$('#atform #id_message').val();
        console.log(message);
    var ATmodel=new ATModel({
        student_name:student_name,
        email:email,
        degree:degree,
        branch:branch,
        mobile:mobile,
        collage_name:collage_name,
        collage_website:collage_website,
        message:message
        });
        ATmodel.save();
        return false;
    },
});

ConsultingView=Backbone.View.extend({
        el:$('#service_container'),
        initialize:function(){
            console.log("ConsultView called");
            this.render();
        },
        events:{
        'click #pcform_submit':'PCAdd',
        'click #dcform_submit':'DCAdd',
        'click #ocform_submit':'OCAdd',
        'click #mcform_submit':'MCAdd',
        'click a.python':'PythonView',
        'click button#show':'ShowView',
        'click button#close':'PythonView',
        },
        PCAdd:function(event){
            console.log('PCAdd consultancy');
            name=$('#pcform #id_name').val();
            email=$('#pcform #id_email').val();
            category=$('#pcform #id_category').val();
            message=$('#pcform #id_message').val();
            var PCmodel=new PCModel({
            name:name,
            email:email,
            category:category,
            message:message,
            });
            PCmodel.save();
            return false;
        },
        DCAdd:function(event){
            console.log('DCAdd consultancy');
            name=$('#dcform #id_name').val();
            email=$('#dcform #id_email').val();
            category=$('#dcform #id_category').val();
            message=$('#dcform #id_message').val();
            var DCmodel=new DCModel({
            name:name,
            email:email,
            category:category,
            message:message,
            });
            DCmodel.save();
            return false;
        },
        OCAdd:function(event){
            console.log('OCAdd consultancy');
            name=$('#ocform #id_name').val();
            email=$('#ocform #id_email').val();
            category=$('#ocform #id_category').val();
            message=$('#ocform #id_message').val();
            var OCmodel=new OCModel({
            name:name,
            email:email,
            category:category,
            message:message,
            });
            OCmodel.save();
            return false;
        },
        MCAdd:function(event){
            console.log('MCAdd consultancy');
            name=$('#mcform #id_name').val();
            email=$('#mcform #id_email').val();
            category=$('#mcform #id_category').val();
            message=$('#mcform #id_message').val();
            var MCmodel=new MCModel({
            name:name,
            email:email,
            category:category,
            message:message,
            });
            MCmodel.save();
            return false;
        },
        PythonView:function(event){
            var python =_.template($('#python_template').html(),{});
            $('#PythonConsultancy').html(python);
        },
        ShowView:function(event){
            var python =_.template($('#show_template').html(),{});
            $('#PythonConsultancy').html(python);
        },
        render:function(){
            var zero =_.template($("#service_consulting_template").html(),{});
            this.$el.html(zero);
        },
});
DevelopementView=Backbone.View.extend({
        el:$('#service_container'),
        initialize:function(){
            console.log("DevelopmentView called");
            this.render();
        },
        events:{
        'click #adform_submit':'ADAdd',
        'click #wdform_submit':'WDAdd',
        },
        ADAdd:function(event){
            console.log('ADAdd Click')
        },
        WDAdd:function(event){
            console.log('WDAdd Click')
            name=$('#wdform #id_name').val();
            email=$('#wdform #id_email').val();
            country=$('#wdform #id_country').val();
            mobile=$('#wdform #id_mobile').val();
            project_budget=$('#wdform #id_project_budget').val();
            project_start_date=$('#wdform #id_project_start_date').val();
            project_file=$('#wdform #id_project_file').val();
            project_message=$('#wdform #id_project_message').val();
            console.log(project_message);
        var WDmodel=new WDModel({
            name:name,
            email:email,
            country:country,
            mobile:mobile,
            project_budget:project_budget,
            project_start_date:project_start_date,
            project_file:project_file,
            project_message:project_message,
            });
            WDmodel.save();
            return false;
        },
        render:function(){
            var zero =_.template($("#service_development_template").html(),{});
            this.$el.html(zero);
        },
});

var ErpView=Backbone.View.extend({
        el:$('#service_container'),
        events:{
            'click #erpinquiryform_submit':'ErpInquiryAdd',
            'click #demoform_submit':'DemoAdd',
            'click a.erp_modules':'ERPModulesDisplay',
        },
        ErpInquiryAdd:function(event){
            name=$('#erpinquiryform #id_name').val();
            job_title=$('#erpinquiryform #id_job_title').val();
            phone=$('#erpinquiryform #id_phone').val();
            email=$('#erpinquiryform #id_email').val();
            company_name=$('#erpinquiryform #id_company_name').val();
            company_website=$('#erpinquiryform #id_company_website').val();
            product=$('#erpinquiryform #id_product').val();
            message=$('#erpinquiryform #id_message').val();
        var ErpInquirymodel= new ErpInquiryModel({
            name:name,
            job_title:job_title,
            phone:phone,
            email:email,
            company_name:company_name,
            company_website:company_website,
            product:product,
            message:message,
        });
        ErpInquirymodel.save();
        return false;
        },
        DemoAdd:function(event){
            console.log('Demo Called')
            name=$('#demoform #id_name').val();
            mobile=$('#demoform #id_mobile').val();
            email=$('#demoform #id_email').val();
            modules=$('#demoform #id_modules').val();
            Type_of_demo=$('#demoform #id_Type_of_demo').val();
            date=$('#demoform #id_date').val();
            time=$('#demoform #id_time').val();
            var Demomodel=new DemoModel({
                name:name,
                mobile:mobile,
                email:email,
                modules:modules,
                Type_of_demo:Type_of_demo,
                date:date,
                time:time,
            });
            Demomodel.save();
            return false;
        },
        initialize:function(){
            console.log("ERPView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#service_erp_template").html(),{});
            this.$el.html(zero);
        },
        ERPModulesDisplay: function(event){
            console.log("ERPModules Display Called");
            var modules=new ERPModuleCollection()
            modules.fetch({
                        success:function(collection,response){
                        var data=_.template($('#modules_template').html(),{modules:response.objects,meta:response.meta});
                        $('#modules').html(data);
                        },
            });
        },
});
/*
var CourseView=Backbone.View.extend({
    el:$('#temp'),
    initialize:function(){
        console.log("ListCoursePage called");
        this.render()
    },
    render:function(response){
        console.log("render function called");
        var temp=_.template($('#crs'),{});
        this.$el.html(temp);
    },
});
*/

var ServiceView=Backbone.View.extend({
    el:$('#service_container'),
    initialize:function(){
        console.log("Deepak Malik");
        this.render();
    },
    render:function(){
        var service =_.template($("#service_template").html(),{});
        this.$el.html(service);
    },
});//serviceview closed
