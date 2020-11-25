console.log("get.js running")

var submit = d3.select("#submit");
var user_input = d3.select(".form-control");

submit.on("click", runFind);
user_input.on("submit", runFind);
// buildGuage();

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
        .append("h6")
        .classed("centered", true)
        .html("so unreal it's unreal");
    }


}

// function buildGuage(info) { 
        

//         var wfreq = 1;
//         console.log(`WASH FREQUENCY OF : ${wfreq}`); 

//         // Code mostly copied from https://plotly.com/javascript/indicator/

//         var data = [
//             {
//               domain: { x: [0, 1], y: [0, 1] },
//               value: wfreq,
//               title: { text: "Accuracy" },
//               type: "indicator",
//               mode: "gauge+number+delta",
//             //   delta: { reference: 380 },
//               gauge: {
//                 axis: { range: [null, 9] },
//                 bar: { color: "#9e5226"},
//                 steps: [
//                   { range: [0, 1], color: "#FFF2E5"},
//                   { range: [1, 2], color: "#FFE6CC" },
//                   { range: [2, 3], color: "#FFDAB2" },
//                   { range: [3, 4], color: "#FFCD99" },
//                   { range: [4, 5], color: "#FFC17F" },
//                   { range: [5, 6], color: "#FFB566" },
//                   { range: [6, 7], color: "#FFA84C" },
//                   { range: [7, 8], color: "#FF9C33" },
//                   { range: [8, 9], color: "#FF9019" }
//                 ],
//                 threshold: {
//                   line: { color: "black", width: 4 },
//                   thickness: 0.75,
//                   value: 2
//                 }
//               }
//             }
//           ];
          
//           var layout = { width: 400, height: 200, margin: { t: 20, b: 0 } };
//           Plotly.newPlot('gauge', data, layout);
// }