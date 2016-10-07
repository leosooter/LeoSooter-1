/////Is Word Alphabetical is in 2.2 Day 2

/////D gets Jiggy

var coolName = "Leo";

function coolify(name){
  if (typeof name === "string" && name.length > 0){
    name = name.split("");
    name.push(" to the ");
    name.push(name[0].toUpperCase());
    name.push("!");
    for (var i = 0; i < name.length-1; i++) {
      name[i] = name[i+1];
    }
    name.pop();
    name[0] = name[0].toUpperCase();
    name = name.join("");
    console.log(name);
  }
  else{
    console.warn("Invalid Name");
  }
  return name;
}

//coolify(coolName);

/////Common Suffix

var rhymeArray = ['book', 'look', 'shook', 'mistook', 'took'];
var rhymeArray = ['white', 'black', 'yellow'];

function rhymeFinder(array){
  if(typeof array === "object" && array.length > 0){
    var suffix = [];
    var j = 1;
    var match = true;
    while (match) {
      var letter = array[0].charAt(array[0].length - j);
      for (var i = 1; i < array.length; i++) {
        console.log("checking letter " + j);
        if(array[i].charAt(array[i].length - j) !== letter){
          match = false;
          break;
        }
      }
      if(match){
        suffix.push(letter);
        j++;
      }
    }
    for (var k = 0; k < Math.floor(suffix.length/2); k++) {
      var length = (suffix.length-1) -k;
      var value = suffix[k];
      suffix[k] = suffix[length];
      suffix[length] = value;
    }
    console.log(suffix);
    return suffix;
  }
}

//rhymeFinder(rhymeArray);


/////Book Index
pageIndex = [1,2,13,14,15,20,22,23,25,26,27,28,35,37,38,50];

function bookIndex(array){
  //Sting that final index will be stored in
  var indexStr = "";
  //Loop trhough array 1 time
  for (var i = 0; i < array.length; i++) {
    //If the value is not one less than the value in front- it closes a set of pages
    if(array[i] + 1 !== array[i+1]){
      console.log(array[i] + " is closer");
      indexStr += array[i];
      //checks to see if value is last in the array- if so, leave off coma
      if (i < array.length-1){
        indexStr += ", ";
      }
    }
    //if the value is one less than the value in front but not 1 more than the value behind it opens a new set of pages
    else if(array[i] + 1 === array[i+1] && array[i] - 1 !== array[i-1] ){
      console.log(array[i] + " is opener");
      indexStr += array[i] + "-";
    }
  }
  console.log(indexStr);
  return indexStr;
}

bookIndex(pageIndex);
