///// String.concat
var string1 = "If I was creating this algorithm";
var string2 = "in Python instead of Javascript,";
var string3 = "I would not need to add all of these semicolons.";

var sliceString = "This is a string that is going to get chopped up into lots of little strings";

var trimString = "\n \n \t \nThis is a string that is going to be trimmed  \t here\t \n";

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
    //Check to make sure argument is string
    if(typeof string === "string"){
      //Create holder for new string to return and break sting to be trimmed into array
      var newString = "";
      var stringArray = string.split("");
      //startFound and endFound will hold the indexes for the content of the string that will be returned
      var startFound = -1;
      var endFound = -1;
      //Iterate inwards from both ends of the array- looking for the first values on each end that are not trimmable
      for (var i = 0; i < Math.floor(stringArray.length / 2); i++) {
        //start and end are optional variables to help improve readablility.
        var start = i;
        var end = (stringArray.length -1) - i;
        //If the start and end index of the content that should not be trimmed have been found- Loop through that content and add it to the new string.
        if (startFound !== -1 && endFound !== -1 ){
          console.log("start and end found");
          for (var j = startFound; j <= endFound; j++) {
            newString += stringArray[j];
          }
          //Return at the new string and end the method
          console.log(newString);
          return newString;
        }
        // If start has not been found, check the next value to see if it is trimmable.
        if(startFound === -1 ){
          console.log("looking for start at: ", start);
          if( (stringArray[start] !== " ") && (stringArray[start] !== "\n" ) && (stringArray[start] !== "\t" ) ){
            //If start is not trimmable- set it as the start of the string to be returned
            console.log("Start found at: ", start);
            startFound = start;
          }
        }
        // If end has not been found, check the next value to see if it is trimmable.
        if(endFound === -1 ){
          console.log("looking for end at: ", end);
          console.log("/t");
          if( (stringArray[end] !== " ") && (stringArray[end] !== "\n" ) && (stringArray[end] !== "\t" ) ){
            //If end index is not trimmable- set it as the end of the string to be returned
            console.log("End found at: ", end);
            endFound = end;
          }
        }
      }
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
