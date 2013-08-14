AboutusRouter = Backbone.Router.extend({
    routes:{
    'zero':'ZeroRoute',
    'dna':'DnaRoute',
    'idea':'IdeaRoute',
    'letskrunk':'LetsKrunkRoute'

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
});

new AboutusRouter();
Backbone.history.start();
