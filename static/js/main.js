/*
function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

btn.onclick = function () {
  const rndCol =
    "rgb(" + random(255) + "," + random(255) + "," + random(255) + ")";
  document.body.style.backgroundColor = rndCol;
};
*/
function show_me(id, type )
{
  var id = id
  var type = type
  var data = confirm("Вы хотите удалить это?");
  if (data){
    window.location.href = "http://127.0.0.1:5000/remove_item/" + type + "/"+ id;}
}