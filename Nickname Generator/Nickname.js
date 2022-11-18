function randNickname() {

    let firstName = firstNameEl.value;
    let lastName = lastNameEl.value;
  
  
    let randomNickname = Math.floor(Math.random() * mynicknameArray.length);
    
    
    nicknameOutputEl.innerHTML = firstName + ' ' + mynicknameArray[randomNickname] + ' ' + lastName;
  }
  
  function allNickname() {
  
    let firstName = firstNameEl.value;
    let lastName = lastNameEl.value;
    let allNicknames = "";
  
    
    for (let rN = 0; rN < mynicknameArray.length; rN++) { allNicknames += firstName + ' ' + mynicknameArray[rN] + ' ' + lastName + "<p>";
    }
  
    nicknameOutputEl.innerHTML = allNicknames;
  }
    