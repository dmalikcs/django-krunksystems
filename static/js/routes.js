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


ServicesRouter = Backbone.Router.extend({
     routes:{
    'service_training':'TrainingRoute',
    'service_consulting':'ConsultingRoute',
    'service_development':'DevelopementRoute',
    'service_erp':'ErpRoute',
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

});

var aboutview=new AboutusRouter();
var servicesview=new ServicesRouter();
Backbone.history.start();
aboutview.navigate('aboutus', {trigger: true});
servicesview.navigate('service_erp',{trigger: true});

