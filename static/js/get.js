console.log("get.js running")


var submit = d3.select("#submit");
var user_input = d3.select(".form-control");

submit.on("click", runFind);
user_input.on("submit", runFind);

function runFind() {
    
    d3.event.preventDefault();

    // Grab user input
    var input_article = d3.select("#userarticle");
    var user_article = input_article.property("value");
    console.log(user_article);

    

    // var newArticle = d3.select("")
}