$(function () {
    console.log('dziala')
    var button = document.querySelector('#reset_button');
    console.log(button)
    var pass = document.querySelector('#id_password');
    console.log(pass)

    var pass2 = document.querySelector('#id_password2');
    var regPass = /^(?=.*\d)(?=.*[A-z]).{5,}$/i;

    button.addEventListener('click', function(e) {
        if(pass.value.length > 8 && pass.value === pass2.value && regPass.test(pass.value)){

        } else {
            console.log('haslo')
            console.log(regPass.test(pass.value))
            pass.after("Twoje hasło nie może być zbyt podobne do twoich innych danych osobistych.\n" +
                "Twoje hasło musi zawierać co najmniej 8 znaków.\n" +
                "Twoje hasło nie może być powszechnie używanym hasłem.\n" +
                "Twoje hasło nie może składać się tylko z cyfr.")
            e.preventDefault();
        }
    })

});