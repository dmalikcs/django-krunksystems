AboutusRouter = Backbone.Router.extend({
 routes:{
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
    },
});



ServicesRouter = Backbone.Router.extend({
     routes:{
    'services':'ServicesRoute',
    'training':'TrainingRoute',
    'consulting':'ConsultingRoute',
    'development':'DevelopementRoute',
    'erp':'ErpRoute',
    'trainingcourse':'trainingcourseRoute',
    },
    TrainingRoute:function(){
        console.log("called from: TrainingRoute");
        new TrainingView();
        console.log("called TrainingView");
    },
    ConsultingRoute:function(){
        console.log("called from: ConsultingRoute");
        new ConsultingView();
        console.log("called AboutView");
    },
    DevelopementRoute:function(){
        console.log("called from: DevelopementRoute");
        new DevelopementView();
        console.log("called AboutView");
    },
    ErpRoute:function(){
        console.log("called from: ErpRoute");
        new ErpView();
        console.log("called ErpView");
    },
    trainingcourseRoute:function(){
        console.log("Called trainingcourseRoute");
        new CourseView();
        console.log("called trainingcourseRoute:success");
    },
    ServicesRoute:function(){
        console.log('Services Page called');
        new ServiceView();
    }
});

var aboutview=new AboutusRouter();
var servicesview=new ServicesRouter();
var contactus=new ContactusRouter();
Backbone.history.start();
aboutview.navigate('aboutus', {trigger: true});
contactus.navigate('',{trigger: true});
