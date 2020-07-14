const email = null;

function validateEmail(email) {
  return email.match(/@/) ? email : new Error(`invalid email:${email}`)
}

try {
  const validatedEmail = validateEmail(email);
  if (validatedEmail instanceof Error) {
    console.error(`Error: ${validatedEmail.message}`)
  } else {
    console.log(`Valid email: ${validatedEmail}`);
  }
} catch (e) {
  console.error(`Error: ${e.message}`)
}
