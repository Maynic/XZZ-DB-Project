// This scripts check whether the user has logged in so that display
// LOGIN or LOGOUT botton respecitively

// GET current user
function getCurrentUser() {
    var isloggin = sessionStorage.getItem('userId');

    if (isloggin !== null) {
        console.log("isloggin:", isloggin)
        // user is logged in, hide login button and show logout button
        $('.login-button').hide();
        $('.logout-button').show();
        return true;
    } else {
        console.log("isloggin2", isloggin)
        // user is not logged in, show login button and hide logout button
        $('.login-button').show();
        $('.logout-button').hide();
        return false;
    }

    };