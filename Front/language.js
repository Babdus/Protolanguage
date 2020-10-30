String.prototype.trunc = String.prototype.trunc ||
  function(n){
    return (this.length > n) ? this.substr(0, n-1) + '&hellip;' : this;
  };

  function md5cycle(x, k) {
  var a = x[0], b = x[1], c = x[2], d = x[3];

  a = ff(a, b, c, d, k[0], 7, -680876936);
  d = ff(d, a, b, c, k[1], 12, -389564586);
  c = ff(c, d, a, b, k[2], 17,  606105819);
  b = ff(b, c, d, a, k[3], 22, -1044525330);
  a = ff(a, b, c, d, k[4], 7, -176418897);
  d = ff(d, a, b, c, k[5], 12,  1200080426);
  c = ff(c, d, a, b, k[6], 17, -1473231341);
  b = ff(b, c, d, a, k[7], 22, -45705983);
  a = ff(a, b, c, d, k[8], 7,  1770035416);
  d = ff(d, a, b, c, k[9], 12, -1958414417);
  c = ff(c, d, a, b, k[10], 17, -42063);
  b = ff(b, c, d, a, k[11], 22, -1990404162);
  a = ff(a, b, c, d, k[12], 7,  1804603682);
  d = ff(d, a, b, c, k[13], 12, -40341101);
  c = ff(c, d, a, b, k[14], 17, -1502002290);
  b = ff(b, c, d, a, k[15], 22,  1236535329);

  a = gg(a, b, c, d, k[1], 5, -165796510);
  d = gg(d, a, b, c, k[6], 9, -1069501632);
  c = gg(c, d, a, b, k[11], 14,  643717713);
  b = gg(b, c, d, a, k[0], 20, -373897302);
  a = gg(a, b, c, d, k[5], 5, -701558691);
  d = gg(d, a, b, c, k[10], 9,  38016083);
  c = gg(c, d, a, b, k[15], 14, -660478335);
  b = gg(b, c, d, a, k[4], 20, -405537848);
  a = gg(a, b, c, d, k[9], 5,  568446438);
  d = gg(d, a, b, c, k[14], 9, -1019803690);
  c = gg(c, d, a, b, k[3], 14, -187363961);
  b = gg(b, c, d, a, k[8], 20,  1163531501);
  a = gg(a, b, c, d, k[13], 5, -1444681467);
  d = gg(d, a, b, c, k[2], 9, -51403784);
  c = gg(c, d, a, b, k[7], 14,  1735328473);
  b = gg(b, c, d, a, k[12], 20, -1926607734);

  a = hh(a, b, c, d, k[5], 4, -378558);
  d = hh(d, a, b, c, k[8], 11, -2022574463);
  c = hh(c, d, a, b, k[11], 16,  1839030562);
  b = hh(b, c, d, a, k[14], 23, -35309556);
  a = hh(a, b, c, d, k[1], 4, -1530992060);
  d = hh(d, a, b, c, k[4], 11,  1272893353);
  c = hh(c, d, a, b, k[7], 16, -155497632);
  b = hh(b, c, d, a, k[10], 23, -1094730640);
  a = hh(a, b, c, d, k[13], 4,  681279174);
  d = hh(d, a, b, c, k[0], 11, -358537222);
  c = hh(c, d, a, b, k[3], 16, -722521979);
  b = hh(b, c, d, a, k[6], 23,  76029189);
  a = hh(a, b, c, d, k[9], 4, -640364487);
  d = hh(d, a, b, c, k[12], 11, -421815835);
  c = hh(c, d, a, b, k[15], 16,  530742520);
  b = hh(b, c, d, a, k[2], 23, -995338651);

  a = ii(a, b, c, d, k[0], 6, -198630844);
  d = ii(d, a, b, c, k[7], 10,  1126891415);
  c = ii(c, d, a, b, k[14], 15, -1416354905);
  b = ii(b, c, d, a, k[5], 21, -57434055);
  a = ii(a, b, c, d, k[12], 6,  1700485571);
  d = ii(d, a, b, c, k[3], 10, -1894986606);
  c = ii(c, d, a, b, k[10], 15, -1051523);
  b = ii(b, c, d, a, k[1], 21, -2054922799);
  a = ii(a, b, c, d, k[8], 6,  1873313359);
  d = ii(d, a, b, c, k[15], 10, -30611744);
  c = ii(c, d, a, b, k[6], 15, -1560198380);
  b = ii(b, c, d, a, k[13], 21,  1309151649);
  a = ii(a, b, c, d, k[4], 6, -145523070);
  d = ii(d, a, b, c, k[11], 10, -1120210379);
  c = ii(c, d, a, b, k[2], 15,  718787259);
  b = ii(b, c, d, a, k[9], 21, -343485551);

  x[0] = add32(a, x[0]);
  x[1] = add32(b, x[1]);
  x[2] = add32(c, x[2]);
  x[3] = add32(d, x[3]);

  }

  function cmn(q, a, b, x, s, t) {
  a = add32(add32(a, q), add32(x, t));
  return add32((a << s) | (a >>> (32 - s)), b);
  }

  function ff(a, b, c, d, x, s, t) {
  return cmn((b & c) | ((~b) & d), a, b, x, s, t);
  }

  function gg(a, b, c, d, x, s, t) {
  return cmn((b & d) | (c & (~d)), a, b, x, s, t);
  }

  function hh(a, b, c, d, x, s, t) {
  return cmn(b ^ c ^ d, a, b, x, s, t);
  }

  function ii(a, b, c, d, x, s, t) {
  return cmn(c ^ (b | (~d)), a, b, x, s, t);
  }

  function md51(s) {
  txt = '';
  var n = s.length,
  state = [1732584193, -271733879, -1732584194, 271733878], i;
  for (i=64; i<=s.length; i+=64) {
  md5cycle(state, md5blk(s.substring(i-64, i)));
  }
  s = s.substring(i-64);
  var tail = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];
  for (i=0; i<s.length; i++)
  tail[i>>2] |= s.charCodeAt(i) << ((i%4) << 3);
  tail[i>>2] |= 0x80 << ((i%4) << 3);
  if (i > 55) {
  md5cycle(state, tail);
  for (i=0; i<16; i++) tail[i] = 0;
  }
  tail[14] = n*8;
  md5cycle(state, tail);
  return state;
  }

  /* there needs to be support for Unicode here,
   * unless we pretend that we can redefine the MD-5
   * algorithm for multi-byte characters (perhaps
   * by adding every four 16-bit characters and
   * shortening the sum to 32 bits). Otherwise
   * I suggest performing MD-5 as if every character
   * was two bytes--e.g., 0040 0025 = @%--but then
   * how will an ordinary MD-5 sum be matched?
   * There is no way to standardize text to something
   * like UTF-8 before transformation; speed cost is
   * utterly prohibitive. The JavaScript standard
   * itself needs to look at this: it should start
   * providing access to strings as preformed UTF-8
   * 8-bit unsigned value arrays.
   */
  function md5blk(s) { /* I figured global was faster.   */
  var md5blks = [], i; /* Andy King said do it this way. */
  for (i=0; i<64; i+=4) {
  md5blks[i>>2] = s.charCodeAt(i)
  + (s.charCodeAt(i+1) << 8)
  + (s.charCodeAt(i+2) << 16)
  + (s.charCodeAt(i+3) << 24);
  }
  return md5blks;
  }

  var hex_chr = '0123456789abcdef'.split('');

  function rhex(n)
  {
  var s='', j=0;
  for(; j<4; j++)
  s += hex_chr[(n >> (j * 8 + 4)) & 0x0F]
  + hex_chr[(n >> (j * 8)) & 0x0F];
  return s;
  }

  function hex(x) {
  for (var i=0; i<x.length; i++)
  x[i] = rhex(x[i]);
  return x.join('');
  }

  function md5(s) {
  return hex(md51(s));
  }

  /* this function is much faster,
  so if possible we use it. Some IEs
  are the only ones I know of that
  need the idiotic second function,
  generated by an if clause.  */

  function add32(a, b) {
  return (a + b) & 0xFFFFFFFF;
  }

  if (md5('hello') != '5d41402abc4b2a76b9719d911017c592') {
  function add32(x, y) {
  var lsw = (x & 0xFFFF) + (y & 0xFFFF),
  msw = (x >> 16) + (y >> 16) + (lsw >> 16);
  return (msw << 16) | (lsw & 0xFFFF);
  }
  }

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

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
  "zu": "Zulu",
  "sva": "Svan",
  "lzz": "Laz",
  "xmf": "Mingrelian",
  "tcy": "Tulu",
  "bfq": "Badaga",
  "kfa": "Kodava",
  "xub": "Betta Kurumba",
  "yea": "Ravula",
  "tcx": "Toda",
  "kfe": "Kota",
  "gon": "Gondi",
  "kff": "Koya",
  "kxv": "Kuvi",
  "kfb": "Kolami",
  "pci": "Duruwa",
  "gdb": "Ollari",
  "brh": "Brahui",
  "kru": "Kurukh",
  "mjt": "Malto",
  "vro": "Võro",
  "liv": "Livonian",
  "vot": "Votic",
  "krl": "Karelian",
  "vep": "Veps"
}

$(window).on('load', function() {
  d3.json("../Data/words_and_languages/swadesh_list.json", function(error, words) {
    $("#table").append('<thead><tr id="thead"><th>English</th><th></th></tr></thead>');
    let url = new URL(window.location.href);
    let langs = url.searchParams.get("langs").split(',');
    let dir = url.searchParams.get("data");
    $("#table").append('<tbody>')
    for(var word in words) {
      a = '<a href="'+url.pathname.replace(/[^/]*$/, '')+"word.html?word="+words[word]+"&data="+dir+'">'
      html = '<tr id="'+words[word]+'"><td>'+a+words[word]+'</a></td><td>'+a+'&nbsp;</a></td></tr>';
      $("#table").append(html);
    }
    $("#table").append('</tbody>')


    langs.forEach(function (lang, index) {
      lang_path = md5(lang);
      let path = "../Data/protolanguages/"+lang_path+".json";
      if(dir){
        path = "../Data/trees/"+dir+"/protolanguages/"+lang_path+".json";
      }
      d3.json(path, function(error, data) {
        lang_name = lang;
        if(lang.includes(".")){
          lang_name = 'Reconstructed';

          var h1 = "Dictionary of reconstructed protolanguage " + lang;
          $('h1').append(h1);
          var p = "This language is an ancestor of modern languages ";
          var langs1 = lang.split(".");
          for (const [index, lang] of langs1.entries()) {
            var a = '<a href="' + url.pathname.replace(/[^/]*$/, '')+"language.html?langs="+lang+'&data='+dir+'">';
            if(index == langs1.length - 2){
              p += a + lang_codes[lang] + '</a>' + " and ";
            } else if (index == langs1.length - 1) {
              p += a + lang_codes[lang] + '</a>' + ". ";
            } else {
              p += a + lang_codes[lang] + '</a>' + ", ";
            }
          }
          var age = 2000 - langs1.length*175;
          p += (age < 0 ? Math.abs(age) + "BC " : age + "AD ") + "is the approximate date (without historical callibration) when this language was split into different languages.";
          $("p").append(p);

          shuffleArray(langs1);
          var dictionary = {}

          for (const lang of langs1.slice(0,10)) {
            lang_path = md5(lang);
            let path = "../Data/protolanguages/"+lang_path+".json";
            if(dir){
              path = "../Data/trees/"+dir+"/protolanguages/"+lang_path+".json";
            }
            $.getJSON(path, function(data){
              $.each(data, function(word, value){
                dictionary[lang+','+word] = value;
              });
            });
          }

          setTimeout(function(){
            var thead = '<th>'+lang_name+'</th><th></th>';
            for (const lang of langs1.slice(0,10)) {
              thead += '<th class="lang-header"><a href="'+url.pathname.replace(/[^/]*$/, '')+"language.html?langs="+lang+'&data='+dir+'">'+lang_codes[lang]+'</a></th>';
            }
            thead += langs1.length > 10 ? '<th class="ellipsis-header">...</th>' : '';
            $('#thead').append(thead);

            var trs = {}

            for (const lang of langs1.slice(0,10)) {
              for (var word in data) {
                var transcription = dictionary[lang+','+word];
                var td = '<td><a href="'+url.pathname.replace(/[^/]*$/, '')+"word.html?word="+word+"&data="+dir+'">['+transcription+']</a></td>';
                if (word in trs) {
                  trs[word] += td;
                }
                else {
                  trs[word] = td;
                }
              }
            }
            for (var word in trs) {
              var a = '<a href="'+url.pathname.replace(/[^/]*$/, '')+"word.html?word="+word+"&data="+dir+'">'
              var html = '<td>'+a+'['+data[word]+']</a></td><td id="arrow">'+a+'&rarr;</a></td>';
              var tr = html + trs[word];
              tr += langs1.length > 10 ? '<td></td>' : '';
              $('#'+word).append(tr);
            }
          }, 250);
        }
        else {
          lang_name = lang_codes[lang];
          $("h1").append("Dictionary of modern language " + lang_codes[lang]);
          $("#thead").append('<th>'+lang_name+'</th>'+(lang.includes(".") ? '<th></th>' : ''));
          for(var word in data) {
            a = '<a href="'+url.pathname.replace(/[^/]*$/, '')+"word.html?word="+word+"&data="+dir+'">'
            html = '<td>'+a+'['+data[word]+']</a></td>';
            $("#"+word).append(html);
          }
        }
      });
    });
  });
});
