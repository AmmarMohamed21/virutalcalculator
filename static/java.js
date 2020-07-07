function writebutton(value) {
    buttonsound();
    if (document.getElementById("equation").value.length < 50)
    {
        document.getElementById("equation").value = document.getElementById("equation").value + value ;
    }
}
function delet()
{
    buttonsound();
    var len = document.getElementById("equation").value.length;
    var curequation = document.getElementById("equation").value;
    document.getElementById("equation").value = curequation.substring(0,len-1);
}
function reset()
{
    buttonsound();
    document.getElementById("equation").value = "";
}
    
function buttonsound()
{
    var audio = new Audio('/static/audio/buttonsound.mp3');
    audio.play();
}
