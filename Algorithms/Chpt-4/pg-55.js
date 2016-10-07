///// Zip arrays to map- function will ignore any extra keys or values
var animal = ["baboon","lion","leopard","bunny","hippo","hyena","buffalo","warthog","giraffe"];
var danger = ["low","high","medium","none","highest","low","high","low"];
function zipMap(keyArray, valueArray){
  var newObj = {};
  var count = keyArray.length;
  if(keyArray.length > valueArray.length){
    count = valueArray.length;
  }
  for (var i = 0; i < count; i++) {
    newObj[keyArray[i]] = valueArray[i];
  }
  return newObj;
}

var canIPetIt = zipMap(animal, danger);
for(var key in canIPetIt){
  console.log("\n" + key + " | " + canIPetIt[key]);
  if(canIPetIt[key] === "none"){
    console.log("You can pet it!");
  }
}

/////Invert Hash Array- Instructions are vauge but I am assuming we are returning a new array rather than changing key names in old array.

function invertHash(obj){
  var newObj = {};
  for(var key in obj){
    newObj[obj[key]] = key;
  }
  return newObj;
}

var myObj = {
  "function" : "dictionary",
  "array" : "list",
  "else if" : "elif",
  "none" : "tupile",
};

var reversedMyObj = invertHash(myObj);
console.log("\nReversed function :");
for(var key in reversedMyObj){
  console.log(key + " | " + reversedMyObj[key]);
}

//// Array length w/out .length

function countKeys(obj){
  var count = 0;
  for(var key in obj){
    count ++;
  }

  console.log("\nNumber of keys = " + count);
  return count;
}

countKeys(myObj);
