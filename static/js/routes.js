AboutusRouter = Backbone.Router.extend({
 routes:{
    '':'AboutRoute',
    'aboutus':'AboutRoute',
    },
    AboutRoute:function(){
        console.log("called from: AboutRoute");
        new AboutView();
        console.log("called AboutView");
    },
});
ContactusRouter = Backbone.Router.extend({
    routes:{
    '':'ContactusRoute',
    },
    ContactusRoute:function(){
        console.log('called');
        new ContactusView();
        new ServiceView();
        new AboutView();
    },
});



ServicesRouter = Backbone.Router.extend({
     routes:{
    '':'ServicesRoute',
    'services':'ServicesRoute',
    'training':'TrainingRoute',
    'consulting':'ConsultingRoute',
    'development':'DevelopementRoute',
    'erp':'ErpRoute',
    'trainingcourse':'trainingcourseRoute',
    },
    TrainingRoute:function(){
        if (typeof this.training != 'undefined'){
            console.log("thi.erp called");
            this.training.close();
        }
        this.training=new TrainingView();
        $('#MainServiceContainer').html(this.training.el)
    },
    ConsultingRoute:function(){
        if (typeof this.consultancy != 'undefined'){
            console.log("thi.erp called");
            this.consultancy.close();
        }
        this.consultancy =new ConsultingView();
        $('#MainServiceContainer').html(this.consultancy.el)
    },
    DevelopementRoute:function(){
        if (typeof this.development != 'undefined'){
            console.log("thi.erp called");
            this.development.close();
        }
        this.development=new DevelopementView();
        $('#MainServiceContainer').html(this.development.el)
    },
    ErpRoute:function(){
        console.log("called from: ErpRoute");
        if (typeof this.erp != 'undefined'){
            console.log("thi.erp called");
            this.erp.close();
        }
        this.erp=new ErpView();
        $('#MainServiceContainer').html(this.erp.el)
    },
    trainingcourseRoute:function(){
        if (typeof this.course != 'undefined'){
            console.log("thi.erp called");
            this.course.close();
        }
        this.course=new ServiceView();
    },
    ServicesRoute:function(){
        if (typeof this.service != 'undefined'){
            console.log("thi.erp called");
            this.service.close();
        }
        this.service=new ServiceView();
        $('#MainServiceContainer').html(this.service.el)
    },
});

var aboutview=new AboutusRouter();
var servicesview=new ServicesRouter();
var contactus=new ContactusRouter();
Backbone.history.start();
