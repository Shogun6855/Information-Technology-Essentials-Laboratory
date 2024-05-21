function testeval() {
  var Fname, Lname, Password, Repassword;
  Fname = document.getElementsByName("fname");
  Lname = document.getElementsByName("lname");
  Password = document.getElementsByName("password");
  Repassword = document.getElementsByName("repassword");
  if (!allLetter(Fname[0]) || !allLetter(Lname[0])) {
    alert("Name must not contain any numbers");
    return null;
  }

  if (chartest(Password[0]) || allLetter(Password[0])) {
    alert("Password must contain special characters or numbers");
    return null;
  }

  if (Password[0].value.length < 6) {
    alert("Password must be atleast 6 characters");
    return null;
  }
  if (Password[0].value.localeCompare(Repassword[0].value)) {
    alert("The passwords do not match");
    return null;
  }
}

function allLetter(inputtxt) {
  var letters = /^[A-Za-z]+$/;
  return inputtxt.value.match(letters) ? true : false;
}

function chartest(inputtxt) {
  return inputtxt.value.match(/^[^a-zA-Z0-9]+$/) ? true : false;
}
