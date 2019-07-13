String.prototype.trunc = String.prototype.trunc ||
  function(n){
    return (this.length > n) ? this.substr(0, n-1) + '&hellip;' : this;
  };

lang_codes = {
  "aa": "Afar",
  "ab": "Abkhazian",
  "af": "Afrikaans",
  "ak": "Akan",
  "sq": "Albanian",
  "am": "Amharic",
  "ar": "Arabic",
  "an": "Aragonese",
  "hy": "Armenian",
  "as": "Assamese",
  "av": "Avaric",
  "ae": "Avestan",
  "ay": "Aymara",
  "az": "Azerbaijani",
  "ba": "Bashkir",
  "bm": "Bambara",
  "eu": "Basque",
  "be": "Belarusian",
  "bn": "Bengali",
  "bh": "Bihari languages",
  "bi": "Bislama",
  "bs": "Bosnian",
  "br": "Breton",
  "bg": "Bulgarian",
  "my": "Burmese",
  "ca": "Catalan",
  "ch": "Chamorro",
  "ce": "Chechen",
  "zh": "Chinese",
  "cu": "Church Slavic",
  "cv": "Chuvash",
  "kw": "Cornish",
  "co": "Corsican",
  "cr": "Cree",
  "cs": "Czech",
  "da": "Danish",
  "dv": "Divehi",
  "nl": "Dutch",
  "dz": "Dzongkha",
  "en": "English",
  "eo": "Esperanto",
  "et": "Estonian",
  "ee": "Ewe",
  "fo": "Faroese",
  "fj": "Fijian",
  "fi": "Finnish",
  "fr": "French",
  "fy": "Western Frisian",
  "ff": "Fulah",
  "ka": "Georgian",
  "de": "German",
  "gd": "Gaelic",
  "ga": "Irish",
  "gl": "Galician",
  "gv": "Manx",
  "el": "Greek",
  "gn": "Guarani",
  "gu": "Gujarati",
  "ht": "Haitian",
  "ha": "Hausa",
  "he": "Hebrew",
  "hz": "Herero",
  "hi": "Hindi",
  "ho": "Hiri Motu",
  "hr": "Croatian",
  "hu": "Hungarian",
  "ig": "Igbo",
  "is": "Icelandic",
  "io": "Ido",
  "ii": "Sichuan Yi",
  "iu": "Inuktitut",
  "ie": "Interlingue",
  "ia": "Interlingua",
  "id": "Indonesian",
  "ik": "Inupiaq",
  "it": "Italian",
  "jv": "Javanese",
  "ja": "Japanese",
  "kl": "Kalaallisut",
  "kn": "Kannada",
  "ks": "Kashmiri",
  "kr": "Kanuri",
  "kk": "Kazakh",
  "km": "Central Khmer",
  "ki": "Kikuyu",
  "rw": "Kinyarwanda",
  "ky": "Kirghiz",
  "kv": "Komi",
  "kg": "Kongo",
  "ko": "Korean",
  "kj": "Kuanyama",
  "ku": "Kurdish",
  "lo": "Lao",
  "la": "Latin",
  "lv": "Latvian",
  "li": "Limburgan",
  "ln": "Lingala",
  "lt": "Lithuanian",
  "lb": "Luxembourgish",
  "lu": "Luba-Katanga",
  "lg": "Ganda",
  "mk": "Macedonian",
  "mh": "Marshallese",
  "ml": "Malayalam",
  "mi": "Maori",
  "mr": "Marathi",
  "ms": "Malay",
  "mg": "Malagasy",
  "mt": "Maltese",
  "mn": "Mongolian",
  "na": "Nauru",
  "nv": "Navajo",
  "nr": "Ndebele South",
  "nd": "Ndebele North",
  "ng": "Ndonga",
  "ne": "Nepali",
  "nn": "Norwegian Nynorsk",
  "nb": "Bokmål Norwegian",
  "no": "Norwegian",
  "ny": "Chichewa",
  "oc": "Occitan",
  "oj": "Ojibwa",
  "or": "Oriya",
  "om": "Oromo",
  "os": "Ossetian",
  "pa": "Panjabi",
  "fa": "Persian",
  "pi": "Pali",
  "pl": "Polish",
  "pt": "Portuguese",
  "ps": "Pushto",
  "qu": "Quechua",
  "rm": "Romansh",
  "ro": "Romanian",
  "rn": "Rundi",
  "ru": "Russian",
  "sg": "Sango",
  "sa": "Sanskrit",
  "si": "Sinhala",
  "sk": "Slovak",
  "sl": "Slovenian",
  "se": "Northern Sami",
  "sm": "Samoan",
  "sn": "Shona",
  "sd": "Sindhi",
  "so": "Somali",
  "st": "Sotho Southern",
  "es": "Spanish",
  "sc": "Sardinian",
  "sr": "Serbian",
  "ss": "Swati",
  "su": "Sundanese",
  "sw": "Swahili",
  "sv": "Swedish",
  "ty": "Tahitian",
  "ta": "Tamil",
  "tt": "Tatar",
  "te": "Telugu",
  "tg": "Tajik",
  "tl": "Tagalog",
  "th": "Thai",
  "bo": "Tibetan",
  "ti": "Tigrinya",
  "to": "Tonga",
  "tn": "Tswana",
  "ts": "Tsonga",
  "tk": "Turkmen",
  "tr": "Turkish",
  "tw": "Twi",
  "ug": "Uighur",
  "uk": "Ukrainian",
  "ur": "Urdu",
  "uz": "Uzbek",
  "ve": "Venda",
  "vi": "Vietnamese",
  "vo": "Volapük",
  "cy": "Welsh",
  "wa": "Walloon",
  "wo": "Wolof",
  "xh": "Xhosa",
  "yi": "Yiddish",
  "yo": "Yoruba",
  "za": "Zhuang",
  "zu": "Zulu"
}

$(window).on('load', function() {
  d3.json("../Data/words_and_languages/swadesh_list.json", function(error, words) {
    $("#table").append('<tr id="thead"><th>English</th><th></th></tr>');
    for(var word in words) {
      $("#table").append('<tr id="'+words[word]+'"><td>'+words[word]+'</td><td></td></tr>');
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
        lang_name = lang
        $("#thead").append('<th>'+lang.trunc(20)+'</th><th></th>');
        for(var word in data) {
          $("#"+word).append('<td>['+data[word]+']</td><td id="arrow">&rarr;</td>');
        }
      });
      if(lang.length > 2 && lang.length % 2 == 0){
        $("h1").append("Dictionary of reconstructed protolanguage " + lang);
        var paragraph = "This language is an ancestor of modern languages ";
        var langs1 = lang.match(/.{2}/g);
        console.log(langs1);
        langs1.forEach(function (lang, index) {
          if(index == langs1.length - 2){
            paragraph += lang_codes[lang] + " and ";
          } else if (index == langs1.length - 1) {
            paragraph += lang_codes[lang] + ". ";
          } else {
            paragraph += lang_codes[lang] + ", ";
          }
          let path = "../Data/protolanguages/"+lang+".json";
          if(dir){
            path = "../Data/trees/"+dir+"/protolanguages/"+lang+".json";
          }
          d3.json(path, function(error, data) {
            $("#thead").append('<th>'+lang_codes[lang]+'</th>');
            for(var word in data) {
              $("#"+word).append('<td>['+data[word]+']</td>');
            }
          });
        });
        var age = 2000 - langs1.length*175;
        paragraph += (age < 0 ? Math.abs(age) + "BC " : age + "AD ") + "is the approximate date (without historical callibration) when this language was split into different languages."
        $("p").append(paragraph);
      }
      else {
        $("h1").append("Dictionary of modern language " + lang_codes[lang]);
      }
    });
  });
});
