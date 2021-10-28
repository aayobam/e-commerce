$(document).ready(function() {
      $('#payment-form').on('submit', function(event) {
         event.preventDefault();
   
         $.ajax({
            url: '{% url "modal-form" %}',
            type: 'POST',
            // headers: {'X-CSRFToken': '{{ csrf_token }}'},
            data: $('#payment-form').serialize(),
   
            success: function(data) {
               $('#payment-form .modal-body').html(data);
            }
         });
      });
});


//payment form validation
function validateForm(){
   let card_number = document.getElementById("card_number").value()
   let cvv = document.getElementById("cvv").value()
   let exp = document.getElementById("exp").value()

   if (isNaN(card_number) || card_number < 16 || card_number >16 || card_number == ""){
      window.alert("invalid input. card number must be be a 16 digit number")
      card_number.focus()
      return false
   }
   else if (isNaN(cvv) || cvv < 3 || card_number > 3 || cc == ""){
      window.alert("invalid input. cvv must be be a 3 digit number")
      cvv.focus()
      return false
   }
   else if (exp < 5 || exp > 5 || exp == ""){
      alert("invalid input. must provide in month/year format eg 10/21")
   }
   else{
      return true
   }
};
