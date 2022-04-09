lastUrl = location.href;

new MutationObserver(() => {
  const url = location.href;
  if (url !== lastUrl) {
    lastUrl = url;
    // onConfirmation();
  }
}).observe(document, { subtree: true, childList: true });

function onConfirmation(item, replacement) {
    console.log( verifyBtn )
    chatData = JSON.parse(localStorage.getItem("chatData"));
    console.log( chatData );

    
    setInputValuesToChatData(chatData)
    item.remove()
    replacement.style.display = "block";

}

function setInputValuesToChatData( chatData ) {
  console.log(chatData)  
  // Get elements
    confirmationInputs = document.querySelectorAll( '.confirmationElem' )
    console.log( confirmationInputs )
    
  for ( let i = 0; i < confirmationInputs.length; i++ ) { 
    console.log( confirmationInputs[i] )
    let name = confirmationInputs[i].getAttribute( 'name' );

    console.log( name )
    if ( name in chatData ) {
      confirmationInputs[i].setAttribute('value', `${chatData[name]}`);
      console.log( confirmationInputs[i] )
      console.log('Name in chatData!')
    }
    else {
      console.log('Name not found')
    }
  }
  
    

    
    // console.log(confirmationInputs)
}
