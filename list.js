var slider = document.getElementById("myRange");
var output = document.getElementById("slider__value");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}

function generateProfile() {
  // alert('aaaa');
  document.getElementById("demo").innerHTML = 
  "- Alpha Metallurgical Resources In</br> - Cvr Partners LP</br> - Alpha Asana Inc Cl A</br> - Aehr Test Systems</br> - Sm Energy Company</br> - Silverbow Resources Inc</br> - Urban One Inc</br> - Weatherford International Plc</br> - Avis Budget Group</br> - Consol Energy Inc</br>";
      }

  document.getElementById("scriptButton").addEventListener("click", hello);

// object.onclick = generateProfile()
// {
//   window.alert( "aaa" );
// };

document.getElementById("scriptButton").addEventListener("click", generateProfile);