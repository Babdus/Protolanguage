# Protolanguage Reconstruction Tool

## შესავალი

### ზოგადი დახასიათება

Protolanguage Reconstuction Tool (PRT) არის პროგრამა, რომელიც იღებს ინფუთად ბუნებრივი ენების ლექსიკონებს და აგენერირებს ამ ენების ნათესაობის ხეს აუთფუთად, რომელიც თითოეულ ნოუდში შეიცავს შუალედური ენების ლექსიკონებს.

აქ ლექსიკონში იგულისხმება სიტყვების სიმრავლე, რომლებსაც აქვთ ზუსტად იმავე რაოდენობის კოგნატი სიტყვა ყველა დანარჩენ განხილულ ენაში. ორი სიტყვა არის ურთიერკოგნატი, თუ ისინი სხვადასხვა ენაზე ერთსა და იმავე შინაარსს ატარებენ და, სავარაუდოდ, ერთი ძირიდან არიან ნაწარმოები.

მაგალითისთვის ავიღოთ სამი ენა და თითოში 4-4 სიტყვა. ინფუთი იქნება:

| ინგლისური  | გერმანული | ფრანგული |
| ---------- | ---------- | -------- |
| Cat  | Katze  | Chat  |
| Mother  | Mutter  | Mère  |
| Squirrel  | Eichhörnchen  | Écureuil  |
| Worm  | Wurm  | Ver  |

აუთფუთის ერთ-ერთი სავარაუდო ფორმა შეიძლება იყოს:

```
Node-1 (*katus, *mehter, *ekorel, *verm) [2800]
|   |
|   └── Node-2 (*katuz, *moder, *eṡkörel, *vorm) [1500]
|       |   |
│       |   └── გერმანული (Katze, Mutter, Eichhörnchen, Wurm)
|       |
│       └── ინგლისური (Cat, Mother, Squirrel, Worm)
|
└── ფრანგული (Chat, Mère, Écureuil, Ver)
```
სადაც ასტერისკით დაწყებული სიტყვები არის პროგრამის მიერ აღდგენილები და კვადრატულ ფრჩხილებში მოცემული რიცხვები არის სავარაუდო წლების რაოდენობა, რომლის წინაც არსებობდა ეს ენა.

### ცნებები და განმარტებები

აქ მოყვანილი იქნება ტერმინებისა და ცნებების განმარტებები, რომლებიც ამ დოკუმენტის განმავლობაში იქნება გამოყენებული:

##### ფონემა
ბგერა, რომელიც შეადგენს რომელიმე ენის ფარგლებში სიტყვის ელემენტარულ ერთეულს. ამ პროექტის ფარგლებში სიტყვებს ჩავწერ ფონემების მასივად IPA-ის (საერთაშორისო ფონეტიკური ანბანის) სიმბოლოებით. ფონემა წარმოდგენილია ბგერითი მახასიათებლების და მათი მნიშვნელობების სიით.

*მაგალითი*: /**ʃ**/ არის ფონემა (IPA-ს ფონემებს სტანდარტულად წერენ ხოლმე ორ დახრილ წილადის ხაზს შორის, როგორც აქ წერია), რომელიც აღნიშნავს ბგერა **შ**-ს ქართული სიტყვების აბსოლუტურ უმრავლესობაში და ინგლისურ სიტყვაბში **sh**-ს, მაგალითად **sh**eep-ში ან **ti**-ს - na**ti**on-ში. ამ ფონემის მახასიათებლებია:
* საწარმოთქმო ადგილი -> უკანანუნისმიერი
* ჰაერნაკადის ტიპი -> ფშვინვიერი
* რაგვარობა -> ნაპრალოვანი
* გვერდითობა -> არაგვერდითი
* ცხვირისმიერობა -> არაცხვირისმიერი
* ბაგისმიერობა -> არაბაგისმიერი
* წინასასიმიერობა -> არაწინასასისმიერი
* უკანასასისმიერობა -> არაუკანასასისმიერი
* ყელისმიერობა -> არაყელისმიერი

სადაც ისრების მარცხნივ წერია მახასიათებლები, რომლებიც ნებისმიერ ფონემას გააჩნა, ხოლო მარჯვენა მხარეს ამ მახასიათებლების მნიშვნელობებია /**ʃ**/-ს შემთხვევაში.

##### სიტყვა
ფონემების მასივი, რომელსაც აქვს ერთი კონკრეტული მნიშვნელობა.

##### ლექსიკონი
სიტყვების სიმრავლე, რომლებიც მიეკუთვნებიან რომელიმე კონკრეტულ ენას (ინფუთად მიცემულ ენასაც და აღდგენილსაც).

##### ხე
ენათა შორის ნათესაობის ხე, რომელსაც აქვს ერთი ფესვი ენა (პროტოენა) და ტოტებად იშელება, რომლის თითოეულ კვანძში არის შუალედური ენები, ხოლო ფოთლებში კი - ინფუთად გადმოცემული თანამედროვე ენები.

##### ფონემებს შორის მანძილი
ორ ფონემას შორის მანძილი არის რიცხვი, რომელიც ასახავს თუ რამდენი მახასიათებლით განსხვავდებიან ერთმანეთისგან, სადაც თითოეული მახასიათებლით განსხვავება შეიძლება იყოს ნებისმიერი რიცხვი, რომელიც იცვლება პროგრამის მიმდინარეობის განმავლობაში და დამოკიდებულია ამ მახასიათებლის მნიშვნელოვნების წონაზე (იხ. ბგერითი მახასიათებლის ცვლილების წონა).

##### სიტყვებს შორის მანძილი
ორ სიტყვას შორის მანძილი არის რიცხვი, რომელიც არის მინიმუმი მნიშვნელობა ერთი სიტყვიდან მეორეს მიღებისა ფონემების ცვლილების გზით. სადაც თითოეულ ფონემათა ცვლილებას აქვს შესაბამისი წონა განსაზღვრული ამ ფონემებს შორის მანძილით (იხ, ფონემებს შორის მანძილი).

##### ენებს შორის მანძილი
არის ორ ენას შორის მანძილი გამოხატული ერთი ან მრავალი რიცხვით, რომელიც ითვლება ამ ენების სიტყვების წყვილ-წყვილად შედარებით და სიტყვებს შორის მანძილის დათვლით. ერთი რიცხვის გამოყვანა ბევრი რიცხვიდან დამოკიდებულია ალგორითმზე, რომელიც შემდეგში იქნება განხილული.

##### ბგერითი მახასიათებლის ცვლილების წონა
არის რიცხვი, რომელიც ასახავს, თუ რამდენი დროის პირობითი ერთეული სჭირდება ბგერის ერთ მახასიათებელს მეორე მახასიათებლად გადასაქცევად. სწორედ ამ დროის ერთეულებში იქნება წარმოდგენილი საბოლოოდ მიღებული ხეც (რაც მერე ისტორიასთან თანხვედრით შეიძლება წლებზე დასკალირდეს).

## პრობლემის დასახვა

იმისათვის რომ ამ პროგრამამ აღადგინოს ენები მათი რეალურ ისტორიულ მნიშვნელობებთან მაქსიმალურად მსგავსად, თეორიულ შემთხვევაში საჭიროა ვიცოდეთ ყველა შესაძლო ბგერათცვლილების ალბათობა დროის რამე პერიოდში. ეს ალბათობები შეიძლება დამოკიდებული იყოს არამხოლოდ ამ ფონემების ბგერით მახასიათებლებზე და მათი მნიშვნელობების წონაზე, არამედ ასევე იმ კონტექსტზე, რომელშიც ისინი იცვლებიან. ლინგვისტიკაში ჩატარებული კვლევების მიხედვით მართლაც ძალიან განსხვავდება სხვადასხვა კონტექსტებში ერთი და იგივე ფონემბის ცვლილებები. ეს კონტექსტი შეიძლება იყოს ამ ფონემის მეზობელი ფონემების თვისებები; ასევე კონტექსტი შეიძლება იყოს მთლიანად ენის მახასიათებელი (მაგალითად, რამდენად მიდრეკილია ეს ენა თანხმოვნების დარბილებისკენ), რომელიც ვარირებს სხვადასხვა ენათა ჯგუფებს შორის; ან კონტექსტი იყოს დროის პერიოდი, რომელშიც ეს ცვლილებები მოხდა; ან სულაც რამე ისეთი კონტექსტი, რომლის ვარაუდიც ზეპირად მხოლოდ ადამიანური კვლევის პირობებში ძნელი აღმოსაჩენია. პროგრამის მიზანი არის მაქსიმალურად ზუსტად ამოიცნოს ეს ბგერათცვლილებების ალბათობები მათი კონტექსტების გათვალისწინებით და შემდეგ ეს ცოდნა გამოიყენოს იმაში, რომ აღადგინოს ხე და მასში ყველა საშუალედო თუ საწყისი პროტოენა.

### ლინგვისტური ბექგრაუნდი და საჭიროება

ლინგვისტების ერთ-ერთ ძირითად საკვლევ სფეროს სწორედ პროტოენების აღდგენა და მათი ხეების შედგენა წარმოადგენს. 150 წელზე მეტია ამ პრობლემას მეტ-ნაკლებად სტრუქტურირებული მეტოდიკით ათასობით ენათმეცნიერი ეჭიდება და გარკვეულ შედეგსაც მიაღწიეს, თუმცა, იმის გამო რომ გასათვალისწინებელია მილიონობით მონაცემი, ეს იმდენად ხანგრძლივ და რთულ სამუშაოსთანაა დაკავშირებული, რომ ძნელია თითოეული ადამიანის ნამუშავრის სანდოობაზე თავის დადება. სწორედ ეს ფაქტორები გახდა იმის მიზეზი, რომ ამ საქმის მექანიზაცია მეცადა.

ამ პროგრამის არსებობის შემთხვევაში რამდენიმე ათასწლეულის განმავლობაში არსებული ყველა შესაძლო ენის რეკონსტრუირებაა შესაძლებელი, რომელიც ენათმეცნიერებს მოაცილებს დამღლელ მექანიკურ საქმეს და მეტ დროს მისცემს მეტად მეცნიერული კვლევის ჩასატარებლად, ბევრად ადვილად გაიშიფრება ჯერაც გაუშიფრავი ძველი ტექსტები და მარტივად გამოაშკარავდება ცრუმეცნიერული დასკვნები ენების შესახებ, რომლებიც შეიძლბეა ხშირად პოლიტიკური მიზნებითაც ყოფილიყო გამოყენებული.

ამ პროგრამის შედეგის ინტერდისციპლინარულად გამოყენება, ანუ კაცობრიობის გენეტიკურ კველვებათან, არქეოლოგიურ მასალასთან და ისტორიულ წყაროებთან ერთად განხილვა ბევრად მეტად მოჰფენს ნათელს ჩვენს ისტორიას, არამარტო მეფეებისა და ბრძოლების ისტორიას, არამედ ჩვეულებრივი ხალხის ცხოვრებებში ჩაგვახედებს. სწორედ ამის გამო ამ პროექტს "დროის მანქანა 1.0"-ს ვეძახი.

### მსგავსი პროექტების მიმოხილვა

ბოლო ათწლეულის განმავლობაში მსგავსი პროექტები არაერთი შექმნილა, თუმცა მათი უდიდესი უმეტესობა მხოლოდ ენათა ხის დაგენერირებით შემოიფარგლება. მხოლოდ ერთი პროექტი არსებობს, რომლიც პროტოენების აღდგენასაც შეეჭიდა.

[ეს სტატია](https://www.pnas.org/content/pnas/110/11/4224.full.pdf) არის სწორედ ამ ერთადერთი პროქტის შესახებ. ქვემოთ ჩამოვწერ ჩემი და მათი პროექტის მსგავსებებს და შემდეგ განსხვავებებს:

|   | Alexandre Bouchard-Côté, David Hall , Thomas L. Griffiths and Dan Klein  | ალექსანდრე აბრამიშვილი  | კომენტარი  |
| --- | --- | --- | --- |
| ინფუთი  | ენების ლექსიკონები  | *იგივე*  |   |
| აუთფუთი  | ენათა ხე და ნოუდებში აღდგენილი ენები, ასევე თითოეულ წიბოზე ყველაზე გავრცელებული ბგერათცვალებადობა  | ენათა ხე და ნოუდებში აღდგენილი ენები  | მიუხედავად იმისა, რომ ჩემი საწყისი იდეა წიბოებზე ბგერათცვალებადობის ტრენდების ჩვენებას არ გულისხმობს, ამ მონაცემის აუთფუთში გამოტანა უკვე არსებული არქიტექტურით უმარტივესი ფუნქციონალი იქნება, თუკი ამის საჭიროებას დავინახავ  |
| მონაცემების შეგროვება  | ავსტრონეზიური ენათა ოჯახის 700-ამდე ენის ლექსიკონები  | Wiktionary-ის API  | ჩემს პროგრამას მეტი მოქნილობა აქვს ინფუთის მხრივ და ყოველი ახალი ხის დაგენერირება არ იქნება დამოკიდებული ადამიანურ შრომაზე |
| ლინგვისტური მოდელი  | პირდაპირ IPA-თი ჩაწერილი ფონემები  | IPA-თი ჩაწერილი თითოეული ფონემა იქნება შენახული ბგერითი მახასიათებლების ვექტორად  | იმის გამო, რომ ფონემები ფიზიკური მახასიათებლების გამო ზოგი ერთმანეთს ძალიან ჰგავს და ზოგიც თითქმის არა, მათი შენახვა მათი მახასიათებლების ვექტორებით უფრო მიახლოებულ მოდელს ქმნის იმისათვის, რომ ბგერების ცვლილებების ალბათობები აღმოვაჩინოთ, თანაც ჩემი მიდგომით თეორიულად ყველა ფონემის მიღებაა შესაძლებელი (დაახლოებით 10 000) მხოლოდ 9 მახასიათებლით და ალბათობების მატრიცაც ბევრად პატარა იქნება და შესაბამისად ნაკლებ დროს მოიხმარს მათი დათვლა ვიდრე პირდაპირ ფონემების ალბათობების  |
| სიტყვებს შორის მანძილის დათვლა  | Levenshtein-ის edit distance, რომელიც 3 მოქმედებას იყენებს: ქარაქტერის ჩანაცვლებას, გაქრობასა და გაჩენას | Damerau–Levenshtein-ის edit distance-ის გავრცობილი ვარიანტით, რომელიც ერთეულად არა ქარაქტერს, არამედ ვექტორს იღებს და აქვს 6 სხვადასხვა მოქმედების ჩატარების უფლება: 1. ერთი ფონემის ჩანაცვლება (ერთი მახასიათებლით განხვავებულით), 2. ფონემის გაჩენა (n მახასიათებლიანი), 3. გაქრობა (n მახასიათებლიანი), 4. მეზობლების გადანაცვლება, 5. მეზობლების გაერთიანება, 6. ფონემის ორად გაყოფა  | მიუხედავად იმისა, რომ სტანდარტული ლევენშტაინის მანძილით დათვლილი ცვლილებები ერთი ენის ფარგლებში ორთოგრაფიული შეცდომების უმეტესობას ფარავს, ენათა შორის ცვალებადობაზე ეს არ ვრცელდება და 3 ყველაზე გავრცელებულ ბგრათცვლილებას არ ითვალისწინებს, რომლებიცაა ფონემების შერწყმა, ფონემების გადანაცვლება და ფონემების განცალკევება. ჩემი ალგორითმი ამ დამატებით სამ ცვლილებასაც შეიცავს და უფრო დახვეწილი შედეგის მიღებას, ვვარაუდობ.  |
| პროტოენების აღდგენა  | ჭეშმარიტი კოგნატების სიმრავლეების გამოყოფით და ბგერათცვლილებების ალბათობაზე დაფუძნებით მშობელ ნოუდებში შვილების ლექსიკონებიდან მშობლის ლექსიკონის აღდგენა  | *იგივე*  | თვითონ ეს პროცესი კი იგივე იქნება ჩემს შემთხვევაშიც, მაგრამ იმის გამო რომ მოდელი მაქვს განსხვავებული ჩემი პროგრამის მიერ აღდგენილი პროტოენები არ იქნება შეზღუდული კონკრეტული ფონოლოოგიით (ფონემათა სიმრავლით). ანუ შეიძლება მივიღოთ ენა, რომელშიც ისეთი ბგერებია, რომელიც არცერთ თანამედროვე ენაში არ გვხვდება, რაც რეალურ პროცეს შეესაბამება.  |
| ბგერათცვლილებების ალბათობების სწავლა  | იტერაციული machine learning ალგორითმი, რომელიც საწყის ხეში სწავლობს ყველა ბგერათცვლილების ალბათობას და შემდეგ ამ ალბათობებზე დაყრდნობით აგებს ხელახლა მთელ ხეს. ეს პროცესი მიმდინარეობს იქამდე სანამ ხე არ დაქონვერჯდება, და დაქონვერჯება გარანტირებულია იმით, რომ ყოველ მომდევნო იტერაციაზე ალგორითმი ენებს შორის წიბოების სიგრძეებს ამცირებს (ანუ ოპტიმალურ გადასვლების გრაფს აგებს)  | *იგივე*  | ამ ეტაპზე შეიძლება deep-learning-ის გამოყენება Expectation–maximization ალგორითმის ნაცვლად, ან ნებისმიერი ML მიდგომის, რომელიც აღმოაჩენს და შეისწავლის ხეში ბგერათცვლილებების ალბათობებს  |


ფონემის მაგივრად მახასიათებლების მოდელი:

* ბევრად პატარა მოდელით ბევრად მეტი ინფორმაციის ჩაწერა

ნებისმიერ-ფონოლოგიანი ენის შესაძლებლობა
სტრინგზე ოპერაციები:

* ცვლილება (ერთი მახასიათებლის)
* გაჩენა (n მახასიათებლიანი)
* გაქრობა (n მახასიათებლიანი)
* მეზობლების გადანაცვლება
* მეზობლების გაერთიანება
* ფონემის ორად გაყოფა

### Uniqueness and Usability of this Project

## Methods and Tools

### Brief Plan of Methods and Tools

### Data Collection

### Creating Model

### Constructing Tree

#### სიტყვების შედარება

#### ენების შედარება

#### Threshold-ების დადება

#### პირველადი ხის დაგენერირება

#### მშობელ კვანძებში ენების დაგენერირება

##### აღდგენილი ენების სიტყვების შედარებით კოგნატებისა და არაკოგნატების გამოყოფა

##### არაკოგნატი შთამომავლების შემთხვევაში მშობელში არჩევა სიტყვის მშობლის დედმამიშვილის შესაბამისი სიტყვიდან

### Self-learning AI Iterations

## Conclusion

## Bibliography
