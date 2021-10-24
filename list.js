var slider = document.getElementById("myRange");
var output = document.getElementById("slider__value");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}

function generateProfile() {
  alert('aaaa');
  }
  document.getElementById("scriptButton").addEventListener("click", hello);

// object.onclick = generateProfile()
// {
//   window.alert( "aaa" );
// };

document.getElementById("scriptButton").addEventListener("click", generateProfile);