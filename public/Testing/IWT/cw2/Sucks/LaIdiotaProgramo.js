// Fo

function ek()
{
  //alert("This just in: You suck!");
  var elt = document.createElement("p");
  var body = document.getElementsByTagName("body")[0];

  elt.appendChild(document.createTextNode("JavaScript was here!"));

  elt.style.backgroundColor = "#AAE";
  elt.style.color = "black";
  elt.style.textAlign = "right";
  elt.style.fontSize = "0.7em";
  elt.style.border = "black 2px";
  elt.style.borderStyle = "solid none";
  elt.style.padding = "0.5ex 1ex";

  body.appendChild(elt);
}
