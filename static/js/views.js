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
        },
        PCAdd:function(event){
            console.log('PCAdd consultancy');
        },
        DCAdd:function(event){
            console.log('DCAdd consultancy');
        },
        OCAdd:function(event){
            console.log('OCAdd consultancy');
        },
        MCAdd:function(event){
            console.log('MCAdd consultancy');
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
            console.log('ERP Inquiry submited')
        },
        DemoAdd:function(event){
            console.log('Demo Called')
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
