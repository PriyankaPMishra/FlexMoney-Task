// Handle form submission
document.getElementById('admissionForm').addEventListener('submit', function(event) {
  // Get form values
  const name = document.getElementById('name').value;
  const age = document.getElementById('age').value;
  const batch = document.getElementById('batch').value;

  // Validate age between 18 and 65
  if (age < 18 || age > 65) {
    alert('Age must be between 18 and 65.');
    event.preventDefault(); // Prevent form submission if validation fails
    return;
  }
  // Allow form submission if validation passes
});



// // Handle form submission
// document.getElementById('admissionForm').addEventListener('submit', function(event) {
//   event.preventDefault(); // Prevent default form submission

//   // Get form values
//   const name = document.getElementById('name').value;
//   const age = document.getElementById('age').value;
//   const batch = document.getElementById('batch').value;

//   // Validate age between 18 and 65
//   if (age < 18 || age > 65) {
//     alert('Age must be between 18 and 65.');
//     return;
//   }

//   // Send form data to the server
//   fetch('/register', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({ name, age, batch })
//   })
//   // .then(response => response.json())
//   // .then(data => {
//   //   console.log('Success:', data);
//   //   // Redirect to payment page after successful form submission
//   //   window.location.href = `payment.html?name=${name}`;
//   // })
//   // .catch((error) => {
//   //   console.error('Error:', error);
//   //   // Handle error, show an error message, etc.
//   // });
// });
