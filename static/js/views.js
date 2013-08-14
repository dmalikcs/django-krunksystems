//ZeroView 
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

