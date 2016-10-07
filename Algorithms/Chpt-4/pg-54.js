var coinChange = {
  dollars : 0,
  quarters : 0,
  dimes : 0,
  nickels : 0,
  pennies : 0,
  makeChange : function(cents){
    if(cents >= 100){
      this.dollars = Math.floor(cents/100);
      cents -= (this.dollars * 100);
      console.log(coinChange.dollars + " dollars | " + cents + " cents left");
    }
    if(cents >= 25){
      this.quarters = Math.floor(cents/25);
      cents -= (this.quarters * 25);
      console.log(coinChange.quarters + " quarters | " + cents + " cents left");
    }
    if(cents >= 10){
      this.dimes = Math.floor(cents/10);
      cents -= (this.dimes * 10);
      console.log(coinChange.dimes + " dimes | " + cents + " cents left");
    }
    if(cents >= 5){
      this.nickels = Math.floor(cents/5);
      cents -= (this.nickels * 5);
      console.log(coinChange.nickels + " nickels | " + cents + " cents left");
    }
    if(cents >= 1){
      this.pennies = Math.floor(cents/1);
      cents -= (this.pennies * 1);
      console.log(coinChange.pennies + " pennies | " + cents + " cents left");
    }
    return coinChange;
  },
};

//var change = coinChange.makeChange(655);
var numbers = [15,8,7,3,2,5,-9,12];
var arrayCalc = {
  min : 0,
  max : 0,
  avg : 0,
  calculate : function(array){
    this.min = array[0];
    this.max = array[0];
    var sum = 0;
    for (var i = 0; i < array.length; i++) {
      sum += array[i];
      if(array[i] > this.max){
        this.max = array[i];
      }
      else if(array[i] < this.min){
        this.min = array[i];
      }
    }
    this.avg = sum/array.length;
    console.log("Min = " + this.min + ", Max = " + this.max + ", Avg = " + this.avg);
    return arrayCalc;
  },
};

var cal = arrayCalc.calculate(numbers);
