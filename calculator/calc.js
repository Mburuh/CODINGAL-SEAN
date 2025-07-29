function getHistory(){
    return document.getElementById("history-value")
}
function printHistory(num){document.getElementById("history-value").innerText=num;}
function getOutput(){
    return document.getElementById("output-value").innerText
}
function printOutput(num){
    if(num=="-"){return ""}
    var n=Number(num)
    var value=n.toLocaleString("en")
    return value
}
function reverseNumberFormat(num){
    return Number(num.replace(/,/g,""))
}
var operator = document.gerElementsByClassname("operator")
for(var i=0;i<operator.length;i++){
    operator[i],addEventListener('click',function(){
        if(this.id=="clear"){
            printHistory("")
            printOutput("")
        }
        else if(this.id=="backspace"){
            var output=getOutput()
            var history=getHistory()
            if(output=="&&history!="")
        }
    })
}