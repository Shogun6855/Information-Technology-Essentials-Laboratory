function testeval() {
  var Fname, Lname, Password, Repassword, Username, Pin, Mobile;
  Fname = document.getElementsByName("fname");
  Lname = document.getElementsByName("lname");
  Password = document.getElementsByName("password");
  Repassword = document.getElementsByName("repassword");
  Username = document.getElementsByName("userid");
  Pin = document.getElementsByName("pincode");
  Mobile = document.getElementsByName("mobile");
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
  if(Username[0].value.length>16) {
    alert("Username should not exceed 16 characters");
    return null;
  }
  if(checkWhitespace(Username[0])) {
    alert("Username must not contain any space");
    return null;
  }
  if (Password[0].value.localeCompare(Repassword[0].value)) {
    alert("The passwords do not match");
    return null;
  }
  if(Pin[0].value.length!=6) {
    alert("Pincode must be 6 digits");
    return null;
  }
  if(Mobile[0].value.length!=10) {
    alert("Mobile number must be 10 digits");
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

function checkWhitespace(str) {
  return /\s/.test(str.value);
}
