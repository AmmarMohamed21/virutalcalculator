function writebutton(value) {
    if (document.getElementById("equation").value.length < 50)
    {
        document.getElementById("equation").value = document.getElementById("equation").value + value ;
    }
}
function delettt()
{
    var len = document.getElementById("equation").value.length;
    var curequation = document.getElementById("equation").value;
    document.getElementById("equation").value = curequation.substring(0,len-1);
}
function reset()
{
    document.getElementById("equation").value = "";
}
    
