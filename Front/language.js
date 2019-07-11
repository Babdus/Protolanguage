$(window).on('load', function() {
  d3.json("../Data/words_and_languages/swadesh_list.json", function(error, words) {
    $("#table").append('<tr id="thead"><th> </th></tr>');
    for(var word in words) {
      $("#table").append('<tr id="'+words[word]+'"><td>'+words[word]+'</td></tr>');
    }
    let url = new URL(window.location.href);
    let langs = url.searchParams.get("langs").split(',');
    let dir = url.searchParams.get("dir");

    langs.forEach(function (lang, index) {
      let path = "../Data/protolanguages/"+lang+".json";
      if(dir){
        path = "../Data/trees/"+dir+"/protolanguages/"+lang+".json";
      }
      d3.json(path, function(error, data) {
        $("#thead").append('<th>'+lang+'</th>');
        for(var word in data) {
          $("#"+word).append('<td>'+data[word]+'</td>');
        }
      });
    });
  });
});
