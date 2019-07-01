$(window).on('load', function() {
  let url = new URL(window.location.href);
  let langs = url.searchParams.get("langs").split(',');
  console.log(langs);
  let jsons = {};

  langs.forEach(function (item, index) {
    d3.json("../Data/protolanguages/"+item+".json", function(error, data) {
      jsons[item] = data;
    });
    console.log(item, index);
  });

  d3.json("../Data/protolanguages/test.json", function(error, data) {
    jsons['test1'] = data;
  });

  d3.json("../Data/protolanguages/test2.json", function(error, data) {
    jsons['test2'] = data;
  });

  console.log(jsons);

  // $("#table").append('<tr><th> </th><th>test</th><th>test2</th></tr>');
  
  console.log(jsons['test']);
  for(var word in jsons['test']) {

    var row = "<tr><th>"+word+"</th>";
    for(var lang in keys) {
      row += "<th>"+jsons[lang][word]+"</th>";
    }
    row += "</tr>";
    console.log(row);
    $("#table").append(row);
  }
});
