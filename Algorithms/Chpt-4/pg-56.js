///// String.concat
var string1 = "If I was creating this algorithm";
var string2 = "in Python instead of Javascript,";
var string3 = "I would not need to add all of these semicolons.";

var sliceString = "This is a string that is going to get chopped up into lots of little strings";

var trimString = " \nThis is a ver y  tricky \t esc ape string \t";

var string = {
  concat : function(){
    var newString = "";
    for (var i = 0; i < arguments.length; i++) {
      if(typeof arguments[i] === "string"){
        newString += arguments[i] + " ";
      }
      else{
        console.warn("Invalid data type: All arguments passed to .concat() method must be strings");
      }
    }
    return newString;
  },
  slice : function(string, start, end){
    if(typeof string === "string"){
      var newString = "";
      var stringArray = string.split("");
      if(typeof end === "undefined"){
        end = string.length;
        if(start < 0){
          start = end + start;
        }
      }
      console.log("slicing from " + start + " to " + end);
      for (var i = start; i < end; i++) {
        newString += stringArray[i];
      }
      console.log(newString);
      return newString;
    }
    else{
      console.warn("Invalid data type: First argument passed to .slice() method must be a string");
      return string;
    }
  },
  trim : function(string){
    if(typeof string === "string"){
      var newString = "";
      var stringArray = string.split("");
      for (var i = 0; i < stringArray.length; i++) {
        if(stringArray[i] !== " "){
          if(stringArray[i] !== "%5C" && stringArray[i] !== "n" && stringArray[i] !== "t"){
            newString += stringArray[i];
          }
        }
      }
      console.log(newString);
      return newString;
    }
    else{
      console.warn("Invalid data type: First argument passed to .trim() method must be a string");
      return string;
    }
  },
};

//var statement = string.concat(string1, string2, string3);
//console.log(statement);

//string.slice(sliceString, 9, 20);
//console.log("\nBonus Negative value slice");
//string.slice(sliceString, -20);

string.trim(trimString);
