AboutusRouter = Backbone.Router.extend({
    routes:{
    'zero':'ZeroRoute',
    'dna':'DnaRoute',
    'idea':'IdeaRoute',
    'letskrunk':'LetsKrunkRoute',
    'crtform':'CRTRoute',
    'about':'AboutRoute',
    'service_training':'TrainingRoute',
    'service_consulting':'ConsultingRoute',
    'service_development':'DevelopementRoute',
    'service_erp':'ErpRoute',

      },
    ZeroRoute:function(){
        console.log("called from Home");
        new ZeroView();
       },
    DnaRoute:function(){
        console.log("called from DNA");
        new DnaView();
    },
    IdeaRoute:function(){
        console.log("called from idea !");
        new IdeaView();
    },
    LetsKrunkRoute:function(){
        console.log("called from  Let's Krunk Systems ");
        new LetskrunkView();
    },
    CRTRoute:function(){
        console.log("called from: Let's CoutRoute");
        new CRTView();
        console.log("called CRTView");
    },
    AboutRoute:function(){
        console.log("called from: AboutRoute");
        new AboutView();
        console.log("called AboutView");
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
    }
});

aboutrouter=new AboutusRouter();
Backbone.history.start();
//aboutrouter.navigate('about', {trigger: true});
//aboutrouter.navigate('service_training', {trigger: true});
