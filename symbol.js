//without Symbol implementation
var map = {};
setProp(map);
setProp2(map);

function setProp(map) {
  map.prop = "hey";
}

function setProp2(map) {
  map.prop = "hey, version 2"; // overrided previous prop
}
console.log(map) // { prop: "hey, version 2"}

//after implementing Symbol data type.
var dict = {};
var symbol1 = Symbol("prop");
var symbol2 = Symbol("prop"); // same name, different instance – so it's a different symbol!
dict[symbol1] = 1;
dict[symbol2] = 2; // doesn't override the previous symbol's value
console.log(dict[symbol1] + dict[symbol2]); // 3
