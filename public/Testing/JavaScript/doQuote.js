// Good:
// http://developer.apple.com/internet/webcontent/xmlhttpreq.html

var req;

function ek()
{
  doQuote();
  var q = document.getElementById("quote")
  //q.createAttribute("onclick");
  q.setAttribute("onclick", "doQuote()");
}

function doQuote()
{
  var uri = "quotes";
  req = new XMLHttpRequest();
  req.onreadystatechange = processChange;
  req.open("GET", uri, true);
  req.send(null);
}

function processChange()
{
  if (req.readyState == 4)
  {
    if (req.status == 200 || req.status == 304)
    {
      quotes = req.responseXML.documentElement.getElementsByTagName("li");
      var numQuotes = quotes.length;
      var quote = quotes[Math.round(Math.random()*(numQuotes-1))].firstChild.nodeValue;
      insertQuote(quote);
    } else {
      insertQuote("Oops. " + req.status + " " + req.statusText);
    }
  }
}

function insertQuote(text)
{
  var q = document.getElementById("quote");
  while (q.hasChildNodes())
  {
    q.removeChild(q.firstChild)
  }
  q.appendChild(document.createTextNode(text));
}

// https://lists.latech.edu/pipermail/javascript/2001-June/001057.html
function delay(gap)
{
  var then,now;
  then=new Date().getTime();
  now=then;
  while((now-then)<gap)
  {
    now=new Date().getTime();
  }
}
