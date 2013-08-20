//ZeroView 
AboutView=Backbone.View.extend({
        el:$('#about_container'),
        initialize:function(){
            console.log("AboutView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#about_template").html(),{});
            this.$el.html(zero);
        },
});

ZeroView=Backbone.View.extend({
        el:$('#about_container'),
        initialize:function(){
            console.log("zeroView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#zero_template").html(),{});
            this.$el.html(zero);
        },
});

//DnaView
DnaView=Backbone.View.extend({
        el:$('#about_container'),
        initialize:function(){
            console.log("DnaView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#dna_template").html(),{});
            this.$el.html(zero);
        },

});

//IdeaView
IdeaView=Backbone.View.extend({
        el:$('#about_container'),
        initialize:function(){
            console.log("IdeaView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#idea_template").html(),{});
            this.$el.html(zero);

        },

});

//LetskrunkView
LetskrunkView=Backbone.View.extend({
        el:$('#about_container'),
        initialize:function(){
            console.log("LetskrunksystemsView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#letskrunk_template").html(),{});
            this.$el.html(zero);
        },
        });
// Testing 
var CRTView=Backbone.View.extend({
    //el:
    el:$('#service_container'),
    initialize:function(){
            console.log("CRTView called");
            this.render();
        },
    render:function(){
           var zero =_.template($("#CRTtemplate").html(),{});
          this.$el.html(zero);
    },
    events:{
    'click button.btn-primary':'CRTAdd',
    },
    CRTAdd:function(event){
            console.log("Workinf");
            company_name=$('#id_company_name').val();
            employee_name=$('#id_employee_name').val();
            personal_email=$('#id_personal_email').val();
            offical_email=$('#id_offical_email').val();
            mobile=$('#id_mobile').val();
            phone=$('#id_phone').val();
            message=$('#id_message').val();
    console.log(message);    
    var CRTmodel=new CRTModel({
               company_name:company_name,
                employee_name:employee_name,
                personal_email:personal_email,
                offical_email:offical_email,
                mobile:mobile,
                phone:phone,
                message:message,
          })
        data='{"company_name":"Krunk Systems","employee_name":"Depak Malik","personal_email":"dmalikcs@gmail.com","offical_email":"krunksystems@gmail.com","mobile":"79975","phone":"9898989"}'
        console.log("console");
        CRTmodel.save();
        return false;
        },
});

TrainingView=Backbone.View.extend({
        el:$('#service_container'),
        initialize:function(){
            console.log("TraiingView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#service_training_template").html(),{});
            this.$el.html(zero);
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
ErpView=Backbone.View.extend({
        el:$('#service_container'),
        initialize:function(){
            console.log("ERPView called");
            this.render();
        },
        render:function(){
            var zero =_.template($("#service_erp_template").html(),{});
            this.$el.html(zero);
        },
});
