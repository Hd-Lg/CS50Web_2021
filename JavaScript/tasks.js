// Wait for page to load
document.addEventListener( 'DOMContentLoaded', function() {

    // Select the submit button and input
    const submit = document.querySelector( '#submit' );
    const newTask = document.querySelector( '#task' );

    // Disable submit button by default
    submit.disabled = true;

    // Listen for input to be typed 
    newTask.onkeyup = () => {
        if ( newTask.value.length > 0 ) {
            submit.disabled = false;
        }
        else {
            submit.disabled = true;
        }
    }

    // Listen for submission of form
    document.querySelector( 'form' ).onsubmit = () => {
        // Find the task submitted
        const task = newTask.value;

        // Create a list of item for the new task and add the task to it
        const li = document.createElement( 'li' );
        li.innerHTML = task;

        // Add new element to our unordored list:
        document.querySelector( '#tasks' ).append( li );

        // Clear out input field
        newTask.value = '';

        // Disable the submit button again
        submit.disabled = true;

        // Stop form from submitting
        return false;
    }

});