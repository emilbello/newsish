console.log("get.js running")


var submit = d3.select("#submit");
var user_input = d3.select(".form-control");

submit.on("click", runFind);
user_input.on("submit", runFind);

function runFind() {
    
    var clearHowReliable = d3.select("#reliability");
    clearHowReliable.html("");

    d3.event.preventDefault();

    // Grab user input
    var input_article = d3.select("#userarticle");
    var user_article = input_article.property("value");
    console.log(user_article);

    if (user_article === '0') {
        
        var howReliable = d3.select("#reliability")
                    .append("h6")
                    .classed("centered", true)
                    .html("RELIABLE");

        var meterChange = d3.select("#meter")
                    .attr('src', '../static/assets/reliable-meter.gif')
    }

    else if (user_article === '1') {
        var howReliable = d3.select("#reliability")
                    .append("h6")
                    .classed("centered", true)
                    .html("UNRELIABLE");

        var meterChange = d3.select("#meter")
                    .attr('src', '../static/assets/unreliable-meter.gif')
    }

    else {
        var howReliable = d3.select("#reliability")
        .append("h1")
        .classed("centered", true)
        .html("NA");
    }

}