document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block'
  document.querySelector('#compose-view').style.display = 'none'

  const view = document.querySelector('#emails-view')

  // Show the mailbox name
  view.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`
  
  // Take emails
  fetch('/emails/' + mailbox)
  .then(response => response.json())
  .then(emails => {

    emails.forEach(email => {
      // Create element div
      let div = document.createElement('div')

      // Assign class to read or unread emails
      div.className = (email.read) ? 'read' : 'unread';

      // Append appropriate content to the div
      div.innerHTML = `
          <span id="sender">${email['sender']}</span>
          <span id="subject">${email['subject']}</span>
          <span id="timestamp">${email['timestamp']}</span>
      `
      view.append(div)
    })
  })
   
}