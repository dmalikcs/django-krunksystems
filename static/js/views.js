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
        'click a.test':'CourseDisplay',
        'click a.Deepak':'SingleCourseDisplay',
        'click button.btn-primary':'CRTAdd',
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
            console.log("Workinf");
            company_name=$('#id_company_name').val();
            employee_name=$('#id_employee_name').val();
            personal_email=$('#id_personal_email').val();
            offical_email=$('#id_offical_email').val();
            mobile=$('#id_mobile').val();
            phone=$('#id_phone').val();
            message=$('#id_message').val();
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
});

ConsultingView=Backbone.View.extend({
        el:$('#service_container'),
        initialize:function(){
            console.log("ConsultView called");
            this.render();
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
        render:function(){
            var zero =_.template($("#service_development_template").html(),{});
            this.$el.html(zero);
        },
});

var ErpView=Backbone.View.extend({
        el:$('#service_container'),
        events:{
            'click a.erp_modules':'ERPModulesDisplay',
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

